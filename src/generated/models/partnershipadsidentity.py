"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
PartnershipAdsIdentityField = Literal["is_saved", "post_types", "secondary_identities"]


class PartnershipAdsIdentityFields(BaseModel):
    """Pydantic model for PartnershipAdsIdentity fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    is_saved: bool = Field(None, alias="is_saved")
    post_types: list[str] = Field(None, alias="post_types")
    secondary_identities: list[dict[str, Any]] = Field(None, alias="secondary_identities")
