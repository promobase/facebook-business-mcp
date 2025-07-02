"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
AdAccountDefaultDestinationField = Literal["destination_id", "destination_url"]


class AdAccountDefaultDestinationFields(BaseModel):
    """Pydantic model for AdAccountDefaultDestination fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    destination_id: str = Field(None, alias="destination_id")
    destination_url: str = Field(None, alias="destination_url")
