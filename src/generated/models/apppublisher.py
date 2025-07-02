"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
AppPublisherField = Literal[
    "content_id", "icon_url", "id", "name", "platform", "store_name", "store_url"
]


class AppPublisherFields(BaseModel):
    """Pydantic model for AppPublisher fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    content_id: str = Field(None, alias="content_id")
    icon_url: str = Field(None, alias="icon_url")
    id: str = Field(None, alias="id")
    name: str = Field(None, alias="name")
    platform: str = Field(None, alias="platform")
    store_name: str = Field(None, alias="store_name")
    store_url: str = Field(None, alias="store_url")
