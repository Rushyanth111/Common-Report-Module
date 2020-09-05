from semester_stats_report.reports import SubjectReport
from .httpclient import BaseClient


class SubjectClient(BaseClient):
    def __init__(self, url: str, subcode: str) -> None:
        super().__init__(url + "/subject")
        self.subcode = subcode

    def get(self):
        return self._get("/{}".format(self.subcode))

    def update(self, report: SubjectReport):
        return self._put("/{}".format(self.subcode), body=report.dict())

    def add(self, report: SubjectReport):
        return self._post("/", body=report.dict())
