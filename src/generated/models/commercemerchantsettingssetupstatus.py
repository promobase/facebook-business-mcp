"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
CommerceMerchantSettingsSetupStatusField = Literal[
    "deals_setup",
    "marketplace_approval_status",
    "marketplace_approval_status_details",
    "payment_setup",
    "review_status",
    "shop_setup",
]


class CommerceMerchantSettingsSetupStatusFields(BaseModel):
    """Pydantic model for CommerceMerchantSettingsSetupStatus fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    deals_setup: str = Field(None, alias="deals_setup")
    marketplace_approval_status: str = Field(None, alias="marketplace_approval_status")
    marketplace_approval_status_details: dict[str, Any] = Field(
        None, alias="marketplace_approval_status_details"
    )
    payment_setup: str = Field(None, alias="payment_setup")
    review_status: dict[str, Any] = Field(None, alias="review_status")
    shop_setup: str = Field(None, alias="shop_setup")
