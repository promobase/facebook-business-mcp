"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
CPASParentCatalogSettingsField = Literal[
    "attribution_windows", "default_currency", "disable_use_as_parent_catalog", "id"
]


class CPASParentCatalogSettingsFields(BaseModel):
    """Pydantic model for CPASParentCatalogSettings fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    attribution_windows: list[str] = Field(None, alias="attribution_windows")
    default_currency: str = Field(None, alias="default_currency")
    disable_use_as_parent_catalog: bool = Field(None, alias="disable_use_as_parent_catalog")
    id: str = Field(None, alias="id")
