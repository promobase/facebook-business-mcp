"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
AdCreativePhotoDataField = Literal[
    "branded_content_shared_to_sponsor_status",
    "branded_content_sponsor_page_id",
    "caption",
    "image_hash",
    "page_welcome_message",
    "url",
]


class AdCreativePhotoDataFields(BaseModel):
    """Pydantic model for AdCreativePhotoData fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    branded_content_shared_to_sponsor_status: str = Field(
        None, alias="branded_content_shared_to_sponsor_status"
    )
    branded_content_sponsor_page_id: str = Field(None, alias="branded_content_sponsor_page_id")
    caption: str = Field(None, alias="caption")
    image_hash: str = Field(None, alias="image_hash")
    page_welcome_message: str = Field(None, alias="page_welcome_message")
    url: str = Field(None, alias="url")
