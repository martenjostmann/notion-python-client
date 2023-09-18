from notion_python_client.handlers.handler import Handler


class DatabaseHandler(Handler):

    def get_pages(self, database_id: str, filter: dict = None) -> dict:

        path = f'/{database_id}/query'

        if filter is not None:
            body = {
                "filter": filter
            }
        else:
            body = None

        database = self._make_request("POST", path, json=body)

        pages = []

        if "object" in database and database["object"] == "list":

            pages.extend(database["results"])

        return pages
