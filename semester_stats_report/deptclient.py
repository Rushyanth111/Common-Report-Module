from semester_stats_report.reports import DepartmentReport

from .httpclient import BaseClient


class DeptClient(BaseClient):
    def __init__(self, url: str, dept: str) -> None:
        super().__init__(url + "/dept")
        self.dept = dept

    def get(self):
        res = self._get("/{}".format(self.dept))
        rec = DepartmentReport.parse_obj(res)
        return rec

    def update(self, report: DepartmentReport):
        res = self._put("/{}".format(self.dept), body=report.dict())
        return res

    def add(self, report: DepartmentReport):
        res = self._post("/", body=report.dict())
        return res
