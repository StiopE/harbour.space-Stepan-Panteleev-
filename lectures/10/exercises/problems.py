"""Lecture 10 practice problems: threading, multiprocessing, and async/await.

Implement each function below so tests pass.
Rules:
- Do not change function names/signatures.
- Use only the Python standard library.
"""

from __future__ import annotations

import asyncio
import threading
import time
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor


def simulated_long_fetch(value: object) -> object:
    """Helper function: Simulate a slow blocking fetch and return the same input value."""
    time.sleep(0.1)
    return value


async def async_simulated_long_fetch(value: object) -> object:
    """Helper function: Simulate a slow async fetch and return the same input value."""
    await asyncio.sleep(0.1)
    return value


def locked_counter_total(num_threads: int, increments_per_thread: int) -> int:
    """Mission 1: thread-safe counter increment with `threading.Lock`."""
    counter = 0
    lock = threading.Lock()

    def worker() -> None:
        nonlocal counter
        for _ in range(increments_per_thread):
            with lock:
                counter += 1

    threads = [threading.Thread(target=worker) for _ in range(num_threads)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    return counter


def threaded_square_map(values: list[int]) -> list[int]:
    """Mission 2: compute squares using one thread per element."""
    results = [0] * len(values)

    def worker(idx: int, val: int) -> None:
        results[idx] = val * val

    threads = [threading.Thread(target=worker, args=(i, v)) for i, v in enumerate(values)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    return results


def threadpool_sleep_map(delays: list[float], max_workers: int = 4) -> list[float]:
    """Mission 3: simulate blocking I/O with `ThreadPoolExecutor`."""
    if max_workers < 1:
        raise ValueError("max_workers must be >= 1")
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        return list(executor.map(simulated_long_fetch, delays))


def _square(x: int) -> int:
    return x * x


def processpool_square_map(values: list[int], max_workers: int = 2) -> list[int]:
    """Mission 4: compute squares with `ProcessPoolExecutor`."""
    if max_workers < 1:
        raise ValueError("max_workers must be >= 1")
    with ProcessPoolExecutor(max_workers=max_workers) as executor:
        return list(executor.map(_square, values))


async def async_tag_fetch(labels: list[str], delay: float = 0.01) -> list[str]:
    """Mission 5: run async tasks concurrently with `asyncio.gather`."""

    async def fetch_one(label: str) -> str:
        await async_simulated_long_fetch(label)
        return f"done:{label}"

    return list(await asyncio.gather(*(fetch_one(l) for l in labels)))


async def async_blocking_double(values: list[int]) -> list[int]:
    """Mission 6: bridge blocking work into async flow."""

    async def fetch_and_double(val: int) -> int:
        result = await asyncio.to_thread(simulated_long_fetch, val)
        return result * 2

    return list(await asyncio.gather(*(fetch_and_double(v) for v in values)))
