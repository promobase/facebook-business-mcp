"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
PlaceTopicField = Literal[
    "count",
    "has_children",
    "icon_url",
    "id",
    "name",
    "parent_ids",
    "plural_name",
    "top_subtopic_names",
]


class PlaceTopicFields(BaseModel):
    """Pydantic model for PlaceTopic fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    count: int = Field(None, alias="count")
    has_children: bool = Field(None, alias="has_children")
    icon_url: str = Field(None, alias="icon_url")
    id: str = Field(None, alias="id")
    name: str = Field(None, alias="name")
    parent_ids: list[str] = Field(None, alias="parent_ids")
    plural_name: str = Field(None, alias="plural_name")
    top_subtopic_names: list[str] = Field(None, alias="top_subtopic_names")
