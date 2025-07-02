"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
ExternalEventSourceCPASEventsDebuggingInfoField = Literal["counts", "diagnostic", "event_name"]


class ExternalEventSourceCPASEventsDebuggingInfoFields(BaseModel):
    """Pydantic model for ExternalEventSourceCPASEventsDebuggingInfo fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    counts: int = Field(None, alias="counts")
    diagnostic: str = Field(None, alias="diagnostic")
    event_name: str = Field(None, alias="event_name")
