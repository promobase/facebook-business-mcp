"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
ManagementSiteLinkField = Literal[
    "ad_account_id",
    "id",
    "link_domain",
    "link_hash",
    "link_image_hash",
    "link_image_url",
    "link_title",
    "link_type",
    "link_url",
]


class ManagementSiteLinkFields(BaseModel):
    """Pydantic model for ManagementSiteLink fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    ad_account_id: str = Field(None, alias="ad_account_id")
    id: str = Field(None, alias="id")
    link_domain: str = Field(None, alias="link_domain")
    link_hash: str = Field(None, alias="link_hash")
    link_image_hash: str = Field(None, alias="link_image_hash")
    link_image_url: str = Field(None, alias="link_image_url")
    link_title: str = Field(None, alias="link_title")
    link_type: str = Field(None, alias="link_type")
    link_url: str = Field(None, alias="link_url")
