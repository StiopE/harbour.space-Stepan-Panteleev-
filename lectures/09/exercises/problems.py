"""Lecture 09 exercises (Python internals).

Implement each function as a small experiment.

Use this mental model:
names -> references -> objects
"""

from __future__ import annotations

from collections.abc import Callable


def extract_opnames(source: str) -> list[str]:
    """Mission 1 (Optional): inspect bytecode produced from source text.

    Goal:
        Show that Python executes bytecode instructions.

    Steps:
        1. Compile `source` in module/exec mode.
        2. Iterate through the compiled instructions.
        3. Return only instruction names (`opname`).

    Example:
        source = "x = 2 + 3\\nprint(x)"
        output shape: ["RESUME", "LOAD_CONST", ...]
    """
    raise NotImplementedError


def aliasing_after_append() -> tuple[list[int], list[int], bool]:
    """Mission 2: demonstrate aliasing (two names, one list object).

    Build:
        a = [1, 2]
        b = a
        b.append(3)

    Expectation:
        both `a` and `b` become [1, 2, 3].

    Return:
        (a, b, same_identity) where same_identity is `id(a) == id(b)`.
    """
    raise NotImplementedError


def copy_after_append() -> tuple[list[int], list[int], bool]:
    """Mission 3: show how shallow copy avoids top-level aliasing.

    Build:
        a = [1, 2]
        b = a.copy()
        b.append(3)

    Expectation:
        `a` stays [1, 2], `b` becomes [1, 2, 3].

    Return:
        (a, b, same_identity) where same_identity should be False.
    """
    raise NotImplementedError


def rebind_after_concat() -> tuple[list[int], list[int], bool]:
    """Mission 4: compare rebinding with in-place mutation.

    Build:
        a = [1, 2]
        b = a
        b = b + [3]  # creates new object

    Key idea:
        `b = b + [3]` rebinds `b` to a new list instead of mutating `a`.

    Return:
        (a, b, same_identity) with `a == [1, 2]`, `b == [1, 2, 3]`,
        and same_identity False.
    """
    raise NotImplementedError


def refcount_steps() -> tuple[int, int, int]:
    """Mission 5: track reference count changes when aliasing.

    Use `sys.getrefcount(obj)` to measure one object's refcount in three moments:
        1. before creating an alias
        2. after creating an alias
        3. after deleting that alias

    Return:
        (start_count, with_alias_count, after_delete_count)

    Expected relation:
        with_alias_count == start_count + 1
        after_delete_count == start_count
    """
    raise NotImplementedError


def make_incrementer(start: int = 0) -> Callable[[], int]:
    """Mission 6: build a stateful closure with `nonlocal`.

    Return a function that:
        - remembers internal value starting from `start`
        - increments that value by 1 on each call
        - returns the new value

    Example:
        inc = make_incrementer(10)
        inc() -> 11
        inc() -> 12
    """
    raise NotImplementedError


def inject_with_exec(namespace: dict[str, object], statement: str) -> dict[str, object]:
    """Mission 7 (Optional): inject names dynamically using `exec`.

    Execute `statement` in the provided `namespace` dictionary.
    Return the same dictionary object after execution.

    Example:
        ns = {}
        inject_with_exec(ns, "x = 42")
        ns["x"] == 42
    """
    raise NotImplementedError


def function_locals_snapshot() -> dict[str, int]:
    """Mission 8: capture local namespace from inside a function.

    Build an inner function where:
        a = 10
        b = 20

    Return `dict(locals())` from that inner function.
    Expected output shape: {"a": 10, "b": 20}
    """
    raise NotImplementedError


def cycle_collected() -> bool:
    """Mission 9 (Optional): verify cycle garbage collection.

    Create two objects that reference each other (a cycle).
    Keep weak references to both objects, delete strong references,
    run `gc.collect()`, then check weak refs.

    Return:
        True only if both weak references are now None.
    """
    raise NotImplementedError


def shallow_vs_deep_copy_state() -> tuple[list[list[int]], list[list[int]], list[list[int]]]:
    """Mission 10: compare shallow vs deep copy for nested lists.

    Build:
        original = [[1], [2]]
        shallow = original.copy()
        deep = deepcopy(original)
        shallow[0].append(99)

    Return:
        (original, shallow, deep)

    Expected outcome:
        original == [[1, 99], [2]]
        shallow == [[1, 99], [2]]
        deep == [[1], [2]]
    """
    raise NotImplementedError
