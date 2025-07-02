"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .adcreativelinkdatacalltoaction import AdCreativeLinkDataCallToActionFields


# Field literal type
AdCreativeStaticFallbackSpecField = Literal[
    "call_to_action", "description", "image_hash", "link", "message", "name"
]


class AdCreativeStaticFallbackSpecFields(BaseModel):
    """Pydantic model for AdCreativeStaticFallbackSpec fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    call_to_action: AdCreativeLinkDataCallToActionFields = Field(None, alias="call_to_action")
    description: str = Field(None, alias="description")
    image_hash: str = Field(None, alias="image_hash")
    link: str = Field(None, alias="link")
    message: str = Field(None, alias="message")
    name: str = Field(None, alias="name")
