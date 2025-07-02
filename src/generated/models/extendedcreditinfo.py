"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
ExtendedCreditInfoField = Literal["credit_left", "credit_revoked", "credit_used", "using_biz_ec"]


class ExtendedCreditInfoFields(BaseModel):
    """Pydantic model for ExtendedCreditInfo fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    credit_left: str = Field(None, alias="credit_left")
    credit_revoked: bool = Field(None, alias="credit_revoked")
    credit_used: str = Field(None, alias="credit_used")
    using_biz_ec: str = Field(None, alias="using_biz_ec")
