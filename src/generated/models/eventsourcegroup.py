"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .business import BusinessFields
    from .externaleventsource import ExternalEventSourceFields


# Field literal type
EventSourceGroupField = Literal["business", "event_sources", "id", "name", "owner_business"]


class EventSourceGroupFields(BaseModel):
    """Pydantic model for EventSourceGroup fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    business: BusinessFields = Field(None, alias="business")
    event_sources: list[ExternalEventSourceFields] = Field(None, alias="event_sources")
    id: str = Field(None, alias="id")
    name: str = Field(None, alias="name")
    owner_business: BusinessFields = Field(None, alias="owner_business")


class EventSourceGroupCreateSharedAccountParams(BaseModel):
    """Parameters for EventSourceGroup.create_shared_account()."""

    model_config = ConfigDict(extra="forbid")
    accounts: list[str] | None = Field(None, description="accounts parameter")
