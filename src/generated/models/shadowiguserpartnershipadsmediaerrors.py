"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
ShadowIGUserPartnershipAdsMediaErrorsField = Literal[
    "ad_code", "error_codes", "errors", "permalink"
]


class ShadowIGUserPartnershipAdsMediaErrorsFields(BaseModel):
    """Pydantic model for ShadowIGUserPartnershipAdsMediaErrors fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    ad_code: str = Field(None, alias="ad_code")
    error_codes: str = Field(None, alias="error_codes")
    errors: list[str] = Field(None, alias="errors")
    permalink: str = Field(None, alias="permalink")
