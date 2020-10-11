from semester_stats_report.reports import DepartmentReport

from .httpclient import BaseClient


class DeptClient(BaseClient):
    def __init__(self, url: str, dept: str) -> None:
        """Client WRT to /dept/ Route

        Args:
            url (str): Url of the Server
            dept (str): Department Required.
        """
        super().__init__(url + "/dept")
        self.dept = dept

    def get(self) -> DepartmentReport:
        """Get the Department

        Returns:
            DepartmentReport: Deparment Report with Details.
        """
        res = self._get("/{}".format(self.dept))
        rec = DepartmentReport.parse_obj(res)
        return rec

    def update(self, report: DepartmentReport):
        """Update a Department

        Args:
            report (DepartmentReport): Department Report
        """
        res = self._put("/{}".format(self.dept), body=report.dict())
        return res

    def add(self, report: DepartmentReport):
        """Send a Department

        Args:
            report (DepartmentReport): Department Report
        """
        res = self._post("/", body=report.dict())
        return res
