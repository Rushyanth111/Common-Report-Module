import requests
from typing import Any, Dict


class RestClient:
    def __init__(self, url=None, port=None) -> None:
        self.url = "https://localhost:8000" if url is not None else url

    def _get(self, params: Dict[str, str] = None) -> requests.Response:
        return requests.get(self.url, params=params)

    def _post(self, body: Any):
        return requests.post(self.url, data=body)

    def _put(self, body: Any):
        return requests.put(self.url, data=body)
