"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .adcreativepromotionmetadataspec import AdCreativePromotionMetadataSpecFields
    from .adcreativesitelinksspec import AdCreativeSiteLinksSpecFields


# Field literal type
AdCreativeSourcingSpecField = Literal[
    "associated_product_set_id",
    "brand",
    "dynamic_site_links_spec",
    "enable_social_feedback_preservation",
    "promotion_metadata_spec",
    "site_links_spec",
    "source_url",
]


class AdCreativeSourcingSpecFields(BaseModel):
    """Pydantic model for AdCreativeSourcingSpec fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    associated_product_set_id: str = Field(None, alias="associated_product_set_id")
    brand: dict[str, Any] = Field(None, alias="brand")
    dynamic_site_links_spec: dict[str, Any] = Field(None, alias="dynamic_site_links_spec")
    enable_social_feedback_preservation: bool = Field(
        None, alias="enable_social_feedback_preservation"
    )
    promotion_metadata_spec: list[AdCreativePromotionMetadataSpecFields] = Field(
        None, alias="promotion_metadata_spec"
    )
    site_links_spec: list[AdCreativeSiteLinksSpecFields] = Field(None, alias="site_links_spec")
    source_url: str = Field(None, alias="source_url")
