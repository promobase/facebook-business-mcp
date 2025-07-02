"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
AdLimitsEnforcementDataField = Literal[
    "ad_limit_on_page",
    "ad_limit_on_scope",
    "ad_volume_on_page",
    "ad_volume_on_scope",
    "is_admin",
    "page_name",
]


class AdLimitsEnforcementDataFields(BaseModel):
    """Pydantic model for AdLimitsEnforcementData fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    ad_limit_on_page: int = Field(None, alias="ad_limit_on_page")
    ad_limit_on_scope: int = Field(None, alias="ad_limit_on_scope")
    ad_volume_on_page: int = Field(None, alias="ad_volume_on_page")
    ad_volume_on_scope: int = Field(None, alias="ad_volume_on_scope")
    is_admin: bool = Field(None, alias="is_admin")
    page_name: str = Field(None, alias="page_name")
