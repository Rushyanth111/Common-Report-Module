from semester_stats_report.reciepts import SubjectReciept
from semester_stats_report.reports import SubjectReport

from .httpclient import BaseClient


class SubjectClient(BaseClient):
    def __init__(self, url: str, subcode: str) -> None:
        super().__init__(url + "/subject")
        self.subcode = subcode

    def get(self):
        res = self._get("/{}".format(self.subcode))
        rec = SubjectReciept.parse_obj(res)
        return rec

    def update(self, report: SubjectReport):
        res = self._put("/{}".format(self.subcode), body=report.dict())
        return res

    def add(self, report: SubjectReport):
        res = self._post("/", body=report.dict())
        return res
