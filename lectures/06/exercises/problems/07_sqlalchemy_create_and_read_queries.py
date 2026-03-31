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
        first_student = session.scalars(select(Student)).first()
        if first_student:
            assignment = Assignment(
                title="SQL Basics Homework",
                score=95,
                student_id=first_student.id,
            )
            session.add(assignment)
            session.flush()

        all_students = session.scalars(select(Student)).all()
        print("All students:")
        for s in all_students:
            print(f"  {s.id}: {s.name}, age={s.age}, track={s.track}")

        older_students = session.scalars(
            select(Student).where(Student.age >= 22).order_by(Student.age.desc())
        ).all()
        print("\nStudents with age >= 22 (desc):")
        for s in older_students:
            print(f"  {s.name}, age={s.age}")

        assignments = session.scalars(
            select(Assignment)
        ).all()
        print("\nAssignments:")
        for a in assignments:
            print(f"  {a.title} (score={a.score}) — student: {a.student.name}")

        session.commit()


if __name__ == "__main__":
    main()
