from semester_stats_report.reciepts import ScoreReciept, StudentReciept
from semester_stats_report.reports import StudentReport
from typing import List
from .httpclient import BaseClient


class StudentClient(BaseClient):
    def __init__(self, url: str, usn: str) -> None:
        """Client WRT to /student/ Route

        Args:
            url (str): Url for the Server
            usn (str): Usn of the Student
        """
        super().__init__(url + "/student")
        self.usn = usn

    async def get(self):
        """Get the Student

        Returns:
            StudentReciept: Reciept of a Student.
        """
        res = await self._get("/{}".format(self.usn))
        rec = StudentReciept.parse_obj(res)
        return rec

    async def get_scores(self) -> List[ScoreReciept]:
        """Get Scores of the Student

        Returns:
            List[ScoreReciept]: List of Score Reciepts
        """
        res = await self._get("/{}/scores".format(self.usn))
        rec = [ScoreReciept.parse_obj(item) for item in res]
        return rec

    async def get_backlogs(self, sem: int = None) -> List[ScoreReciept]:
        """Get Backlogs of the Student

        Args:
            sem (int, optional): Semester in Particular

        Returns:
            List[ScoreReciept]: List of Score Reciepts.
        """
        res = await self._get("/{}/backlogs".format(self.usn), params={"sem": sem})
        rec = [ScoreReciept.parse_obj(item) for item in res]
        return rec

    async def get_subject(self, subcode: str) -> ScoreReciept:
        """Get the Score of a Subject

        Args:
            subcode (str): Subcode of the Subject.

        Returns:
            ScoreReciept: Score Reciept.
        """
        res = await self._get("/{}/subject/{}".format(self.usn, subcode))
        rec = ScoreReciept.parse_obj(res)
        return rec

    async def update(self, report: StudentReport):
        """Update a Particular Student

        Args:
            report (StudentReport): Student Report to Update
        """
        res = await self._post("/{}".format(self.usn), body=report.dict())
        return res

    async def put(self, report: StudentReport):
        """Insert a Particular Student

        Args:
            report (StudentReport): Student Report to Insert
        """
        res = await self._post("/", body=report.dict())
        return res
