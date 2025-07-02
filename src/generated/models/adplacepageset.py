"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .page import PageFields


# Field literal type
AdPlacePageSetField = Literal[
    "account_id", "id", "location_types", "name", "pages_count", "parent_page"
]


class AdPlacePageSetFields(BaseModel):
    """Pydantic model for AdPlacePageSet fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    account_id: str = Field(None, alias="account_id")
    id: str = Field(None, alias="id")
    location_types: list[str] = Field(None, alias="location_types")
    name: str = Field(None, alias="name")
    pages_count: int = Field(None, alias="pages_count")
    parent_page: PageFields = Field(None, alias="parent_page")
