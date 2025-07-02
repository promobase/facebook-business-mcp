"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
PartnerCategoryField = Literal[
    "approximate_count",
    "country",
    "description",
    "details",
    "id",
    "is_private",
    "name",
    "parent_category",
    "source",
    "status",
    "targeting_type",
]


class PartnerCategoryFields(BaseModel):
    """Pydantic model for PartnerCategory fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    approximate_count: int = Field(None, alias="approximate_count")
    country: str = Field(None, alias="country")
    description: str = Field(None, alias="description")
    details: str = Field(None, alias="details")
    id: str = Field(None, alias="id")
    is_private: bool = Field(None, alias="is_private")
    name: str = Field(None, alias="name")
    parent_category: str = Field(None, alias="parent_category")
    source: str = Field(None, alias="source")
    status: str = Field(None, alias="status")
    targeting_type: str = Field(None, alias="targeting_type")
