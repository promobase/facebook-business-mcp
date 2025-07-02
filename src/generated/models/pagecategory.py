"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
PageCategoryField = Literal["api_enum", "fb_page_categories", "id", "name"]


class PageCategoryFields(BaseModel):
    """Pydantic model for PageCategory fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    api_enum: str = Field(None, alias="api_enum")
    fb_page_categories: list[PageCategoryFields] = Field(None, alias="fb_page_categories")
    id: str = Field(None, alias="id")
    name: str = Field(None, alias="name")
