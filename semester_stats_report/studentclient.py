from semester_stats_report.reports import StudentReport

from .httpclient import BaseClient


class StudentClient(BaseClient):
    def __init__(self, url: str, usn: str) -> None:
        super().__init__(url + "/student")
        self.usn = usn

    def get(self):
        return self._get("/{}".format(self.usn))

    def get_scores(self):
        return self._get("/{}/scores".format(self.usn))

    def get_backlogs(self, sem: int):
        return self._get("/{}/backlogs".format(self.usn), params={"sem": sem})

    def get_subject(self, subcode: str):
        return self._get("/{}/subject/{}".format(self.usn, self.subcode))

    def update(self, report: StudentReport):
        return self._post("/{}".format(self.usn), body=report.dict())

    def put(self, report: StudentReport):
        return self._post("/", body=report.dict())
