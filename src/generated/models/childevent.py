"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
ChildEventField = Literal["end_time", "id", "start_time", "ticket_uri"]


class ChildEventFields(BaseModel):
    """Pydantic model for ChildEvent fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    end_time: str = Field(None, alias="end_time")
    id: str = Field(None, alias="id")
    start_time: str = Field(None, alias="start_time")
    ticket_uri: str = Field(None, alias="ticket_uri")
