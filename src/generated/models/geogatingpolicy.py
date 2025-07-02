"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
GeoGatingPolicyField = Literal[
    "after_schedule",
    "exclude_country",
    "id",
    "include_country",
    "name",
    "valid_from",
    "valid_until",
]


class GeoGatingPolicyFields(BaseModel):
    """Pydantic model for GeoGatingPolicy fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    after_schedule: str = Field(None, alias="after_schedule")
    exclude_country: list[str] = Field(None, alias="exclude_country")
    id: str = Field(None, alias="id")
    include_country: list[str] = Field(None, alias="include_country")
    name: str = Field(None, alias="name")
    valid_from: datetime = Field(None, alias="valid_from")
    valid_until: datetime = Field(None, alias="valid_until")
