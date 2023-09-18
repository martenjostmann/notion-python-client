from typing import Dict, Optional

from notion_python_client.handlers.handler import Handler


class DatabaseHandler(Handler):

    def get_pages(self, database_id: str, filter: Optional[Dict] = None) -> Dict:
        """Get all pages from a database that match the filter

        Args:
            database_id (str): The id of the database where the pages should be retrieved from
            filter (dict, optional): The filter that should be applied. Defaults to None.

        Returns:
            dict: The pages that match the filter
        """

        path = f'/{database_id}/query'

        # Check if filter is provided
        if filter is not None:
            body = {
                "filter": filter
            }
        else:
            body = None

        # Make the request
        database = self._make_request("POST", path, json=body)

        pages = []

        if "object" in database and database["object"] == "list":

            pages.extend(database["results"])

        return pages
