"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .user import UserFields


# Field literal type
VideoCopyrightMatchField = Literal[
    "created_date",
    "id",
    "last_modified_user",
    "match_data",
    "match_status",
    "notes",
    "permalink",
    "ugc_content_format",
]


class VideoCopyrightMatchFields(BaseModel):
    """Pydantic model for VideoCopyrightMatch fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    created_date: datetime = Field(None, alias="created_date")
    id: str = Field(None, alias="id")
    last_modified_user: UserFields = Field(None, alias="last_modified_user")
    match_data: list[dict[str, Any]] = Field(None, alias="match_data")
    match_status: str = Field(None, alias="match_status")
    notes: str = Field(None, alias="notes")
    permalink: str = Field(None, alias="permalink")
    ugc_content_format: str = Field(None, alias="ugc_content_format")
