"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .adassetfeedspecassetlabel import AdAssetFeedSpecAssetLabelFields


# Field literal type
AdAssetFeedSpecLinkURLField = Literal[
    "adlabels",
    "carousel_see_more_url",
    "deeplink_url",
    "display_url",
    "object_store_urls",
    "url_tags",
    "website_url",
]


class AdAssetFeedSpecLinkURLFields(BaseModel):
    """Pydantic model for AdAssetFeedSpecLinkURL fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    adlabels: list[AdAssetFeedSpecAssetLabelFields] = Field(None, alias="adlabels")
    carousel_see_more_url: str = Field(None, alias="carousel_see_more_url")
    deeplink_url: str = Field(None, alias="deeplink_url")
    display_url: str = Field(None, alias="display_url")
    object_store_urls: list[str] = Field(None, alias="object_store_urls")
    url_tags: str = Field(None, alias="url_tags")
    website_url: str = Field(None, alias="website_url")
