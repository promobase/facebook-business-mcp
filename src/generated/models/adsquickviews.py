"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .profile import ProfileFields


# Field literal type
AdsQuickViewsField = Literal[
    "attribution_windows",
    "breakdowns",
    "column_fields",
    "description",
    "id",
    "name",
    "owner",
    "permission",
    "quick_view_type",
    "sort",
]


class AdsQuickViewsFields(BaseModel):
    """Pydantic model for AdsQuickViews fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    attribution_windows: list[str] = Field(None, alias="attribution_windows")
    breakdowns: list[str] = Field(None, alias="breakdowns")
    column_fields: list[str] = Field(None, alias="column_fields")
    description: str = Field(None, alias="description")
    id: str = Field(None, alias="id")
    name: str = Field(None, alias="name")
    owner: ProfileFields = Field(None, alias="owner")
    permission: str = Field(None, alias="permission")
    quick_view_type: str = Field(None, alias="quick_view_type")
    sort: list[dict[str, Any]] = Field(None, alias="sort")
