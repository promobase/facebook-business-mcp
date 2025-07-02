"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .application import ApplicationFields


# Field literal type
AppRequestField = Literal[
    "action_type", "application", "created_time", "data", "from", "id", "message", "object", "to"
]


class AppRequestFields(BaseModel):
    """Pydantic model for AppRequest fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    action_type: str = Field(None, alias="action_type")
    application: ApplicationFields = Field(None, alias="application")
    created_time: datetime = Field(None, alias="created_time")
    data: str = Field(None, alias="data")
    from_: dict[str, Any] = Field(None, alias="from")
    id: str = Field(None, alias="id")
    message: str = Field(None, alias="message")
    object: dict[str, Any] = Field(None, alias="object")
    to: dict[str, Any] = Field(None, alias="to")
