from semester_stats_report.reciepts import SubjectReciept
from semester_stats_report.reports import SubjectReport

from .httpclient import BaseClient


class SubjectClient(BaseClient):
    def __init__(self, url: str, subcode: str) -> None:
        """Client WRT to the /Subject/ Endpoint

        Args:
            url (str): Url of the Server
            subcode (str): Subject Code
        """
        super().__init__(url + "/subject")
        self.subcode = subcode

    async def get(self) -> SubjectReciept:
        """Client that gets the Subject

        Returns:
            SubjectReciept : Subject Reciept
        """
        res = await self._get("/{}".format(self.subcode))
        rec = SubjectReciept.parse_obj(res)
        return rec

    async def update(self, report: SubjectReport):
        """Update a Student

        Args:
            report (SubjectReport): Student Report
        """
        res = await self._put("/{}".format(self.subcode), body=report.dict())
        return res

    async def add(self, report: SubjectReport):
        """Insert a Student

        Args:
            report (SubjectReport): Student Report
        """
        res = await self._post("/", body=report.dict())
        return res
