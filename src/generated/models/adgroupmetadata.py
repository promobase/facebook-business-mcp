"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
AdgroupMetadataField = Literal[
    "ad_standard_enhancements_edit_source",
    "adgroup_creation_source",
    "adgroup_edit_source",
    "carousel_style",
    "carousel_with_static_card_style",
]


class AdgroupMetadataFields(BaseModel):
    """Pydantic model for AdgroupMetadata fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    ad_standard_enhancements_edit_source: int = Field(
        None, alias="ad_standard_enhancements_edit_source"
    )
    adgroup_creation_source: str = Field(None, alias="adgroup_creation_source")
    adgroup_edit_source: str = Field(None, alias="adgroup_edit_source")
    carousel_style: str = Field(None, alias="carousel_style")
    carousel_with_static_card_style: str = Field(None, alias="carousel_with_static_card_style")
