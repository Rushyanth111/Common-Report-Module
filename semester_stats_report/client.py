from .batchclient import BatchClient
from .bulkclient import BulkClient
from .deptclient import DeptClient
from .studentclient import StudentClient
from .subjectclient import SubjectClient


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
        """Obtain the Client wrt to /batch/

        Args:
            batch (int): Batch to Obtain

        Returns:
            BatchClient: BatchClient that Handles Batch Requests.
        """
        return BatchClient(self.url, batch)

    def dept(self, dept: str) -> DeptClient:
        """Obtain the Client wrt to /dept/

        Args:
            dept (str): Department Code.

        Returns:
            DeptClient: DeptClient that Handles Department Requests.
        """
        return DeptClient(self.url, dept)

    def student(self, usn: str) -> StudentClient:
        """Obtain the Client wrt to /student/

        Args:
            usn (str): Usn for Student to be Searched By.

        Returns:
            StudentClient: StudentClient that Handles Student Requests.
        """
        return StudentClient(self.url, usn)

    def subject(self, subcode: str) -> SubjectClient:
        """Obtain the Client wrt to /subject/

        Args:
            subcode (str): Subject Code that needs to be searched for.

        Returns:
            SubjectClient: SubjectClient that Handles Subject Requests.
        """
        return SubjectClient(self.url, subcode)

    def bulk(self) -> BulkClient:
        """Obtain the Client wrt to /bulk/

        Returns:
            BulkClient: BulkClient that Handles Bulk Requests.
        """
        return BulkClient(self.url)
