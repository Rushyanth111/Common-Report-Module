from typing import Optional

from pydantic import BaseModel


class DepartmentReport(BaseModel):
    Code: str
    Name: str

    def __eq__(self, o: "DepartmentReport") -> bool:
        return self.Code == o.Code

    def __hash__(self) -> int:
        return hash(self.Code)


class StudentReport(BaseModel):
    Usn: str
    Name: str
    Batch: Optional[int]
    Department: Optional[str]

    def __hash__(self) -> int:
        return hash(self.Usn)

    def __eq__(self, o: "StudentReport") -> bool:
        return self.Usn == o.Usn


class SubjectReport(BaseModel):
    Code: str
    Name: str
    Semester: Optional[int]
    Scheme: Optional[int]
    Department: Optional[str]

    def __hash__(self) -> int:
        return hash(self.Code)

    def __eq__(self, o: "SubjectReport") -> bool:
        return self.Code == o.Code


class ScoreReport(BaseModel):
    Usn: str
    SubjectCode: str
    Internals: int
    Externals: int

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
