"""Lecture 04 practice problems.

Implement each class/function below so tests pass.
Rules:
- Do not change names/signatures.
- Use only the Python standard library.

Problems:
1. log_calls decorator
2. measure_time decorator
3. count_calls decorator
4. ensure_non_negative decorator
5. Retry class decorator
6. Throttle class decorator
7. CallLimit class decorator
8. LruCache class decorator (optional)

"""

from __future__ import annotations

from collections.abc import Callable
from typing import Any
import time
import functools


def log_calls(func: Callable[..., Any]) -> Callable[..., Any]:
    """Problem 1. `log_calls` decorator.

    Print each function call in this format:
    `name(arg1, arg2, kw=value) -> result`

    Hint:
    - Function name: `func.__name__`
    - Positional values: `args`
    - Keyword names/values: `kwargs.items()`

    Example:
    >>> @log_calls
    ... def add(a, b):
    ...     return a + b
    >>> add(2, 3)
    add(2, 3) -> 5
    5
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        parts = [repr(a) for a in args]
        parts += [f"{k}={v!r}" for k, v in kwargs.items()]
        print(f"{func.__name__}({', '.join(parts)}) -> {result!r}")
        return result
    return wrapper


def measure_time(func: Callable[..., Any]) -> Callable[..., Any]:
    """Problem 2. `measure_time` decorator.

    Measure function execution time and print:
    `Executed in <milliseconds> ms`

    Hint:
    - Use `time.perf_counter()` before and after the function call.
    - Convert seconds to milliseconds with `* 1000`.

    Example:
    >>> @measure_time
    ... def work():
    ...     return "done"
    >>> work()
    done
    """
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = (time.perf_counter() - start) * 1000
        print(f"Executed in {elapsed} ms")
        return result
    return wrapper



def count_calls(func: Callable[..., Any]) -> Callable[..., Any]:
    """Problem 3. `count_calls` decorator.

    Count how many times the wrapped function is called.
    Store the counter in `wrapper.calls`.

    Example:
    >>> @count_calls
    ... def ping():
    ...     return "ok"
    >>> ping(); ping()
    'ok'
    >>> ping.calls
    2
    """
    def wrapper(*args, **kwargs):
        wrapper.calls += 1
        return func(*args, **kwargs)
    wrapper.calls = 0
    return wrapper



def ensure_non_negative(func: Callable[..., Any]) -> Callable[..., Any]:
    """Problem 4. `ensure_non_negative` decorator.

    Raise `ValueError` when the decorated function returns a negative number.

    Example:
    >>> @ensure_non_negative
    ... def diff(a, b):
    ...     return a - b
    >>> diff(5, 2)
    3
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if result < 0:
            raise ValueError("Result is negative")
        return result
    return wrapper


class Retry:
    """Problem 5. `Retry(times)` class decorator.

    Implement this as a class with:
    - `__init__(times)` to validate/store `times`
    - `__call__(func)` to return the wrapped function

    Retry a function up to `times` retries after the initial attempt.
    Raise `ValueError` when `times < 0`.

    Example:
    >>> @Retry(2)
    ... def flaky():
    ...     ...
    """

    def __init__(self, times: int) -> None:
        if times < 0:
            raise ValueError("times must be non-negative")
        self.times = times

    def __call__(self, func: Callable[..., Any]) -> Callable[..., Any]:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            last_exc = None
            for attempt in range(1 + self.times):
                try:
                    return func(*args, **kwargs)
                except Exception as exc:
                    last_exc = exc
            raise last_exc
        return wrapper


class Throttle:
    """Problem 6. `Throttle(interval)` class decorator.

    Implement this as a class with:
    - `__init__(interval)` to validate/store the minimum allowed time gap
    - `__call__(func)` to return the wrapped function

    The decorated function may be called at most once per `interval` seconds.
    If it is called again too early, raise `RuntimeError`.

    Requirements:
    - Use `time.perf_counter()` to track call times
    - `interval` must be non-negative, otherwise raise `ValueError`
    - The first call should always succeed
    - If enough time has passed since the previous successful call,
      the next call should succeed
    - Track timing separately for each decorated function

    Example:
    >>> @Throttle(0.5)
    ... def ping():
    ...     return "pong"
    >>> ping()
    'pong'
    >>> ping()
    Traceback (most recent call last):
        ...
    RuntimeError: Too many calls

    Notes:
    - Store the timestamp of the last successful call
    - Only successful calls should update that timestamp
    - Implement this as a class decorator
    """

    def __init__(self, interval: float) -> None:
        if interval < 0:
            raise ValueError("interval must be non-negative")
        self.interval = interval

    def __call__(self, func: Callable[..., Any]) -> Callable[..., Any]:
        last_called: dict[str, float | None] = {"t": None}

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            now = time.perf_counter()
            if last_called["t"] is not None and now - last_called["t"] < self.interval:
                raise RuntimeError("Too many calls")
            result = func(*args, **kwargs)
            last_called["t"] = now
            return result
        return wrapper


class CallLimit:
    """Problem 7 (advanced). `CallLimit(limit)` class decorator.

    Implement this as a class with:
    - `__init__(limit)` to validate/store the maximum allowed number of calls
    - `__call__(func)` to return the wrapped function

    Allow the decorated function to be called at most `limit` times.
    After that, raise `RuntimeError` on every further call.

    Requirements:
    - Raise `ValueError` when `limit < 0`
    - If `limit == 0`, the function must always raise immediately
    - Count only actual attempts to call the function
    - Track the counter separately for each decorated function
    - Store the number of already used calls in `wrapper.calls`

    Example:
    >>> @CallLimit(2)
    ... def greet(name):
    ...     return f"Hello, {name}"
    >>> greet("Alice")
    'Hello, Alice'
    >>> greet("Bob")
    'Hello, Bob'
    >>> greet.calls
    2
    >>> greet("Charlie")
    Traceback (most recent call last):
        ...
    RuntimeError: Call limit exceeded

    Notes:
    - This problem is harder than `count_calls` because behavior changes
      after the limit is reached
    - Implement this as a class decorator
    """

    def __init__(self, limit: int) -> None:
        if limit < 0:
            raise ValueError("limit must be non-negative")
        self.limit = limit

    def __call__(self, func: Callable[..., Any]) -> Callable[..., Any]:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if wrapper.calls >= self.limit:
                raise RuntimeError("Call limit exceeded")
            wrapper.calls += 1
            return func(*args, **kwargs)
        wrapper.calls = 0
        return wrapper


class LruCache:
    """Problem 8 (optional). `LruCache(maxsize)` class decorator.

    Implement this as a class with:
    - `__init__(maxsize)` to store cache size
    - `__call__(func)` to return the wrapped callable

    Use Least Recently Used eviction policy and keep only the last
    `maxsize` used results.

    Example:
    >>> @LruCache(2)
    ... def square(x):
    ...     return x * x
    >>> square(2), square(3), square(2)
    (4, 9, 4)
    """

    def __init__(self, maxsize: int) -> None:
        self.maxsize = maxsize

    def __call__(self, func: Callable[..., Any]) -> Callable[..., Any]:
        from collections import OrderedDict
        cache: OrderedDict[Any, Any] = OrderedDict()

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            key = (args, tuple(sorted(kwargs.items())))
            if key in cache:
                cache.move_to_end(key)
                return cache[key]
            result = func(*args, **kwargs)
            if self.maxsize > 0:
                cache[key] = result
                if len(cache) > self.maxsize:
                    cache.popitem(last=False)
            return result
        return wrapper
