from .httpclient import BaseClient


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

    def get(self, dept: str = None):
        """Obtain the Batch Students

        Args:
            dept (str, optional): Department String. Defaults to None.

        Returns:
            Dict: The Result of the Operation
        """
        params = None if dept is None else {"dept": dept}
        return self._get("/{}".format(self.batch), params=params)

    def get_scores(self, dept: str = None, sem: int = None):
        return self._get(
            "/{}/scores".format(self.batch), params={"dept": dept, "sem": sem}
        )

    def get_usns(self, dept: str):
        return self._get("/{}/usns".format(self.batch), params={"dept": dept})

    def get_scheme(self):
        return self._get("/{}/scheme".format(self.batch))

    def get_detained(self, dept: str):
        return self._get("/{}/detained".format(self.batch), params={"dept": dept})

    def get_backlogs(self, dept: str, sem: int):
        return self._get(
            "/{}/backlogs".format(self.batch), params={"dept": dept, "sem": sem}
        )

    def get_aggregate(self, dept: str):
        return self._get("/{}/aggregate".format(self.batch), params={"dept": dept})
