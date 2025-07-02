"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
AdAssetFeedAdditionalDataField = Literal[
    "automated_product_tags",
    "brand_page_id",
    "is_click_to_message",
    "multi_share_end_card",
    "page_welcome_message",
    "partner_app_welcome_message_flow_id",
]


class AdAssetFeedAdditionalDataFields(BaseModel):
    """Pydantic model for AdAssetFeedAdditionalData fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    automated_product_tags: bool = Field(None, alias="automated_product_tags")
    brand_page_id: str = Field(None, alias="brand_page_id")
    is_click_to_message: bool = Field(None, alias="is_click_to_message")
    multi_share_end_card: bool = Field(None, alias="multi_share_end_card")
    page_welcome_message: str = Field(None, alias="page_welcome_message")
    partner_app_welcome_message_flow_id: str = Field(
        None, alias="partner_app_welcome_message_flow_id"
    )
