from typing import Dict, Optional, List

from notion_python_client.handlers.handler import Handler
from notion_python_client.models.page import Page


class DatabaseHandler(Handler):
    def get_pages(self, database_id: str, filter: Optional[Dict] = None) -> List[Page]:
        """Get all pages from a database that match the filter

        Args:
            database_id (str): The id of the database
                where the pages should be retrieved from
            filter (dict, optional): The filter that should be applied.
                Defaults to None.

        Returns:
            List[Page]: The pages that match the filter
        """

        path = f"/{database_id}/query"

        # Check if filter is provided
        if filter is not None:
            body = {"filter": filter}
        else:
            body = None

        # Make the request
        database = self._make_request("POST", path, json=body)

        pages = []

        if "object" in database and database["object"] == "list":
            for page in database["results"]:
                pages.append(Page.model_validate(page))

        return pages
