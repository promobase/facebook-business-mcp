"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
CampaignGroupBrandConfigurationField = Literal["brand_product_name", "locale", "vertical"]


class CampaignGroupBrandConfigurationFields(BaseModel):
    """Pydantic model for CampaignGroupBrandConfiguration fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    brand_product_name: str = Field(None, alias="brand_product_name")
    locale: str = Field(None, alias="locale")
    vertical: str = Field(None, alias="vertical")
