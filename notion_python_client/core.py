from notion_python_client.client import Client
from notion_python_client.handlers import DatabaseHandler, PageHandler
from notion_python_client.constants import API_BASE_URL, API_VERSION


class NPC:

    def __init__(self, api_key):
        self._client = Client(
            base_url=f"{API_BASE_URL}/{API_VERSION}",
            api_key=api_key
        )

        self.database_handler = DatabaseHandler(self._client, "/databases")
        self.page_handler = PageHandler(self._client, "/pages")
