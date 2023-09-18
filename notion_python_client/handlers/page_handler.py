from typing import Dict
from cerberus import Validator

from notion_python_client.exceptions import PageValidationException, PropertyNotIncludedException, PropertyTypeException
from notion_python_client.validation import PAGE_SCHEMA
from notion_python_client.handlers.handler import Handler


class PageHandler(Handler):

    def get_page(self, page_id: str) -> Dict:
        """Get a page with the given id

        Args:
            page_id (str): Page id of the page that should be retrieved

        Returns:
            Dict: Retrieved page
        """

        path = f'/{page_id}'

        # Make the request
        return self._make_request("GET", path)

    def update_page(self, page_id: str, updates: Dict) -> Dict:
        """Update a specifc page with the content in the updates dict

        Args:
            page_id (str): The id of the page that should be updated
            updates (Dict): The dict containing the updates

        Returns:
            Dict: Updated page
        """

        path = f'/{page_id}'

        # Make the request
        page = self._make_request("PATCH", path, json=updates)

        return page

    def delete_page(self, page_id: str) -> Dict:
        """The deletion of a page is the equivalent of archiving it. Therefore, this method will just archive the page.

        Args:
            page_id (str): Page id of the page that should be deleted

        Returns:
            Dict: Deleted page
        """

        body = {
            "archived": True
        }

        page = self.update_page(page_id, body)

        return page

    def update_status(self, page_id: str, property_name: str, status: str) -> Dict:
        """Updates the status property of a page

        Args:
            page_id (str): Page id of the page that should be updated
            property_name (str): The name of the status property
            status (str): The status that should be set

        Returns:
            Dict: The updated page
        """

        body = {
            "properties": {
                property_name: {
                    "id": "status",
                    "type": "status",
                    "status": {
                        "name": status
                    }
                }
            }
        }

        return self.update_page(page_id, body)

    def update_title(self, page_id: str, propery_name: str, title: str) -> Dict:
        """Updates the title property of a page

        Args:
            page_id (str): Page id of the page that should be updated
            propery_name (str): The name of the title property
            title (str): The title that should be set

        Returns:
            Dict: The updated page
        """

        body = {
            "properties": {
                propery_name: {
                    "id": "title",
                    "type": "title",
                    "title": [
                        {
                            "text": {
                                "content": title
                            }
                        }
                    ]
                }
            }
        }

        return self.update_page(page_id, body)

    def set_title_to_relation(self, page: Dict, relation_property_name: str, title_property_name: str) -> Dict:
        """Sets the title of a page to the title of the relation

        Args:
            page (Dict): The page that should be updated
            relation_property_name (str): The name of the relation property
            title_property_name (str): The name of the title property. This property will be updated with the title of the relation

        Returns:
            Dict: The updated page
        """

        validator = Validator(PAGE_SCHEMA, allow_unknown=True)

        if validator.validate(page):
            properties = page['properties']

            if relation_property_name in properties:
                _property = properties[relation_property_name]

                if _property['type'] == 'relation':
                    relation = _property['relation']

                    # Check if relation is not empty
                    if len(relation) > 0:
                        relation_page = self.get_page(relation[0]['id'])

                        if title_property_name in relation_page['properties']:
                            title = relation_page['properties'][title_property_name]['title'][0]['text']['content']
                            updated_page = self.update_title(
                                page['id'], title_property_name, title)
                        else:
                            raise PropertyNotIncludedException(
                                title_property_name)

                        return updated_page

                else:
                    raise PropertyTypeException('relation', _property['type'])
            else:
                raise PropertyNotIncludedException(relation_property_name)
        else:
            raise PageValidationException(
                "The page provided is not a a Notion page")
