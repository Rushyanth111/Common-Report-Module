from _pytest.mark import pytest_unconfigure
from semester_stats_report.helpers import score_check, student_check, subject_check
from semester_stats_report.reports import ScoreReport, StudentReport, SubjectReport
import pytest
from semester_stats_report import DepartmentReport, department_check


@pytest.mark.parametrize(
    ["dept_set", "check", "op"],
    [
        ({"AA"}, "CS", False),
        ({"CS", "XD", "DS"}, "DS", True),
        ({"HO", "OH"}, "OOH", False),
        ({}, "SS", False),
    ],
)
def test_check_department(dept_set, check, op):
    depset = {DepartmentReport(Code=x, Name="A") for x in dept_set}

    assert department_check(depset, check) == op


@pytest.mark.parametrize(
    ["student_set", "check", "op"],
    [
        ({"1CR15TE117"}, "1CR15TE117", True),
        ({"1CR15TE117", "1CR15TE113", "1CR15TE119"}, "1CR15TE116", False),
        ({}, "1CR15TE117", False),
    ],
)
def test_check_student(student_set, check, op):
    student_set = {StudentReport(Name="X", Usn=x) for x in student_set}

    assert student_check(student_set, check) == op


@pytest.mark.parametrize(
    ["subject_set", "check", "op"],
    [
        ({"15CS13", "15CS31"}, "15CS31", True),
        ({"15CS13", "15CS31"}, "15CS41", False),
        ({}, "15CS31", False),
    ],
)
def test_check_subject(subject_set, check, op):
    subject_set = {SubjectReport(Code=x, Name="A") for x in subject_set}

    assert subject_check(subject_set, check) == op


@pytest.mark.parametrize(
    [
        "students",
        "subjects",
        "internals",
        "externals",
        "student",
        "subject",
        "internal",
        "external",
        "op",
    ],
    [
        (
            ["1CR17CS118", "1CR15TE117", "1CR15TE119"],
            ["17CS13", "15CS31", "15CS56"],
            [30, 20, 10],
            [40, 50, 60],
            "1CR15TE119",
            "15CS56",
            10,
            60,
            True,
        ),
        (
            ["1CR17CS118", "1CR15TE117", "1CR15TE119"],
            ["17CS13", "15CS31", "15CS56"],
            [30, 20, 10],
            [40, 50, 60],
            "1CR15TE119",
            "15CS66",
            10,
            60,
            False,
        ),
        ([], [], [], [], "1CR15TE119", "15CS56", 10, 60, False),
    ],
)
def test_check_student(
    students, subjects, internals, externals, student, subject, internal, external, op
):
    score_set = {
        ScoreReport(Usn=usn, SubjectCode=code, Internals=inte, Externals=ext)
        for (usn, code, inte, ext) in zip(students, subjects, internals, externals)
    }

    score_check(score_set, student, subject, internal, external) == op
