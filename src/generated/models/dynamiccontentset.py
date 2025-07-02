"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
DynamicContentSetField = Literal["business_id", "id", "name"]


class DynamicContentSetFields(BaseModel):
    """Pydantic model for DynamicContentSet fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    business_id: str = Field(None, alias="business_id")
    id: str = Field(None, alias="id")
    name: str = Field(None, alias="name")
