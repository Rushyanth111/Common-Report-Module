from typing import Tuple
from .httpclient import BaseClient
from .reciepts import StudentScoreReciept


class BatchClient(BaseClient):
    def __init__(self, url: str, batch: int) -> None:
        """Batch Client Handles All of the Operations In Respect to a Batch.
            Do not Initialize this Class Directly, Use the SemesterClient.
        Args:
            url (str): Url Of the API
            batch (int): Integer Batch to Note.
        """
        super().__init__(url + "/batch")
        self.batch = str(batch)

    async def get_scores(self, dept: str = None, sem: int = None):
        """/scores Endpoint

        Args:
            dept (str, optional): Department Code. Defaults to None.
            sem (int, optional): Semester. Defaults to None.

        Returns:
            StudentScoreReciept: Student Report with Scores Embedded.
        """
        res = await self._get(
            "/{}/scores".format(self.batch), params={"dept": dept, "sem": sem}
        )
        rec = StudentScoreReciept.parse_obj(res)
        return rec

    async def get_detained(
        self, dept: str = None, thresh: int = None
    ) -> StudentScoreReciept:
        """/detained Enpoint

        Args:
            dept (str): Department Code.

        Returns:
            StudentScoreReciept: Student Report With Scores Embedded.
        """
        res = await self._get(
            "/{}/detained".format(self.batch), params={"dept": dept, "thresh": thresh}
        )
        rec = StudentScoreReciept.parse_obj(res)
        return rec

    async def get_backlogs(self, dept: str, sem: int = None) -> StudentScoreReciept:
        """/backlog Endpoint

        Args:
            dept (str): Department Code
            sem (int, optional): Semester,

        Returns:
            StudentScoreReciept: Student Report With Scores Embedded.
        """
        res = await self._get(
            "/{}/backlogs".format(self.batch), params={"dept": dept, "sem": sem}
        )
        rec = StudentScoreReciept.parse_obj(res)
        return rec

    async def get_aggregate(self, dept: str = None) -> Tuple[str, int]:
        """/aggregate Endpoint

        Args:
            dept (str, optional): Department Code. Defaults to None.

        Returns:
            Tuple[str, int]: Student Aggregate With [USN, int]
        """
        res = await self._get("/{}/aggregate".format(self.batch), params={"dept": dept})
        return res
