"""Auto-tests for lecture 09 exercises.

Default target module: problems
Override with: SOLUTIONS_MODULE=reference_solutions
"""

from __future__ import annotations

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


class Lecture09InternalsTest(unittest.TestCase):
    def test_extract_opnames(self) -> None:
        opnames = problems.extract_opnames("x = 2 + 3\nprint(x)")
        self.assertIsInstance(opnames, list)
        self.assertTrue(opnames)
        self.assertIn("STORE_NAME", opnames)
        self.assertTrue("RETURN_VALUE" in opnames or "RETURN_CONST" in opnames)
        self.assertTrue(any(name.startswith("CALL") for name in opnames))

    def test_aliasing_after_append(self) -> None:
        a, b, same_identity = problems.aliasing_after_append()
        self.assertEqual(a, [1, 2, 3])
        self.assertEqual(b, [1, 2, 3])
        self.assertTrue(same_identity)

    def test_copy_after_append(self) -> None:
        a, b, same_identity = problems.copy_after_append()
        self.assertEqual(a, [1, 2])
        self.assertEqual(b, [1, 2, 3])
        self.assertFalse(same_identity)

    def test_rebind_after_concat(self) -> None:
        a, b, same_identity = problems.rebind_after_concat()
        self.assertEqual(a, [1, 2])
        self.assertEqual(b, [1, 2, 3])
        self.assertFalse(same_identity)

    def test_refcount_steps(self) -> None:
        start_count, with_alias_count, after_delete_count = problems.refcount_steps()
        self.assertGreater(start_count, 0)
        self.assertEqual(with_alias_count, start_count + 1)
        self.assertEqual(after_delete_count, start_count)

    def test_make_incrementer(self) -> None:
        inc = problems.make_incrementer(10)
        self.assertEqual(inc(), 11)
        self.assertEqual(inc(), 12)
        self.assertEqual(inc(), 13)

    def test_inject_with_exec(self) -> None:
        ns: dict[str, object] = {}
        returned = problems.inject_with_exec(ns, "mystery = 42")
        self.assertIs(returned, ns)
        self.assertEqual(ns.get("mystery"), 42)

    def test_function_locals_snapshot(self) -> None:
        snapshot = problems.function_locals_snapshot()
        self.assertEqual(snapshot, {"a": 10, "b": 20})

    def test_cycle_collected(self) -> None:
        self.assertTrue(problems.cycle_collected())

    def test_shallow_vs_deep_copy_state(self) -> None:
        original, shallow, deep = problems.shallow_vs_deep_copy_state()
        self.assertEqual(original, [[1, 99], [2]])
        self.assertEqual(shallow, [[1, 99], [2]])
        self.assertEqual(deep, [[1], [2]])


if __name__ == "__main__":
    unittest.main()
