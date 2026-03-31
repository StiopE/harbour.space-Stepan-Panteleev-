"""Shared SQLAlchemy ORM models for Problems 06-07.

Task:
- Keep Student mapped to existing `students` table.
- Add Assignment as related model (many assignments per student).
- Complete relationship fields in both models.
"""

from __future__ import annotations

from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


class Student(Base):
    __tablename__ = "students"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    age: Mapped[int] = mapped_column(Integer, nullable=False)
    email: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    track: Mapped[str] = mapped_column(String, nullable=False)

    # TODO: add relationship to Assignment
    # assignments: Mapped[list["Assignment"]] = relationship(back_populates="student")


class Assignment(Base):
    __tablename__ = "assignments"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String, nullable=False)
    score: Mapped[int] = mapped_column(Integer, nullable=False)
    student_id: Mapped[int] = mapped_column(ForeignKey("students.id"), nullable=False)

    # TODO: add relationship back to Student
    # student: Mapped[Student] = relationship(back_populates="assignments")
