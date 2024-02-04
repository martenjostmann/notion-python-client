from notion_python_client.models.properties import *  # noqa: F403
import pytest
import json
import os

from typing import Dict


class TestSerialization:

    @pytest.fixture
    def page_content_properties_serialized(self) -> Dict:
        dirname = os.path.dirname(__file__)
        with open(os.path.join(dirname, 'test_data', 'test_properties.json')) as f:
            properties = json.load(f)

        return properties

    # def test_correct_serialization_of_page_properties(self,
    #                                                   page_content,
    #                                                   page_content_properties_serialized):

    #     serialized_properties = PropertiesBase.build_properties(  # noqa: F405
    #         page_content.properties)

    #     assert serialized_properties == page_content_properties_serialized
