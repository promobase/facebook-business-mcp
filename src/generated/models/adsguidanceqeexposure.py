"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
AdsGuidanceQEExposureField = Literal["account_exposed"]


class AdsGuidanceQEExposureFields(BaseModel):
    """Pydantic model for AdsGuidanceQEExposure fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    account_exposed: bool = Field(None, alias="account_exposed")
