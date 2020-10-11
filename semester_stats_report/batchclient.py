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

    def get_scores(self, dept: str = None, sem: int = None):
        res = self._get(
            "/{}/scores".format(self.batch), params={"dept": dept, "sem": sem}
        )
        rec = StudentScoreReciept.parse_obj(res)
        return rec

    def get_detained(self, dept: str):
        res = self._get("/{}/detained".format(self.batch), params={"dept": dept})
        rec = StudentScoreReciept.parse_obj(res)
        return rec

    def get_backlogs(self, dept: str, sem: int):
        res = self._get(
            "/{}/backlogs".format(self.batch), params={"dept": dept, "sem": sem}
        )
        rec = StudentScoreReciept.parse_obj(res)
        return rec

    def get_aggregate(self, dept: str):
        res = self._get("/{}/aggregate".format(self.batch), params={"dept": dept})
        return res
