import pytest
from semester_stats_report.regex import department_regex, subcode_regex, usn_regex


@pytest.mark.parametrize(
    ["usn", "op"],
    [
        ("1AB18ZO156", True),
        ("1AB16NE186", True),
        ("", False),
        ("1CR17CS222", True),
        ("ssddda", False),
    ],
)
def test_usn_regex(usn, op):
    assert bool(usn_regex.fullmatch(usn)) == op


@pytest.mark.parametrize(
    ["subcode", "op"],
    [
        ("15CS66", True),
        ("16CS33", True),
        ("15CSL33", True),
        ("16MATDIP41", True),
        ("17SS661", True),
        ("", False),
        ("sssss", False),
    ],
)
def test_sub_code_regex(subcode, op):
    assert bool(subcode_regex.fullmatch(subcode)) == op


@pytest.mark.parametrize(
    ["dept", "op"],
    [
        ("", False),
        ("A", False),
        ("AA", True),
        ("AAA", True),
        ("AAAA", False),
        ("CSL", True),
    ],
)
def test_dept_regex(dept, op):
    assert bool(department_regex.fullmatch(dept)) == op