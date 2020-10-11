from semester_stats_report.reciepts import ScoreReciept, StudentReciept
from semester_stats_report.reports import StudentReport

from .httpclient import BaseClient


class StudentClient(BaseClient):
    def __init__(self, url: str, usn: str) -> None:
        super().__init__(url + "/student")
        self.usn = usn

    def get(self):
        res = self._get("/{}".format(self.usn))
        rec = StudentReciept.parse_obj(res)
        return rec

    def get_scores(self):
        res = self._get("/{}/scores".format(self.usn))
        rec = [ScoreReciept.parse_obj(item) for item in res]
        return rec

    def get_backlogs(self, sem: int):
        res = self._get("/{}/backlogs".format(self.usn), params={"sem": sem})
        rec = [ScoreReciept.parse_obj(item) for item in res]
        return rec

    def get_subject(self, subcode: str):
        res = self._get("/{}/subject/{}".format(self.usn, self.subcode))
        rec = ScoreReciept.parse_obj(res)
        return rec

    def update(self, report: StudentReport):
        res = self._post("/{}".format(self.usn), body=report.dict())
        return res

    def put(self, report: StudentReport):
        res = self._post("/", body=report.dict())
        return res
