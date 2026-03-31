"""Problem 02: Write rows into `students` using sqlite3.

Task:
1. Connect to `school.db`
2. Insert all rows from STUDENTS into `students`
3. Commit changes
4. Print how many rows were inserted

Tip:
- Use `executemany` with placeholders `(?, ?, ?, ?)`.
"""

import sqlite3

DB_PATH = "school.db"

STUDENTS = [
    ("Ana", 21, "ana@example.com", "backend"),
    ("Omar", 24, "omar@example.com", "data"),
    ("Lina", 22, "lina@example.com", "backend"),
    ("Marta", 20, "marta@example.com", "frontend"),
    ("Ivan", 23, "ivan@example.com", "data"),
]


def main() -> None:
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    # TODO: insert STUDENTS rows here.
    # cur.executemany("INSERT INTO students (name, age, email, track) VALUES (?, ?, ?, ?)", STUDENTS)

    conn.commit()
    print("Inserted rows:", cur.rowcount)
    conn.close()


if __name__ == "__main__":
    main()
