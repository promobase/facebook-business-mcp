"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
AdAssetLinkURLField = Literal[
    "android_deeplink_url",
    "carousel_see_more_url",
    "deeplink_url",
    "display_url",
    "id",
    "ipad_deeplink_url",
    "iphone_deeplink_url",
    "url_tags",
    "website_url",
]


class AdAssetLinkURLFields(BaseModel):
    """Pydantic model for AdAssetLinkURL fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    android_deeplink_url: str = Field(None, alias="android_deeplink_url")
    carousel_see_more_url: str = Field(None, alias="carousel_see_more_url")
    deeplink_url: str = Field(None, alias="deeplink_url")
    display_url: str = Field(None, alias="display_url")
    id: str = Field(None, alias="id")
    ipad_deeplink_url: str = Field(None, alias="ipad_deeplink_url")
    iphone_deeplink_url: str = Field(None, alias="iphone_deeplink_url")
    url_tags: str = Field(None, alias="url_tags")
    website_url: str = Field(None, alias="website_url")
