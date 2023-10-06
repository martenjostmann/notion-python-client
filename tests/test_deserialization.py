import pytest
from notion_python_client.models.page import Page


class TestDeserialization:

    @pytest.fixture
    def page_content(self):

        example_page_content = {
            "object": "page",
            "id": "15e4163e-93ba-40fa-bcc4-0b99b816071b",
            "created_time": "2023-09-23T13:24:00.000Z",
            "last_edited_time": "2023-10-05T11:14:00.000Z",
            "created_by": {
                "object": "user",
                "id": "1be0a2d9-0e4d-493f-8344-33431e514404"
            },
            "last_edited_by": {
                "object": "user",
                "id": "4db9b42a-baff-4f6a-8df3-3b64f1a45648"
            },
            "cover": None,
            "icon": None,
            "parent": {
                "type": "database_id",
                "database_id": "53da7135-2b5a-4d7e-ba78-f255f9531379"
            },
            "archived": False,
            "properties": {
                "Multi-select": {
                    "id": "%3Ab%3Ep",
                    "type": "multi_select",
                    "multi_select": [
                        {
                            "id": "84c1f7c7-7663-4c3a-b327-ab31ef7c22d8",
                            "name": "Test1",
                            "color": "purple"
                        },
                        {
                            "id": "554a5e69-09b8-4728-a317-986f3d9a6e2c",
                            "name": "Test3",
                            "color": "pink"
                        }
                    ]
                },
                "Formula": {
                    "id": "DAjW",
                    "type": "formula",
                    "formula": {
                        "type": "number",
                        "number": 2
                    }
                },
                "Number": {
                    "id": "DtK%3E",
                    "type": "number",
                    "number": 1
                },
                "Text": {
                    "id": "HHBy",
                    "type": "rich_text",
                    "rich_text": [
                        {
                            "type": "text",
                            "text": {
                                "content": "Hallo",
                                "link": None
                            },
                            "annotations": {
                                "bold": False,
                                "italic": False,
                                "strikethrough": False,
                                "underline": False,
                                "code": False,
                                "color": "default"
                            },
                            "plain_text": "Hallo",
                            "href": None
                        }
                    ]
                },
                "Todo": {
                    "id": "J%7Ba%3E",
                    "type": "relation",
                    "relation": [],
                    "has_more": False
                },
                "Checkbox": {
                    "id": "LRqP",
                    "type": "checkbox",
                    "checkbox": False
                },
                "Last edited by": {
                    "id": "MqWs",
                    "type": "last_edited_by",
                    "last_edited_by": {
                        "object": "user",
                        "id": "4db9b42a-baff-4f6a-8df3-3b64f1a45648"
                    }
                },
                "Phone": {
                    "id": "Pw%60a",
                    "type": "phone_number",
                    "phone_number": "123677"
                },
                "Person": {
                    "id": "Rucm",
                    "type": "people",
                    "people": []
                },
                "Email": {
                    "id": "Volp",
                    "type": "email",
                    "email": "test@test.de"
                },
                "Last edited time": {
                    "id": "%5BHRT",
                    "type": "last_edited_time",
                    "last_edited_time": "2023-10-05T11:14:00.000Z"
                },
                "URL": {
                    "id": "%5CHJV",
                    "type": "url",
                    "url": "www.google.de"
                },
                "Files & media": {
                    "id": "%5CXXR",
                    "type": "files",
                    "files": []
                },
                "Select": {
                    "id": "%5Ewxq",
                    "type": "select",
                    "select": {
                        "id": "d59b95cc-5c1b-45a6-b978-cf8c8ac56212",
                        "name": "Test1",
                        "color": "brown"
                    }
                },
                "Date": {
                    "id": "dqM%7B",
                    "type": "date",
                    "date": {
                        "start": "2023-10-01T21:07:00.000+00:00",
                        "end": None,
                        "time_zone": None
                    }
                },
                "Status": {
                    "id": "pvY%3C",
                    "type": "status",
                    "status": {
                        "id": "17ee6fe3-30a1-4e38-afdc-210e6274115f",
                        "name": "Not started",
                        "color": "default"
                    }
                },
                "Created by": {
                    "id": "rten",
                    "type": "created_by",
                    "created_by": {
                        "object": "user",
                        "id": "1be0a2d9-0e4d-493f-8344-33431e514404",
                        "name": "Google Calendar Sync",
                        "avatar_url": None,
                        "type": "bot",
                        "bot": {}
                    }
                },
                "ID": {
                    "id": "vLbN",
                    "type": "unique_id",
                    "unique_id": {
                        "prefix": None,
                        "number": 9
                    }
                },
                "Created time": {
                    "id": "%7CUlI",
                    "type": "created_time",
                    "created_time": "2023-09-23T13:24:00.000Z"
                },
                "Name": {
                    "id": "title",
                    "type": "title",
                    "title": [
                        {
                            "type": "text",
                            "text": {
                                "content": "Test",
                                "link": None
                            },
                            "annotations": {
                                "bold": False,
                                "italic": False,
                                "strikethrough": False,
                                "underline": False,
                                "code": False,
                                "color": "default"
                            },
                            "plain_text": "Test",
                            "href": None
                        }
                    ]
                }
            },
            "url": "https://www.notion.so/Test-15e4163e93ba40fabcc40b99b816071b",
            "public_url": None
        }

        return example_page_content

    def test_deserialization_without_errors(self, page_content):

        Page.model_validate(page_content)
