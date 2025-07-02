"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
PagePublisherField = Literal["global_parent_id", "icon", "id", "name", "url"]


class PagePublisherFields(BaseModel):
    """Pydantic model for PagePublisher fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    global_parent_id: str = Field(None, alias="global_parent_id")
    icon: str = Field(None, alias="icon")
    id: str = Field(None, alias="id")
    name: str = Field(None, alias="name")
    url: str = Field(None, alias="url")
