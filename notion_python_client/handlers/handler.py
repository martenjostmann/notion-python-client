from abc import ABCMeta

import requests
from notion_python_client.client import Client
from notion_python_client.exceptions import APIException


class Handler(metaclass=ABCMeta):

    def __init__(self, client: Client, path):
        self._path = path
        self._client = client

    def _make_request(self, method: str, path: str, **kwargs) -> dict:
        try:
            response = requests.request(method, self._client.base_url + self._path + path,
                                        headers=self._client.headers(), **kwargs)

            # Get json from response
            response_json = response.json()

            # Check for errors
            if response_json["object"] == "error":
                raise APIException(
                    status_code=response_json["status"], message=response_json["message"])

            return response_json

        except requests.exceptions.RequestException as e:
            raise requests.exceptions.RequestException(e)
