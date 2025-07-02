"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
MessengerDestinationPageWelcomeMessageField = Literal[
    "id",
    "page_welcome_message_body",
    "page_welcome_message_type",
    "template_name",
    "time_created",
    "time_last_used",
]


class MessengerDestinationPageWelcomeMessageFields(BaseModel):
    """Pydantic model for MessengerDestinationPageWelcomeMessage fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    id: str = Field(None, alias="id")
    page_welcome_message_body: str = Field(None, alias="page_welcome_message_body")
    page_welcome_message_type: str = Field(None, alias="page_welcome_message_type")
    template_name: str = Field(None, alias="template_name")
    time_created: datetime = Field(None, alias="time_created")
    time_last_used: datetime = Field(None, alias="time_last_used")
