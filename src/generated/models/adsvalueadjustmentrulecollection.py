"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
AdsValueAdjustmentRuleCollectionField = Literal[
    "id", "is_default_setting", "name", "product_type", "status"
]


class AdsValueAdjustmentRuleCollectionFields(BaseModel):
    """Pydantic model for AdsValueAdjustmentRuleCollection fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    id: str = Field(None, alias="id")
    is_default_setting: bool = Field(None, alias="is_default_setting")
    name: str = Field(None, alias="name")
    product_type: str = Field(None, alias="product_type")
    status: str = Field(None, alias="status")
