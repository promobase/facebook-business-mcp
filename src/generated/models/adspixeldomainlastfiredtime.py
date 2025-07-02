"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
AdsPixelDomainLastFiredTimeField = Literal["domain_name", "last_fired_time"]


class AdsPixelDomainLastFiredTimeFields(BaseModel):
    """Pydantic model for AdsPixelDomainLastFiredTime fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    domain_name: str = Field(None, alias="domain_name")
    last_fired_time: int = Field(None, alias="last_fired_time")
