"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
PageCTSTopicField = Literal["app_id", "frequency", "image_hash", "image_url", "subscriber", "title"]


class PageCTSTopicFields(BaseModel):
    """Pydantic model for PageCTSTopic fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    app_id: str = Field(None, alias="app_id")
    frequency: str = Field(None, alias="frequency")
    image_hash: str = Field(None, alias="image_hash")
    image_url: str = Field(None, alias="image_url")
    subscriber: int = Field(None, alias="subscriber")
    title: str = Field(None, alias="title")
