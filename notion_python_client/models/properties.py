from pydantic import BaseModel, Field, validator
from typing import Optional, Literal, Dict, List, Union, no_type_check
from datetime import datetime, date
from abc import ABC, abstractmethod
import uuid
import inspect

from notion_python_client.models.user import User
from notion_python_client.models.file import File
from notion_python_client.models.rich_text import RichText


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
                           "formula", "last_edited_by", "multi_select",
                           "number", "people", "phone_number", "relation",
                           "rollup", "select", "title", "url", "status"]] = Field(default=None)


class PropertiesBase(PatchedModel, ABC):
    @abstractmethod
    def create_object(self, property_name: str) -> Dict:
        pass

    def clean_none(self, d):
        if isinstance(d, dict):
            return {k: self.clean_none(v) for k, v in d.items() if v is not None}
        else:
            return d


class Checkbox(PropertiesBase):
    checkbox: bool

    def create_object(self, property_name: str) -> Dict:
        checkbox = {
            property_name: {
                "checkbox": self.checkbox
            }
        }

        checkbox_cleaned = self.clean_none(checkbox)

        return checkbox_cleaned


class CheckboxDict(PropertiesDictBase):
    checkbox: Checkbox


class CreatedBy(PropertiesBase):
    created_by: User

    def create_object(self, property_name: str) -> Dict:
        """The created_by property cannot be updated, so it is not included in the created_by object."""

        return None


class CreatedByDict(PropertiesDictBase):
    created_by: CreatedBy


class CreatedTime(PropertiesBase):
    created_time: datetime

    def create_object(self, property_name: str) -> Dict:
        """The created_time property cannot be updated, so it is not included in the created_time object."""

        return None


class CreatedTimeDict(PropertiesDictBase):
    created_time: CreatedTime


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


class Email(PropertiesBase):
    email: str

    def create_object(self, property_name: str) -> Dict:
        email = {
            property_name: {
                "email": self.email
            }
        }

        email_cleaned = self.clean_none(email)

        return email_cleaned


class EmailDict(PropertiesDictBase):
    email: Email


class Files(PropertiesBase):
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


class FilesDict(PropertiesDictBase):
    files: Files


class Formula(PropertiesBase):
    formula: Union[bool, datetime, float, int, str]
    type: Literal["boolean", "date", "number", "string"]

    def create_object(self, property_name: str) -> Dict:
        """The formula property cannot be updated, so it is not included in the formula object."""

        return None


class FormulaDict(PropertiesDictBase):
    formula: Formula


class LastEditedBy(PropertiesBase):
    last_edited_by: User

    def create_object(self, property_name: str) -> Dict:
        """The last_edited_by property cannot be updated, so it is not included in the last_edited_by object."""

        return None


class LastEditedByDict(PropertiesDictBase):
    last_edited_by: LastEditedBy


class LastEditedTime(PropertiesBase):
    last_edited_time: datetime

    def create_object(self, property_name: str) -> Dict:
        """The last_edited_time property cannot be updated, so it is not included in the last_edited_time object."""

        return None


class LastEditedTimeDict(PropertiesDictBase):
    last_edited_time: LastEditedTime


class MultiSelect(PropertiesBase):
    color: Optional[Literal["blue", "brown", "default", "gray", "green",
                            "orange", "pink", "purple", "red", "yellow"]] = Field(default="default")
    id: uuid.UUID = Field(default=None)
    name: str = Field(default=None)

    def create_object(self, property_name: str) -> Dict:
        """Color cannot be updated, so it is not included in the multi_select object."""

        multi_select = {
            property_name: {
                "multi_select": [
                    {
                        "id": self.id,
                        "name": self.name
                    }
                ]
            }
        }

        multi_select_cleaned = self.clean_none(multi_select)

        return multi_select_cleaned


class MultiSelectDict(PropertiesDictBase):
    multi_select: MultiSelect


class Number(PropertiesBase):
    number: Union[float, int]

    def create_object(self, property_name: str) -> Dict:
        number = {
            property_name: {
                "number": self.number
            }
        }

        number_cleaned = self.clean_none(number)

        return number_cleaned


class NumberDict(PropertiesDictBase):
    number: Number


class People(PropertiesBase):
    people: List[User]

    def create_object(self, property_name: str) -> Dict:
        people = {
            property_name: {
                "people": self.people
            }
        }

        people_cleaned = self.clean_none(people)

        return people_cleaned


class PeopleDict(PropertiesDictBase):
    people: People


class PhoneNumber(PropertiesBase):
    phone_number: str

    def create_object(self, property_name: str) -> Dict:
        phone_number = {
            property_name: {
                "phone_number": self.phone_number
            }
        }

        phone_number_cleaned = self.clean_none(phone_number)

        return phone_number_cleaned


class PhoneNumberDict(PropertiesDictBase):
    phone_number: PhoneNumber


class Relation(PropertiesBase):
    has_more: bool = Field(default=False)
    relation: List[str]

    def create_object(self, property_name: str) -> Dict:

        relation = {
            property_name: {
                "relation": [{"id": r} for r in self.relation]
            }
        }

        relation_cleaned = self.clean_none(relation)

        return relation_cleaned


class RelationDict(PropertiesDictBase):
    relation: Relation


class RichTextProp(PropertiesBase):
    rich_text: List[RichText]

    def create_object(self, property_name: str) -> Dict:

        rich_text = {
            property_name: {
                "rich_text": self.rich_text
            }
        }

        rich_text_cleaned = self.clean_none(rich_text)

        return rich_text_cleaned


class RichTextPropDict(PropertiesDictBase):
    rich_text: RichTextProp


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


if __name__ == "__main__":
    print(Select(id=uuid.uuid4(), name="test", color="blue").color)
