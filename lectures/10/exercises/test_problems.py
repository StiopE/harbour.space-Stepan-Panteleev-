"""Auto-tests for lecture 10 exercises.

Default target module: problems
Override with: SOLUTIONS_MODULE=reference_solutions
"""

from __future__ import annotations

import asyncio
import importlib
import os
import sys
import unittest
from pathlib import Path

THIS_DIR = Path(__file__).resolve().parent
if str(THIS_DIR) not in sys.path:
    sys.path.insert(0, str(THIS_DIR))

MODULE_NAME = os.getenv("SOLUTIONS_MODULE", "problems")
problems = importlib.import_module(MODULE_NAME)


class Lecture10ConcurrencyTest(unittest.TestCase):
    def test_simulated_long_fetch(self) -> None:
        self.assertEqual(problems.simulated_long_fetch("x"), "x")

    def test_async_simulated_long_fetch(self) -> None:
        self.assertEqual(asyncio.run(problems.async_simulated_long_fetch("y")), "y")

    def test_locked_counter_total(self) -> None:
        self.assertEqual(problems.locked_counter_total(4, 1000), 4000)
        self.assertEqual(problems.locked_counter_total(0, 10), 0)

    def test_threaded_square_map(self) -> None:
        self.assertEqual(problems.threaded_square_map([2, -3, 4]), [4, 9, 16])
        self.assertEqual(problems.threaded_square_map([]), [])

    def test_threadpool_sleep_map(self) -> None:
        delays = [0.001, 0.002, 0.001]
        self.assertEqual(problems.threadpool_sleep_map(delays, max_workers=2), delays)
        with self.assertRaises(ValueError):
            problems.threadpool_sleep_map(delays, max_workers=0)

    def test_processpool_square_map(self) -> None:
        self.assertEqual(problems.processpool_square_map([1, 2, 3, 4], max_workers=2), [1, 4, 9, 16])
        with self.assertRaises(ValueError):
            problems.processpool_square_map([1], max_workers=0)

    def test_async_tag_fetch(self) -> None:
        result = asyncio.run(problems.async_tag_fetch(["a", "b", "c"], delay=0.001))
        self.assertEqual(result, ["done:a", "done:b", "done:c"])

    def test_async_blocking_double(self) -> None:
        result = asyncio.run(problems.async_blocking_double([1, 2, 3]))
        self.assertEqual(result, [2, 4, 6])


if __name__ == "__main__":
    unittest.main()
