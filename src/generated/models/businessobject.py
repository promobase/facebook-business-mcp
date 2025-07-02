"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
BusinessObjectField = Literal["asset", "asset_type", "id", "name", "picture"]


class BusinessObjectFields(BaseModel):
    """Pydantic model for BusinessObject fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    asset: dict[str, Any] = Field(None, alias="asset")
    asset_type: str = Field(None, alias="asset_type")
    id: str = Field(None, alias="id")
    name: str = Field(None, alias="name")
    picture: str = Field(None, alias="picture")
