"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .business import BusinessFields


# Field literal type
BusinessImageField = Literal[
    "business",
    "creation_time",
    "hash",
    "height",
    "id",
    "media_library_url",
    "name",
    "url",
    "url_128",
    "width",
]


class BusinessImageFields(BaseModel):
    """Pydantic model for BusinessImage fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    business: BusinessFields = Field(None, alias="business")
    creation_time: datetime = Field(None, alias="creation_time")
    hash: str = Field(None, alias="hash")
    height: int = Field(None, alias="height")
    id: str = Field(None, alias="id")
    media_library_url: str = Field(None, alias="media_library_url")
    name: str = Field(None, alias="name")
    url: str = Field(None, alias="url")
    url_128: str = Field(None, alias="url_128")
    width: int = Field(None, alias="width")
