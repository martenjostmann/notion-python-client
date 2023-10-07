import pytest

from notion_python_client.models.properties import *   # noqa: F403
from notion_python_client.models.file import File
from notion_python_client import NPC
import os
import json


class TestHandler:

    @pytest.fixture
    def client(self) -> NPC:

        return NPC(api_key="Testkey")

    @pytest.fixture
    def get_page_mock_requests(self, mocker):

        dirname = os.path.dirname(__file__)
        with open(os.path.join(dirname, 'test_data', 'test_page.json')) as f:
            response_data = json.load(f)

        mocker.patch(
            'notion_python_client.handlers.handler.Handler._make_request',
            return_value=response_data)

        return mocker

    @pytest.fixture
    def create_page_mock_requests(self, mocker):
        dirname = os.path.dirname(__file__)
        with open(os.path.join(dirname, 'test_data', 'test_create_page.json')) as f:
            response_data = json.load(f)

        mocker.patch(
            'notion_python_client.handlers.handler.Handler._make_request',
            return_value=response_data)

        return mocker

    @pytest.fixture
    def update_page_mock_requests(self, mocker):
        dirname = os.path.dirname(__file__)
        with open(os.path.join(dirname, 'test_data', 'test_update_page.json')) as f:
            response_data = json.load(f)

        mocker.patch(
            'notion_python_client.handlers.handler.Handler._make_request',
            return_value=response_data)

        return mocker

    @pytest.fixture
    def delete_page_mock_requests(self, mocker):
        dirname = os.path.dirname(__file__)
        with open(os.path.join(dirname, 'test_data', 'test_delete_page.json')) as f:
            response_data = json.load(f)

        mocker.patch(
            'notion_python_client.handlers.handler.Handler._make_request',
            return_value=response_data)

        return mocker

    @pytest.fixture
    def create_page_properties(self):
        number = Number(id="DtK%3E",  # noqa: F405
                        type="number",
                        number=1)

        select_1 = Select(id="DAjW",  # noqa: F405
                          color_="brown",
                          type="select",
                          name="Option1")

        select_2 = Select(id="DAjW",  # noqa: F405
                          color_="green",
                          type="select",
                          name="Option2")

        multi_select = MultiSelect(id="%3Ab%3Ep",  # noqa: F405
                                   type="multi_select",
                                   multi_select=[select_1, select_2])

        title = Title("My beautiful title")  # noqa: F405

        return number, multi_select, title

    def test_get_page_without_errors(self, client: NPC, get_page_mock_requests):

        page = client.page_handler.get_page("TestID")

        assert page.id == "15e4163e-93ba-40fa-bcc4-0b99b816071b"

    def test_create_page_without_cover(self,
                                       client: NPC,
                                       create_page_mock_requests,
                                       create_page_properties):

        number, multi_select, title = create_page_properties

        properties = PropertiesBase.build_properties(  # noqa: F405
            {"Number": number, "Multi-select": multi_select, "Title": title})

        client.page_handler.create_page(
            "df00e9f8-9fe5-46cb-98c4-7e332a71059f", properties)

    def test_create_page_with_cover_string(self,
                                           client: NPC,
                                           create_page_mock_requests,
                                           create_page_properties):

        number, multi_select, title = create_page_properties

        properties = PropertiesBase.build_properties(  # noqa: F405
            {"Number": number, "Multi-select": multi_select, "Title": title})

        cover_url = "www.test.de/image.png"

        client.page_handler.create_page(
            "df00e9f8-9fe5-46cb-98c4-7e332a71059f", properties, cover=cover_url)

    def test_create_page_with_cover_file(self,
                                         client: NPC,
                                         create_page_mock_requests,
                                         create_page_properties):

        number, multi_select, title = create_page_properties

        properties = PropertiesBase.build_properties(  # noqa: F405
            {"Number": number, "Multi-select": multi_select, "Title": title})

        file = File(type="external", external={
            "url": "www.test.de/image.png"})

        client.page_handler.create_page(
            "df00e9f8-9fe5-46cb-98c4-7e332a71059f", properties, cover=file)

    def test_create_page_with_cover_dict(self,
                                         client: NPC,
                                         create_page_mock_requests,
                                         create_page_properties):

        number, multi_select, title = create_page_properties

        properties = PropertiesBase.build_properties(  # noqa: F405
            {"Number": number, "Multi-select": multi_select, "Title": title})

        file = {
            "type": "external",
            "external": {
                "url": "www.test.de/image.png"
            }
        }

        client.page_handler.create_page(
            "df00e9f8-9fe5-46cb-98c4-7e332a71059f", properties, cover=file)

    def test_update_page_with_page_object(self,
                                          client: NPC,
                                          page_content,
                                          update_page_mock_requests):

        client.page_handler.update_page(page=page_content)

    def test_update_page_without_properties(self, client: NPC):

        with pytest.raises(ValueError):
            client.page_handler.update_page()

    def test_delete_page(self, client: NPC, delete_page_mock_requests):

        page_id = "15e4163e-93ba-40fa-bcc4-0b99b816071b"
        page = client.page_handler.delete_page(page_id)

        assert page.archived is True
        assert page.id == page_id
