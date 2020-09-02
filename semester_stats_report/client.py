from .batchclient import BatchClient
from .deptclient import DeptClient
from .studentclient import StudentClient
from .subjectclient import SubjectClient


class SemesterClient:
    def __init__(self, url: str) -> None:
        self.url = url

    def batch(self, batch: int) -> BatchClient:
        return BatchClient(self.url, batch)

    def dept(self, dept: str) -> DeptClient:
        return DeptClient(self.url)

    def student(self, usn: str) -> StudentClient:
        return StudentClient(self.url)

    def subject(self, subcode: str) -> SubjectClient:
        return SubjectClient(self.url)
