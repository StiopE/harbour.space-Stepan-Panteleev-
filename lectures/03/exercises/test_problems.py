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

THIS_DIR = Path(__file__).resolve().parent
if str(THIS_DIR) not in sys.path:
    sys.path.insert(0, str(THIS_DIR))

MODULE_NAME = os.getenv("SOLUTIONS_MODULE", "problems")
problems = importlib.import_module(MODULE_NAME)


class Lecture03ProblemsTest(unittest.TestCase):
    def test_countdown(self) -> None:
        c = problems.Countdown(5)
        self.assertEqual(list(c), [5, 4, 3, 2, 1, 0])
        self.assertEqual(list(c), [5, 4, 3, 2, 1, 0])
        self.assertEqual(list(problems.Countdown(-1)), [])

    def test_step_iterator(self) -> None:
        self.assertEqual(list(problems.StepIterator([10, 20, 30, 40, 50, 60])), [10, 30, 50])
        self.assertEqual(list(problems.StepIterator([1, 2, 3, 4, 5, 6, 7], step=3)), [1, 4, 7])
        with self.assertRaises(ValueError):
            problems.StepIterator([1, 2], step=0)

    def test_unique_consecutive_iterator(self) -> None:
        data = [1, 1, 2, 2, 2, 3, 1, 1]
        self.assertEqual(list(problems.UniqueConsecutiveIterator(data)), [1, 2, 3, 1])
        self.assertEqual(list(problems.UniqueConsecutiveIterator([1, 2, 1, 2])), [1, 2, 1, 2])
        self.assertEqual(list(problems.UniqueConsecutiveIterator([])), [])

    def test_circular_iterator(self) -> None:
        it = problems.CircularIterator(["A", "B", "C"], 8)
        self.assertEqual(list(it), ["A", "B", "C", "A", "B", "C", "A", "B"])
        self.assertEqual(list(problems.CircularIterator([1, 2], 0)), [])
        with self.assertRaises(ValueError):
            problems.CircularIterator([], 3)
        with self.assertRaises(ValueError):
            problems.CircularIterator([1], -1)

    def test_read_words(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            path = Path(tmpdir) / "sample.txt"
            path.write_text("  one   two\n\nthree\n   four   five  ", encoding="utf-8")
            self.assertEqual(list(problems.read_words(str(path))), ["one", "two", "three", "four", "five"])

    def test_batch(self) -> None:
        self.assertEqual(list(problems.batch([1, 2, 3, 4, 5, 6, 7], 3)), [[1, 2, 3], [4, 5, 6], [7]])
        self.assertEqual(list(problems.batch((x for x in range(5)), 2)), [[0, 1], [2, 3], [4]])
        with self.assertRaises(ValueError):
            list(problems.batch([1, 2, 3], 0))

    def test_flatten_generator(self) -> None:
        data = [1, [2, 3], [4, [5, 6]], 7]
        self.assertEqual(list(problems.flatten(data)), [1, 2, 3, 4, 5, 6, 7])
        self.assertEqual(list(problems.flatten([[], [1, [2]], 3])), [1, 2, 3])

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
        attempts = {"n": 0}

        @problems.retry(2)
        def flaky() -> str:
            attempts["n"] += 1
            if attempts["n"] < 3:
                raise RuntimeError("fail")
            return "ok"

        self.assertEqual(flaky(), "ok")
        self.assertEqual(attempts["n"], 3)

        failures = {"n": 0}

        @problems.retry(1)
        def always_fail() -> None:
            failures["n"] += 1
            raise ValueError("boom")

        with self.assertRaises(ValueError):
            always_fail()
        self.assertEqual(failures["n"], 2)

        with self.assertRaises(ValueError):
            problems.retry(-1)

    def test_lru_cache(self) -> None:
        calls = {"n": 0}

        @problems.lru_cache(2)
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

        @problems.lru_cache(0)
        def identity(x: int) -> int:
            no_cache_calls["n"] += 1
            return x

        self.assertEqual(identity(1), 1)
        self.assertEqual(identity(1), 1)
        self.assertEqual(no_cache_calls["n"], 2)

        kw_calls = {"n": 0}

        @problems.lru_cache(2)
        def greet(name: str, prefix: str = "Hi") -> str:
            kw_calls["n"] += 1
            return f"{prefix} {name}"

        self.assertEqual(greet("Ana", prefix="Hello"), "Hello Ana")
        self.assertEqual(greet("Ana", prefix="Hello"), "Hello Ana")
        self.assertEqual(kw_calls["n"], 1)


if __name__ == "__main__":
    unittest.main()
