from typing import Any, Dict

import requests
from pydantic import ValidationError

# All of the responses recieved are JSON. Work With them.


class BaseClient:
    def __init__(self, url: str) -> None:
        # Remove the Traling Slash from the Link if there is.
        self.url = url.strip("/")

    def _get(self, ep: str, params: Dict[str, str] = None):
        url = self.url + ep
        res = requests.get(url, params=params)
        data = res.json()
        if res.status_code == 422:
            raise ValidationError(**data)
        else:
            return data

    def _post(self, ep: str, body: Any):
        url = self.url + ep
        res = requests.get(url, body=body)
        data = res.json()
        if res.status_code == 422:
            raise ValidationError(**data)
        else:
            return data

    def _put(self, ep: str, body: Any):
        url = self.url + ep
        res = requests.get(url, body=body)
        data = res.json()
        if res.status_code == 422:
            raise ValidationError(**data)
        else:
            return data
