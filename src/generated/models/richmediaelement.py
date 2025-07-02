"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
RichMediaElementField = Literal["element", "element_type", "name"]


class RichMediaElementFields(BaseModel):
    """Pydantic model for RichMediaElement fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    element: dict[str, Any] = Field(None, alias="element")
    element_type: str = Field(None, alias="element_type")
    name: str = Field(None, alias="name")
