"""Auto-tests for lecture 03 exercises.

Default target module: problems
Override with: SOLUTIONS_MODULE=reference_solutions
"""

from __future__ import annotations

import importlib
import io
import os
import sys
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path
from unittest.mock import patch

THIS_DIR = Path(__file__).resolve().parent
if str(THIS_DIR) not in sys.path:
    sys.path.insert(0, str(THIS_DIR))

MODULE_NAME = os.getenv("SOLUTIONS_MODULE", "problems")
problems = importlib.import_module(MODULE_NAME)


class Lecture03ProblemsTest(unittest.TestCase):

    def test_log_calls(self) -> None:
        @problems.log_calls
        def add(a: int, b: int) -> int:
            return a + b

        out = io.StringIO()
        with redirect_stdout(out):
            result = add(2, 3)
        self.assertEqual(result, 5)
        self.assertEqual(out.getvalue().strip(), "add(2, 3) -> 5")

    def test_measure_time(self) -> None:
        @problems.measure_time
        def multiply(a: int, b: int) -> int:
            return a * b

        out = io.StringIO()
        with redirect_stdout(out):
            result = multiply(3, 4)
        self.assertEqual(result, 12)
        text = out.getvalue().strip()
        self.assertTrue(text.startswith("Executed in "))
        self.assertTrue(text.endswith(" ms"))

    def test_count_calls(self) -> None:
        @problems.count_calls
        def ping(x: int) -> int:
            return x

        self.assertEqual(ping.calls, 0)
        ping(1)
        ping(2)
        ping(3)
        self.assertEqual(ping.calls, 3)

    def test_ensure_non_negative(self) -> None:
        @problems.ensure_non_negative
        def diff(a: int, b: int) -> int:
            return a - b

        self.assertEqual(diff(5, 2), 3)
        with self.assertRaises(ValueError):
            diff(2, 5)

    def test_retry(self) -> None:
        self.assertIsInstance(problems.Retry, type)

        attempts = {"n": 0}

        @problems.Retry(2)
        def flaky() -> str:
            attempts["n"] += 1
            if attempts["n"] < 3:
                raise RuntimeError("fail")
            return "ok"

        self.assertEqual(flaky(), "ok")
        self.assertEqual(attempts["n"], 3)

        failures = {"n": 0}

        @problems.Retry(1)
        def always_fail() -> None:
            failures["n"] += 1
            raise ValueError("boom")

        with self.assertRaises(ValueError):
            always_fail()
        self.assertEqual(failures["n"], 2)

        with self.assertRaises(ValueError):
            problems.Retry(-1)

    def test_throttle(self) -> None:
        self.assertIsInstance(problems.Throttle, type)

        with self.assertRaises(ValueError):
            problems.Throttle(-0.1)

        calls = {"f": 0, "g": 0}

        @problems.Throttle(1.0)
        def first() -> str:
            calls["f"] += 1
            return "first"

        @problems.Throttle(1.0)
        def second() -> str:
            calls["g"] += 1
            return "second"

        with patch.object(problems.time, "perf_counter", side_effect=[10.0, 10.2, 10.3, 11.05]):
            self.assertEqual(first(), "first")
            with self.assertRaises(RuntimeError):
                first()
            self.assertEqual(second(), "second")
            self.assertEqual(first(), "first")

        self.assertEqual(calls["f"], 2)
        self.assertEqual(calls["g"], 1)

    def test_call_limit(self) -> None:
        self.assertIsInstance(problems.CallLimit, type)

        with self.assertRaises(ValueError):
            problems.CallLimit(-1)

        limiter = problems.CallLimit(2)
        calls = {"hello": 0, "bye": 0}

        @limiter
        def hello(name: str) -> str:
            calls["hello"] += 1
            return f"Hello, {name}"

        @limiter
        def bye() -> str:
            calls["bye"] += 1
            return "bye"

        self.assertEqual(hello("Alice"), "Hello, Alice")
        self.assertEqual(hello("Bob"), "Hello, Bob")
        with self.assertRaises(RuntimeError):
            hello("Charlie")
        self.assertEqual(calls["hello"], 2)

        self.assertEqual(bye(), "bye")
        self.assertEqual(bye(), "bye")
        with self.assertRaises(RuntimeError):
            bye()
        self.assertEqual(calls["bye"], 2)

        @problems.CallLimit(0)
        def never() -> None:
            raise AssertionError("must not be called when limit is zero")

        with self.assertRaises(RuntimeError):
            never()

    def test_lru_cache(self) -> None:
        self.assertIsInstance(problems.LruCache, type)

        calls = {"n": 0}

        @problems.LruCache(2)
        def square(x: int) -> int:
            calls["n"] += 1
            return x * x

        self.assertEqual(square(2), 4)
        self.assertEqual(square(3), 9)
        self.assertEqual(square(2), 4)
        self.assertEqual(calls["n"], 2)
        self.assertEqual(square(4), 16)
        self.assertEqual(square(3), 9)
        self.assertEqual(calls["n"], 4)

        no_cache_calls = {"n": 0}

        @problems.LruCache(0)
        def identity(x: int) -> int:
            no_cache_calls["n"] += 1
            return x

        self.assertEqual(identity(1), 1)
        self.assertEqual(identity(1), 1)
        self.assertEqual(no_cache_calls["n"], 2)

        kw_calls = {"n": 0}

        @problems.LruCache(2)
        def greet(name: str, prefix: str = "Hi") -> str:
            kw_calls["n"] += 1
            return f"{prefix} {name}"

        self.assertEqual(greet("Ana", prefix="Hello"), "Hello Ana")
        self.assertEqual(greet("Ana", prefix="Hello"), "Hello Ana")
        self.assertEqual(kw_calls["n"], 1)


if __name__ == "__main__":
    unittest.main()
