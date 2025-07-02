"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
CreativeAssetTagField = Literal["name"]


class CreativeAssetTagFields(BaseModel):
    """Pydantic model for CreativeAssetTag fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    name: str = Field(None, alias="name")
