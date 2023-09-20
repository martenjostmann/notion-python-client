from pydantic import BaseModel, Field, validator
from typing import Optional, Literal, Dict, List, Union, no_type_check
from datetime import datetime, date
from abc import ABC, abstractmethod
import uuid
import inspect

from notion_python_client.models.user import User
from notion_python_client.models.file import File
from notion_python_client.models.rich_text import RichText
from notion_python_client.models.page_reference import PageReference


class PatchedModel(BaseModel):
    @no_type_check
    def __setattr__(self, name, value):
        """
        To be able to use properties with setters
        """
        try:
            super().__setattr__(name, value)
        except ValueError as e:
            setters = inspect.getmembers(
                self.__class__,
                predicate=lambda x: isinstance(
                    x, property) and x.fset is not None
            )
            for setter_name, func in setters:
                if setter_name == name:
                    object.__setattr__(self, name, value)
                    break
            else:
                raise e


class PropertiesDictBase(BaseModel):
    id: Optional[str] = Field(default=None)
    type: Optional[Literal["checkbox", "created_by",
                           "created_time", "date", "email", "files",
                           "formula", "last_edited_by", "last_edited_time", "multi_select",
                           "number", "people", "phone_number", "relation", "rich_text",
                           "rollup", "select", "title", "url", "status", "unique_id", "url"]] = Field(default=None)


class PropertiesBase(PatchedModel, ABC):
    @abstractmethod
    def create_object(self, property_name: str) -> Dict:
        pass

    def clean_none(self, d):
        if isinstance(d, dict):
            return {k: self.clean_none(v) for k, v in d.items() if v is not None}
        else:
            return d


class Checkbox(PropertiesDictBase, PropertiesBase):
    checkbox: bool

    def create_object(self, property_name: str) -> Dict:
        checkbox = {
            property_name: {
                "checkbox": self.checkbox
            }
        }

        checkbox_cleaned = self.clean_none(checkbox)

        return checkbox_cleaned


class CreatedBy(PropertiesDictBase, PropertiesBase):
    created_by: User

    def create_object(self, property_name: str) -> Dict:
        """The created_by property cannot be updated, so it is not included in the created_by object."""

        return None


class CreatedTime(PropertiesDictBase, PropertiesBase):
    created_time: datetime

    def create_object(self, property_name: str) -> Dict:
        """The created_time property cannot be updated, so it is not included in the created_time object."""

        return None


class Date(PropertiesBase):
    start: Union[datetime, date]
    end: Optional[datetime] = Field(default=None)

    def create_object(self, property_name: str) -> Dict:
        date = {
            property_name: {
                "date": {
                    "start": self.start,
                    "end": self.end
                }
            }
        }

        date_cleaned = self.clean_none(date)

        return date_cleaned


class DateDict(PropertiesDictBase):
    date: Date


class Email(PropertiesDictBase, PropertiesBase):
    email: str

    def create_object(self, property_name: str) -> Dict:
        email = {
            property_name: {
                "email": self.email
            }
        }

        email_cleaned = self.clean_none(email)

        return email_cleaned


class Files(PropertiesDictBase, PropertiesBase):
    files: List[File]

    def create_object(self, property_name: str) -> Dict:
        """When updating a file page property value, the value is overwritten by the array of files passed."""

        files = {
            property_name: {
                "files": self.files
            }
        }

        files_cleaned = self.clean_none(files)

        return files_cleaned


class Formula(PropertiesBase):
    boolean: Optional[bool] = Field(default=None)
    date: Optional[datetime] = Field(default=None)
    number: Optional[Union[float, int]] = Field(default=None)
    string: Optional[str] = Field(default=None)
    type: Literal["boolean", "date", "number", "string"]

    def create_object(self, property_name: str) -> Dict:
        """The formula property cannot be updated, so it is not included in the formula object."""

        return None


class FormulaDict(PropertiesDictBase):
    formula: Formula


class LastEditedBy(PropertiesDictBase, PropertiesBase):
    last_edited_by: User

    def create_object(self, property_name: str) -> Dict:
        """The last_edited_by property cannot be updated, so it is not included in the last_edited_by object."""

        return None


class LastEditedTime(PropertiesDictBase, PropertiesBase):
    last_edited_time: datetime

    def create_object(self, property_name: str) -> Dict:
        """The last_edited_time property cannot be updated, so it is not included in the last_edited_time object."""

        return None


class Select(PropertiesBase):
    color_: Optional[Literal["blue", "brown", "default", "gray", "green",
                             "orange", "pink", "purple", "red", "yellow"]] = Field(default="default")
    id: uuid.UUID
    name: str

    @property
    def color(self):
        return self.color_

    @color.setter
    def color(self, value):
        if value not in ["blue", "brown", "gray", "green",
                         "orange", "pink", "purple", "red", "yellow"]:
            self.color_ = "default"
        else:
            self.color_ = value

    def create_object(self, property_name: str) -> Dict:
        """Color cannot be updated, so it is not included in the status object."""

        select = {
            property_name: {
                "status": {
                    "id": self.id,
                    "name": self.name,
                }
            }
        }

        select_cleaned = self.clean_none(select)

        return select_cleaned


class SelectDict(PropertiesDictBase):
    select: Select


class MultiSelectDict(PropertiesDictBase):
    multi_select: List[Select]


class Number(PropertiesDictBase, PropertiesBase):
    number: Union[float, int]

    def create_object(self, property_name: str) -> Dict:
        number = {
            property_name: {
                "number": self.number
            }
        }

        number_cleaned = self.clean_none(number)

        return number_cleaned


class People(PropertiesDictBase, PropertiesBase):
    people: List[User]

    def create_object(self, property_name: str) -> Dict:
        people = {
            property_name: {
                "people": self.people
            }
        }

        people_cleaned = self.clean_none(people)

        return people_cleaned


class PhoneNumber(PropertiesDictBase, PropertiesBase):
    phone_number: str

    def create_object(self, property_name: str) -> Dict:
        phone_number = {
            property_name: {
                "phone_number": self.phone_number
            }
        }

        phone_number_cleaned = self.clean_none(phone_number)

        return phone_number_cleaned


class Relation(PropertiesDictBase, PropertiesBase):
    has_more: bool = Field(default=False)
    relation: List[PageReference]

    def create_object(self, property_name: str) -> Dict:

        relation = {
            property_name: {
                "relation": [{"id": r} for r in self.relation]
            }
        }

        relation_cleaned = self.clean_none(relation)

        return relation_cleaned


class RichTextProp(PropertiesDictBase, PropertiesBase):
    rich_text: List[RichText]

    def create_object(self, property_name: str) -> Dict:

        rich_text = {
            property_name: {
                "rich_text": self.rich_text
            }
        }

        rich_text_cleaned = self.clean_none(rich_text)

        return rich_text_cleaned


class Status(PropertiesBase):
    color_: Optional[Literal["blue", "brown", "default", "gray", "green",
                             "orange", "pink", "purple", "red", "yellow"]] = Field(default="default")
    id: str = Field(default=None)
    name: str

    @property
    def color(self):
        return self.color_

    @color.setter
    def color(self, value):
        if value not in ["blue", "brown", "gray", "green",
                         "orange", "pink", "purple", "red", "yellow"]:
            self.color_ = "default"
        else:
            self.color_ = value

    def create_object(self, property_name: str) -> Dict:
        """Color cannot be updated, so it is not included in the status object."""

        status = {
            property_name: {
                "status": {
                    "id": self.id,
                    "name": self.name,
                }
            }
        }

        status_cleaned = self.clean_none(status)

        return status_cleaned


class StatusDict(PropertiesDictBase):
    status: Status


class Title(PropertiesDictBase, PropertiesBase):
    title: List[RichText]

    def create_object(self, property_name: str) -> Dict:
        title = {
            property_name: {
                "title": self.title
            }
        }

        title_cleaned = self.clean_none(title)

        return title_cleaned


class URL(PropertiesDictBase, PropertiesBase):
    url: str

    def create_object(self, property_name: str) -> Dict:
        url = {
            property_name: {
                "url": self.url
            }
        }

        url_cleaned = self.clean_none(url)

        return url_cleaned


class UniqueId(PropertiesBase):
    number: Union[float, int]
    prefix: Optional[str] = Field(default=None)

    def create_object(self, property_name: str) -> Dict:
        unique_id = {
            property_name: {
                "unique_id": {
                    "number": self.number,
                    "prefix": self.prefix
                }
            }
        }

        unique_id_cleaned = self.clean_none(unique_id)

        return unique_id_cleaned


class UniqueIdDict(PropertiesDictBase):
    unique_id: UniqueId
