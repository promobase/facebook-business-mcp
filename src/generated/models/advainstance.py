"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .business import BusinessFields


# Field literal type
AdvAInstanceField = Literal["id", "instance_type", "name", "owner_business"]


class AdvAInstanceFields(BaseModel):
    """Pydantic model for AdvAInstance fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    id: str = Field(None, alias="id")
    instance_type: str = Field(None, alias="instance_type")
    name: str = Field(None, alias="name")
    owner_business: BusinessFields = Field(None, alias="owner_business")
