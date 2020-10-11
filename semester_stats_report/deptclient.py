from semester_stats_report.reports import DepartmentReport

from .httpclient import BaseClient


class DeptClient(BaseClient):
    def __init__(self, url: str, dept: str) -> None:
        super().__init__(url + "/dept")
        self.dept = dept

    def get(self):
        return self._get("/{}".format(self.dept))

    def update(self, report: DepartmentReport):
        return self._put("/{}".format(self.dept), body=report.dict())

    def add(self, report: DepartmentReport):
        return self._post("/", body=report.dict())
