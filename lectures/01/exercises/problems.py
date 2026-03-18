"""Lecture 01 practice problems.

Implement each function below so tests pass.
Rules:
- Do not change function names/signatures.
- Keep implementations pure unless the function explicitly needs I/O.
- Use only the Python standard library.
"""

from __future__ import annotations
import re
from collections import Counter
from collections import deque
from collections import defaultdict

def normalize_username(name: str) -> str:
    """Return a normalized username.

    Rules:
    - Trim outer whitespace
    - Lowercase everything
    - Replace internal whitespace runs with a single underscore
    """
    return re.sub(r'\s+', '_', name.strip().lower())
    raise NotImplementedError

def is_valid_age(age: int) -> bool:
    """Return True if age is in [18, 120], otherwise False."""
    if age >= 18 and age <= 120:
        return True
    else:
        return False
    
    raise NotImplementedError


def truthy_values(values: list[object]) -> list[object]:
    """Return a new list containing only truthy values from input."""
    l = []
    for i in range(len(values)):
        if values[i]:
            l.append(values[i])
    return l
    raise NotImplementedError


def sum_until_negative(numbers: list[int]) -> int:
    """Return sum of numbers until the first negative value (exclusive)."""

    sums = 0
    for i in range(len(numbers)):
        if numbers[i] < 0:
            return sums
        else:
            sums += numbers[i]
    return sums


def skip_multiples_of_three(numbers: list[int]) -> list[int]:
    """Return numbers excluding values divisible by 3."""
    l = []
    for i in range(len(numbers)):
        if numbers[i] % 3 == 0:
            continue
        else:
            l.append(numbers[i])
    return l
    raise NotImplementedError


def first_even_or_none(numbers: list[int]) -> int | None:
    """Return the first even number, or None if no even number exists."""
    for i in range(len(numbers)):
        if numbers[i] % 2 == 0:
            return numbers[i]
    return None


def squares_of_even(numbers: list[int]) -> list[int]:
    """Return squares of all even numbers in input order."""
    l = []
    for i in range(len(numbers)):
        if numbers[i] % 2 == 0:
            l.append(numbers[i]**2)
    return l
    raise NotImplementedError


def word_lengths(words: list[str]) -> dict[str, int]:
    """Return dict mapping each word to its length."""
    return {word: len(word) for word in words}
    raise NotImplementedError


def zip_to_pairs(keys: list[str], values: list[int]) -> list[tuple[str, int]]:
    """Zip keys and values into list of pairs. Ignore extras in longer list."""
    return list(zip(keys, values))
    raise NotImplementedError


def build_user(name: str, role: str = "student", active: bool = True) -> dict[str, object]:
    """Build and return {'name': name, 'role': role, 'active': active}."""
    return {'name': name, 'role': role, 'active': active}

    raise NotImplementedError


def append_tag_safe(tag: str, tags: list[str] | None = None) -> list[str]:
    """Append tag to tags safely (no shared mutable default across calls)."""
    if tags is None:
        tags = []
    tags.append(tag)
    return tags    

    raise NotImplementedError


def invert_dict(mapping: dict[str, int]) -> dict[int, str]:
    """Invert mapping. Assume values are unique."""
    inv_map = {v: k for k, v in mapping.items()}
        
    return inv_map
    raise NotImplementedError


def unique_sorted_tags(tags: list[str]) -> list[str]:
    """Return unique tags sorted ascending."""
    return sorted(set(tags))
    raise NotImplementedError


def count_words(words: list[str]) -> dict[str, int]:
    """Count occurrences of each word using collections.Counter."""
    count = Counter(words)
    return count

    raise NotImplementedError


def group_scores(records: list[tuple[str, int]]) -> dict[str, list[int]]:
    """Group scores by student name using collections.defaultdict(list)."""

    grouped = defaultdict(list)

    for name, score in records:
        grouped[name].append(score)
    
    return dict(grouped)
    raise NotImplementedError


def rotate_queue(items: list[str], steps: int) -> list[str]:
    """Rotate queue to the right by `steps` using collections.deque and return as list."""
    d = deque(items)
    d.rotate(steps)
    return list(d)
    raise NotImplementedError


def safe_int(value: str) -> int | None:
    """Convert string to int, returning None if conversion fails."""
    try:
        value = int(value)
        return value
    except ValueError:
        return None
    raise NotImplementedError


def read_lines(path: str) -> list[str]:
    """Read a text file with a context manager and return non-empty stripped lines."""
    try:
        with open(path, 'r', encoding='utf-8') as file:
            return [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        return []
    



def top_n_scores(scores: list[int], n: int = 3) -> list[int]:
    """Return top `n` scores in descending order."""
    sorted_scores = sorted(scores, reverse=True)
    return sorted_scores[:n] 

    raise NotImplementedError


def all_passed(scores: list[int], threshold: int = 50) -> bool:
    """Return True if every score is >= threshold."""
    for i in range(len(scores)):
        if scores[i] < threshold:
            return False
    return True
