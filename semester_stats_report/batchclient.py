from .httpclient import BaseClient


class BatchClient(BaseClient):
    def __init__(self, url: str, batch: int) -> None:
        super().__init__(url + "/batch")
        self.batch = str(batch)

    def get(self, dept: str):
        return self._get("/{}".format(self.batch), params={"dept": dept})

    def get_scores(self, dept: str, sem: int):
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
