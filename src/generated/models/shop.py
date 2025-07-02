"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .commercemerchantsettings import CommerceMerchantSettingsFields


# Field literal type
ShopField = Literal[
    "commerce_merchant_settings",
    "fb_sales_channel",
    "id",
    "ig_sales_channel",
    "is_onsite_enabled",
    "shop_status",
    "workspace",
]


class ShopFields(BaseModel):
    """Pydantic model for Shop fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    commerce_merchant_settings: CommerceMerchantSettingsFields = Field(
        None, alias="commerce_merchant_settings"
    )
    fb_sales_channel: dict[str, Any] = Field(None, alias="fb_sales_channel")
    id: str = Field(None, alias="id")
    ig_sales_channel: dict[str, Any] = Field(None, alias="ig_sales_channel")
    is_onsite_enabled: bool = Field(None, alias="is_onsite_enabled")
    shop_status: str = Field(None, alias="shop_status")
    workspace: dict[str, Any] = Field(None, alias="workspace")
