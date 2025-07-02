"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .event import EventFields
    from .place import PlaceFields


# Field literal type
StatusField = Literal["event", "from", "id", "message", "place", "updated_time"]


class StatusFields(BaseModel):
    """Pydantic model for Status fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    event: EventFields = Field(None, alias="event")
    from_: dict[str, Any] = Field(None, alias="from")
    id: str = Field(None, alias="id")
    message: str = Field(None, alias="message")
    place: PlaceFields = Field(None, alias="place")
    updated_time: datetime = Field(None, alias="updated_time")


class StatusCreateLikeParams(BaseModel):
    """Parameters for Status.create_like()."""

    model_config = ConfigDict(extra="forbid")
    feedback_source: str | None = Field(None, description="feedback_source parameter")
    nectar_module: str | None = Field(None, description="nectar_module parameter")
    notify: bool | None = Field(None, description="notify parameter")
    tracking: str | None = Field(None, description="tracking parameter")
