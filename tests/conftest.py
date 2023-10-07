import pytest

from notion_python_client.models.properties import *  # noqa: F403
from notion_python_client.models.page import Page
from notion_python_client.models.parent import Parent
from notion_python_client.models.user import User
from notion_python_client.models.file import File

from datetime import datetime


@pytest.fixture
def page_content() -> Page:

    checkbox = Checkbox(id="d%3A%3E",  # noqa: F405
                        type="checkbox",
                        checkbox=True)

    date_with_start = DateDict(id="d%3A%3E",  # noqa: F405
                               type="date",
                               date=Date(start="2021-09-23"))  # noqa: F405

    date_with_end = DateDict(id="d%3A%3E",  # noqa: F405
                                type="date",
                                date=Date(start="2021-09-23", end="2021-09-24"))  # noqa: F405

    date_with_time = DateDict(id="d%3A%3F",  # noqa: F405
                              type="date",
                              date=Date(  # noqa: F405
                                  start="2021-09-23T13:24:00.000Z",
                                  end="2021-09-24T13:24:00.000Z"))

    email = Email(id="d%3A%3E",  # noqa: F405
                  type="email",
                  email="test@test.de")

    file_external = Files(id="d%3A%3E",  # noqa: F405
                          type="files",
                          files=[
                              File(name="Externalfile",
                                   type="external",
                                   external={"url": "https://www.google.com"})
                          ])

    file_file = Files(id="d%3A%3E",  # noqa: F405
                      type="files",
                      files=[
                          File(name="File", type="file", file={
                              "url": "https://www.google.de/myfile.pdf",
                              "expiry_time": "2023-10-06T13:19:48.446Z"
                          })
                      ]
                      )

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

    page = Page(id="15e4163e-93ba-40fa-bcc4-0b99b816071b",
                parent=Parent(
                    database_id="53da7135-2b5a-4d7e-ba78-f255f9531379"),
                created_time=datetime.now(),
                last_edited_time=datetime.now(),
                created_by=User(id="1be0a2d9-0e4d-493f-8344-33431e514404"),
                last_edited_by=User(
                    id="4db9b42a-baff-4f6a-8df3-3b64f1a45648"),
                properties={"Number": number,
                            "Multi-select": multi_select,
                            "Title": title,
                            "Checkbox": checkbox,
                            "Date with start": date_with_start,
                            "Date with end": date_with_end,
                            "Date with time": date_with_time,
                            "Email": email,
                            "File External": file_external,
                            "File File": file_file,
                            },
                url="https://www.notion.so/My-Beautiful-Page-15e4163e93ba40fabcc40b99b816071b",
                )

    return page
