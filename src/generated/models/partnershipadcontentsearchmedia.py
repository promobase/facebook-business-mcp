"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .fbpageandinstagramaccount import FBPageAndInstagramAccountFields
    from .igmedia import IGMediaFields


# Field literal type
PartnershipAdContentSearchMediaField = Literal[
    "ig_ad_code_sponsor_count",
    "ig_ad_code_sponsors",
    "ig_media",
    "ig_media_has_product_tags",
    "is_ad_code_eligible_for_boosting_by_two_sponsors",
    "is_ad_code_entry",
]


class PartnershipAdContentSearchMediaFields(BaseModel):
    """Pydantic model for PartnershipAdContentSearchMedia fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    ig_ad_code_sponsor_count: int = Field(None, alias="ig_ad_code_sponsor_count")
    ig_ad_code_sponsors: list[FBPageAndInstagramAccountFields] = Field(
        None, alias="ig_ad_code_sponsors"
    )
    ig_media: IGMediaFields = Field(None, alias="ig_media")
    ig_media_has_product_tags: bool = Field(None, alias="ig_media_has_product_tags")
    is_ad_code_eligible_for_boosting_by_two_sponsors: bool = Field(
        None, alias="is_ad_code_eligible_for_boosting_by_two_sponsors"
    )
    is_ad_code_entry: bool = Field(None, alias="is_ad_code_entry")
