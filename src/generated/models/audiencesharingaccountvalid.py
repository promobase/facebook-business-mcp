"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
AudienceSharingAccountValidField = Literal[
    "account_id",
    "account_type",
    "business_id",
    "business_name",
    "can_ad_account_use_lookalike_container",
    "sharing_agreement_status",
]


class AudienceSharingAccountValidFields(BaseModel):
    """Pydantic model for AudienceSharingAccountValid fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    account_id: str = Field(None, alias="account_id")
    account_type: str = Field(None, alias="account_type")
    business_id: str = Field(None, alias="business_id")
    business_name: str = Field(None, alias="business_name")
    can_ad_account_use_lookalike_container: bool = Field(
        None, alias="can_ad_account_use_lookalike_container"
    )
    sharing_agreement_status: int = Field(None, alias="sharing_agreement_status")
