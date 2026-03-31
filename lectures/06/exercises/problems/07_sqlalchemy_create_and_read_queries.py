"""Problem 07: Create and read data with SQLAlchemy.

Task:
1. Open a SQLAlchemy Session on `school.db`.
2. Create one Assignment for an existing student.
3. Read all students.
4. Read students with age >= 22 sorted by age descending.
5. Read assignments with joined student names.

Starter:
- Reuse `Student` and `Assignment` from `db_models.py`.
- Use `select(...)` queries.
"""

from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session

from db_models import Assignment, Student

DB_URL = "sqlite:///school.db"


def main() -> None:
    engine = create_engine(DB_URL, echo=False)

    with Session(engine) as session:
        # TODO 1: add an assignment for an existing student

        # TODO 2: read all students

        # TODO 3: read filtered + sorted students

        # TODO 4: read assignments with student data

        session.commit()


if __name__ == "__main__":
    main()
