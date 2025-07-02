"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
SiteLinkField = Literal["id", "link_image_hash", "link_title", "link_type", "link_url"]


class SiteLinkFields(BaseModel):
    """Pydantic model for SiteLink fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    id: str = Field(None, alias="id")
    link_image_hash: str = Field(None, alias="link_image_hash")
    link_title: str = Field(None, alias="link_title")
    link_type: str = Field(None, alias="link_type")
    link_url: str = Field(None, alias="link_url")
