from abc import ABCMeta

import requests
from typing import Dict
from notion_python_client.client import Client
from notion_python_client.exceptions import APIException


class Handler(metaclass=ABCMeta):

    def __init__(self, client: Client, path):
        self._path = path
        self._client = client

    def _make_request(self, method: str, path: str, **kwargs) -> Dict:
        """Make a request to the Notion API based on the method, 
        path and additional arguments

        Args:
            method (str): HTTP Method to be used
            path (str): addtional path to be added to the base url 
                and the handler path. Typically the id of the object
            **kwargs: Additional arguments that should be passed to the request

        Raises:
            APIException: In case of an error from the Notion API
            requests.exceptions.RequestException: In case of a general request error

        Returns:
            Dict: The response from the Notion API
        """
        try:
            response = requests.request(method,
                                        self._client.base_url + self._path + path,
                                        headers=self._client.headers(), **kwargs)

            # Get json from response
            response_json = response.json()

            # Check for errors
            if response_json["object"] == "error":
                raise APIException(
                    status_code=response_json["status"],
                    message=response_json["message"])

            return response_json

        except requests.exceptions.RequestException as e:
            raise requests.exceptions.RequestException(e)
