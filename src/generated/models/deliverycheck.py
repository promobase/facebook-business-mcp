"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .deliverycheckextrainfo import DeliveryCheckExtraInfoFields


# Field literal type
DeliveryCheckField = Literal["check_name", "description", "extra_info", "summary"]


class DeliveryCheckFields(BaseModel):
    """Pydantic model for DeliveryCheck fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    check_name: str = Field(None, alias="check_name")
    description: str = Field(None, alias="description")
    extra_info: DeliveryCheckExtraInfoFields = Field(None, alias="extra_info")
    summary: str = Field(None, alias="summary")
