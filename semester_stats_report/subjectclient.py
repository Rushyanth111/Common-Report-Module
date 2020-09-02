from .httpclient import BaseClient


class SubjectClient(BaseClient):
    def __init__(self, url: str, subcode: str) -> None:
        super().__init__(url + "/subject")
        self.subcode = subcode

    def get(self):
        return self._get("/{}".format(self.subcode))

    def update(self):
        pass

    def add(self):
        pass
