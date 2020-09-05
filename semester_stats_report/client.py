from .batchclient import BatchClient
from .deptclient import DeptClient
from .studentclient import StudentClient
from .subjectclient import SubjectClient
from .bulkclient import BulkClient


class SemesterClient:
    """The Base Client for All API Manipulation."""

    def __init__(self, url: str) -> None:
        """Obtain the API Client that Can Interact
            with the Server at the given URL.

        Args:
            url (str): The url of the server
        """
        self.url = url

    def batch(self, batch: int) -> BatchClient:
        """Obtain the Client wrt to /Batch/

        Args:
            batch (int): Integer Batch to Obtain

        Returns:
            BatchClient: A Client that Handles Batch Operations
        """
        return BatchClient(self.url, batch)

    def dept(self, dept: str) -> DeptClient:
        """[summary]

        Args:
            dept (str): [description]

        Returns:
            DeptClient: [description]
        """
        return DeptClient(self.url, dept)

    def student(self, usn: str) -> StudentClient:
        """[summary]

        Args:
            usn (str): [description]

        Returns:
            StudentClient: [description]
        """
        return StudentClient(self.url, usn)

    def subject(self, subcode: str) -> SubjectClient:
        """[summary]

        Args:
            subcode (str): [description]

        Returns:
            SubjectClient: [description]
        """
        return SubjectClient(self.url, subcode)

    def bulk(self):
        return BulkClient(self.url)
