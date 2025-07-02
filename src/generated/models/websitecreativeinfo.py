"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
WebsiteCreativeInfoField = Literal["id", "image_urls", "link_url"]


class WebsiteCreativeInfoFields(BaseModel):
    """Pydantic model for WebsiteCreativeInfo fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    id: str = Field(None, alias="id")
    image_urls: list[str] = Field(None, alias="image_urls")
    link_url: str = Field(None, alias="link_url")
