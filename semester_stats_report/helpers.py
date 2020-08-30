from typing import Set
from .reports import DepartmentReport, ScoreReport, StudentReport, SubjectReport


def department_check(dept_set: Set[DepartmentReport], code: str):
    if DepartmentReport(Name="A", Code=code) in dept_set:
        return True

    return False


def student_check(student_set: Set[StudentReport], usn: str):
    if StudentReport(Usn=usn, Name="A") in student_set:
        return True

    return False


def subject_check(subject_set: Set[SubjectReport], subcode: str):
    if SubjectReport(Code=subcode, Name="A") in subject_set:
        return True

    return False


def score_check(
    student_set: Set[ScoreReport],
    usn: str,
    subcode: str,
    internals: int,
    externals: int,
):
    if (
        ScoreReport(
            Usn=usn, SubjectCode=subcode, Internals=internals, Externals=externals
        )
        in student_set
    ):
        return True

    return False
