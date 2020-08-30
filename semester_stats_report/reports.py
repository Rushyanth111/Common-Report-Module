from re import sub
from typing import Optional, Tuple, List

from pydantic import BaseModel, validator
from .regex import department_regex, usn_regex, subcode_regex


def dept_validate(dept: str):
    dept = dept.upper()
    if department_regex.match(dept) is None:
        raise ValueError("Not a Department Code.")
    return dept


def usn_validate(usn: str):
    usn = usn.upper()
    if usn_regex.match(usn) is None:
        raise ValueError("Not a Valid Usn")
    return usn


def subcode_validate(subcode: str):
    subcode = subcode.upper()
    if subcode_regex.match(subcode) is None:
        raise ValueError("Not a valid Subject Code")
    return subcode


class DepartmentReport(BaseModel):
    Code: str
    Name: str

    def __eq__(self, o: "DepartmentReport") -> bool:
        return self.Code == o.Code

    def __hash__(self) -> int:
        return hash(self.Code)

    _code_check = validator("Code", pre=True)(dept_validate)


class StudentReport(BaseModel):
    Usn: str
    Name: str

    def __hash__(self) -> int:
        return hash(self.Usn)

    def __eq__(self, o: "StudentReport") -> bool:
        return self.Usn == o.Usn

    _usn_check = validator("Usn")(usn_validate)


class SubjectReport(BaseModel):
    Code: str
    Name: str

    def __hash__(self) -> int:
        return hash(self.Code)

    def __eq__(self, o: "SubjectReport") -> bool:
        return self.Code == o.Code

    _subcode_check = validator("Code")(subcode_validate)


class ScoreReport(BaseModel):
    Usn: str
    SubjectCode: str
    Internals: int
    Externals: int

    _usn_check = validator("Usn", pre=True)(usn_validate)
    _subcode_check = validator("SubjectCode", pre=True)(subcode_validate)

    def __hash__(self) -> int:
        return hash((self.Usn, self.SubjectCode, self.Internals, self.Externals))

    def __eq__(self, o: "ScoreReport") -> bool:
        return (
            self.Usn == o.Usn
            and self.SubjectCode == o.SubjectCode
            and self.Internals == o.Internals
            and self.Externals == o.Internals
        )

    def __gt__(self, o: "ScoreReport") -> bool:
        return (self.Internals + self.Externals) > (o.Internals + o.Externals)

    def __ge__(self, o: "ScoreReport") -> bool:
        return (self.Internals + self.Externals) >= (o.Internals + o.Externals)


class SubjectScoreList(BaseModel):
    Code: str
    Name: str
    Internal: int
    External: int

    def __hash__(self) -> int:
        return hash((self.Code, self.Name, self.Internal, self.External))

    def __eq__(self, o: object) -> bool:
        return (
            self.Code == o.Code
            and self.Internal == o.Internal
            and self.External == o.External
        )

    _subcode_check = validator("Code", pre=True)(subcode_validate)


class MergedReport(BaseModel):
    Usn: str
    Name: str
    Scores: List[SubjectScoreList]

    _usn_check = validator("Usn", pre=True)(usn_validate)
