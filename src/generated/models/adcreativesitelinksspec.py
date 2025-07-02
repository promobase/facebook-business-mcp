"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
AdCreativeSiteLinksSpecField = Literal[
    "is_site_link_sticky",
    "site_link_hash",
    "site_link_id",
    "site_link_image_hash",
    "site_link_image_url",
    "site_link_recommendation_type",
    "site_link_title",
    "site_link_url",
]


class AdCreativeSiteLinksSpecFields(BaseModel):
    """Pydantic model for AdCreativeSiteLinksSpec fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    is_site_link_sticky: bool = Field(None, alias="is_site_link_sticky")
    site_link_hash: str = Field(None, alias="site_link_hash")
    site_link_id: str = Field(None, alias="site_link_id")
    site_link_image_hash: str = Field(None, alias="site_link_image_hash")
    site_link_image_url: str = Field(None, alias="site_link_image_url")
    site_link_recommendation_type: str = Field(None, alias="site_link_recommendation_type")
    site_link_title: str = Field(None, alias="site_link_title")
    site_link_url: str = Field(None, alias="site_link_url")
