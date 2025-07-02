"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
AdCreativeVideoDataMediaElementsField = Literal["element_id", "element_type"]


class AdCreativeVideoDataMediaElementsFields(BaseModel):
    """Pydantic model for AdCreativeVideoDataMediaElements fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    element_id: str = Field(None, alias="element_id")
    element_type: str = Field(None, alias="element_type")
