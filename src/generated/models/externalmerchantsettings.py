"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
ExternalMerchantSettingsField = Literal["connect_woo", "external_platform", "id"]


class ExternalMerchantSettingsFields(BaseModel):
    """Pydantic model for ExternalMerchantSettings fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    connect_woo: str = Field(None, alias="connect_woo")
    external_platform: str = Field(None, alias="external_platform")
    id: str = Field(None, alias="id")
