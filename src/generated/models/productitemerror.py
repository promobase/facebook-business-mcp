"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
ProductItemErrorField = Literal["description", "error_priority", "error_type", "title"]


class ProductItemErrorFields(BaseModel):
    """Pydantic model for ProductItemError fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    description: str = Field(None, alias="description")
    error_priority: str = Field(None, alias="error_priority")
    error_type: str = Field(None, alias="error_type")
    title: str = Field(None, alias="title")
