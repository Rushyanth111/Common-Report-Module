from .httpclient import BaseClient


class StudentClient(BaseClient):
    def __init__(self, url: str, usn: str) -> None:
        super().__init__(url + "/student")
        self.usn = usn

    def get(self):
        return self._get("/{}".format(self.usn))

    def update(self):
        pass

    def get_scores(self):
        return self._get("/{}/scores".format(self.usn))

    def get_semester(self, sem: int):
        return self._get("/{}/semester".format(self.usn), params={"sem": sem})

    def get_backlogs(self, sem: int):
        return self._get("/{}/backlogs".format(self.usn), params={"sem": sem})

    def get_subject(self, subcode: str):
        return self._get("/{}/subject/{}".format(self.usn, self.subcode))
