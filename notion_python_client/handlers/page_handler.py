from typing import Dict, Optional, Union
from cerberus import Validator

from notion_python_client.exceptions import PropertyNotIncludedException, PropertyTypeException, RelationOutOfRangeException
from notion_python_client.validation import PAGE_SCHEMA
from notion_python_client.handlers.handler import Handler

from notion_python_client.models.page import Page
from notion_python_client.models.properties import Status, Title, PropertiesBase
from notion_python_client.models.rich_text import RichText
from notion_python_client.models.text import Text
from notion_python_client.models.file import File
from notion_python_client.models.parent import Parent


class PageHandler(Handler):

    def get_page(self, page_id: str) -> Page:
        """Get a page with the given id

        Args:
            page_id (str): Page id of the page that should be retrieved

        Returns:
            Page: Retrieved page
        """

        path = f'/{page_id}'

        # Make the request
        resp = self._make_request("GET", path)

        return Page.model_validate(resp)

    def create_page(self, parent_id: str, properties: Dict, cover: Optional[Union[File, Dict, str]] = None) -> Page:
        """Create a new page with the given properties

        Args:
            parent_id (str): The id of the parent page
            properties (Dict): The properties of the new page
            cover (Optional[Union[File, Dict, str]]): 
                The cover of the page. Can be a File object, a dict or a string. If a string is provided, 
                it will be interpreted as a url. If a dict is provided, it will be interpreted as a File object. Defaults to None.

        Returns:
            Page: The created page
        """

        path = f''

        if "properties" in properties:
            properties = properties["properties"]

        # Create the body
        body = {
            "properties": properties
        }

        # Insert parent information
        body.update(Parent(database_id=parent_id).create_object())

        # Check if cover is provided
        if cover is not None:

            # Create cover object if necessary
            if isinstance(cover, dict):
                cover = File.model_validate(cover)

            elif isinstance(cover, str):
                cover = File(type="external", external={
                             "url": cover}).create_object()

            properties.update(cover.create_object(property_name="cover"))

        # Make the request
        resp = self._make_request("POST", path, json=body)

        return Page.model_validate(resp)

    def update_page(self, page_id: str, updates: Dict) -> Page:
        """Update a specifc page with the content in the updates dict

        Args:
            page_id (str): The id of the page that should be updated
            updates (Dict): The dict containing the updates

        Returns:
            Page: Updated page
        """

        path = f'/{page_id}'

        # Make the request
        resp = self._make_request("PATCH", path, json=updates)

        return Page.model_validate(resp)

    def delete_page(self, page_id: str) -> Page:
        """The deletion of a page is the equivalent of archiving it. Therefore, this method will just archive the page.

        Args:
            page_id (str): Page id of the page that should be deleted

        Returns:
            Dict: Deleted page
        """

        body = {
            "archived": True
        }

        resp = self.update_page(page_id, body)

        return Page.model_validate(resp)

    def update_status(self, page_id: str, property_name: str, status: str) -> Page:
        """Updates the status property of a page

        Args:
            page_id (str): Page id of the page that should be updated
            property_name (str): The name of the status property
            status (str): The status that should be set

        Returns:
            Dict: The updated page
        """

        status_object = Status(id="status", name=status).create_object(
            property_name=property_name)

        body = PropertiesBase.build_properties(properties=[status_object])

        resp = self.update_page(page_id, body)

        return Page.model_validate(resp)

    def update_title(self, page_id: str, property_name: str, title: str) -> Page:
        """Updates the title property of a page

        Args:
            page_id (str): Page id of the page that should be updated
            property_name (str): The name of the title property
            title (str): The title that should be set

        Returns:
            Dict: The updated page
        """

        body = PropertiesBase.build_properties([Title(title=title).create_object(
            property_name=property_name)])

        resp = self.update_page(page_id, body)
        return Page.model_validate(resp)

    def set_title_to_relation(self, page: Page, relation_property_name: str, title_property_name: str, relation_idx: int = 0) -> Page:
        """Sets the title of a page to the title of the relation

        Args:
            page (Page): The page that should be updated
            relation_property_name (str): The name of the relation property
            title_property_name (str): The name of the title property. This property will be updated with the title of the relation
            relation_idx (int, optional): The index of the relation that should be used. Can be used when multiple relations are available. Defaults to 0.

        Returns:
            Dict: The updated page
        """

        properties = page.properties

        if relation_property_name in properties:
            _property = properties[relation_property_name]

            if _property.type == 'relation':
                relation = _property.relation

                # Check if relation is not empty
                if len(relation) > 0:
                    if len(relation) > relation_idx:
                        relation_page = self.get_page(
                            relation[relation_idx].id)

                        if title_property_name in relation_page.properties:
                            title = relation_page.properties[title_property_name].title[0].text.content
                            resp = self.update_title(
                                page.id, title_property_name, title)
                        else:
                            raise PropertyNotIncludedException(
                                title_property_name)

                        return Page.model_validate(resp)
                    else:
                        raise RelationOutOfRangeException(
                            relation_idx, len(relation))

            else:
                raise PropertyTypeException('relation', _property['type'])
        else:
            raise PropertyNotIncludedException(relation_property_name)
