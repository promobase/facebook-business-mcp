"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
DeliveryStatusField = Literal["status", "substatuses"]


class DeliveryStatusFields(BaseModel):
    """Pydantic model for DeliveryStatus fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    status: str = Field(None, alias="status")
    substatuses: list[str] = Field(None, alias="substatuses")
