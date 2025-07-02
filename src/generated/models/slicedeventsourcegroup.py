"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .eventsourcegroup import EventSourceGroupFields


# Field literal type
SlicedEventSourceGroupField = Literal["event_source_group", "filter", "id", "name"]


class SlicedEventSourceGroupFields(BaseModel):
    """Pydantic model for SlicedEventSourceGroup fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    event_source_group: EventSourceGroupFields = Field(None, alias="event_source_group")
    filter: str = Field(None, alias="filter")
    id: str = Field(None, alias="id")
    name: str = Field(None, alias="name")
