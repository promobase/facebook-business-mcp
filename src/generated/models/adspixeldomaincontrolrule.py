"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
AdsPixelDomainControlRuleField = Literal["domain_list", "type"]


class AdsPixelDomainControlRuleFields(BaseModel):
    """Pydantic model for AdsPixelDomainControlRule fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    domain_list: list[dict[str, Any]] = Field(None, alias="domain_list")
    type: str = Field(None, alias="type")
