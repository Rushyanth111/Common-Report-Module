from .batchclient import BatchClient
from .deptclient import DeptClient
from .studentclient import StudentClient
from .subjectclient import SubjectClient
from .bulkclient import BulkClient


class SemesterClient:
    def __init__(self, url: str) -> None:
        self.url = url

    def batch(self, batch: int) -> BatchClient:
        return BatchClient(self.url, batch)

    def dept(self, dept: str) -> DeptClient:
        return DeptClient(self.url, dept)

    def student(self, usn: str) -> StudentClient:
        return StudentClient(self.url, usn)

    def subject(self, subcode: str) -> SubjectClient:
        return SubjectClient(self.url, subcode)

    def bulk(self):
        return BulkClient(self.url)
