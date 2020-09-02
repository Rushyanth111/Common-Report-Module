from .httpclient import BaseClient


class DeptClient(BaseClient):
    def __init__(self, url: str, dept: str) -> None:
        super().__init__(url + "/dept")
        self.dept = dept

    def get(self):
        return self._get("/{}".format(self.dept))

    def update(self):
        pass

    def add(self):
        pass
