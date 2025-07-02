"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
BroadTargetingCategoriesField = Literal[
    "category_description",
    "id",
    "name",
    "parent_category",
    "path",
    "size_lower_bound",
    "size_upper_bound",
    "source",
    "type",
    "type_name",
    "untranslated_name",
    "untranslated_parent_name",
]


class BroadTargetingCategoriesFields(BaseModel):
    """Pydantic model for BroadTargetingCategories fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    category_description: str = Field(None, alias="category_description")
    id: str = Field(None, alias="id")
    name: str = Field(None, alias="name")
    parent_category: str = Field(None, alias="parent_category")
    path: list[str] = Field(None, alias="path")
    size_lower_bound: int = Field(None, alias="size_lower_bound")
    size_upper_bound: int = Field(None, alias="size_upper_bound")
    source: str = Field(None, alias="source")
    type: int = Field(None, alias="type")
    type_name: str = Field(None, alias="type_name")
    untranslated_name: str = Field(None, alias="untranslated_name")
    untranslated_parent_name: str = Field(None, alias="untranslated_parent_name")
