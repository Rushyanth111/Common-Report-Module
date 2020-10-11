from typing import List

from semester_stats_report.reports import (
    DepartmentReport,
    ScoreReport,
    StudentReport,
    SubjectReport,
)

from .httpclient import BaseClient


class BulkClient(BaseClient):
    def __init__(self, url: str) -> None:
        super().__init__(url + "/bulk")

    def scores(self, reports: List[ScoreReport]):
        return self._post("/score", body=[x.dict() for x in reports])

    def dept(self, reports: List[DepartmentReport]):
        return self._post("/dept", body=[x.dict() for x in reports])

    def subject(self, reports: List[SubjectReport]):
        return self._post("/subject", body=[x.dict() for x in reports])

    def student(self, reports: List[StudentReport]):
        return self._post("/student", body=[x.dict() for x in reports])
