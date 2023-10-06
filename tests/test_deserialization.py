import pytest
from notion_python_client.models.page import Page
import json
import os


class TestDeserialization:

    @pytest.fixture
    def page_content(self):

        dirname = os.path.dirname(__file__)
        with open(os.path.join(dirname, 'test_data', 'test_page.json')) as f:
            example_page_content = json.load(f)

        return example_page_content

    def test_deserialization_without_errors(self, page_content):

        Page.model_validate(page_content)
