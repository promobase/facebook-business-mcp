"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
BAPIDomainField = Literal["domain", "in_cool_down_until", "is_eligible_for_vo", "is_in_cool_down"]


class BAPIDomainFields(BaseModel):
    """Pydantic model for BAPIDomain fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    domain: str = Field(None, alias="domain")
    in_cool_down_until: int = Field(None, alias="in_cool_down_until")
    is_eligible_for_vo: bool = Field(None, alias="is_eligible_for_vo")
    is_in_cool_down: bool = Field(None, alias="is_in_cool_down")
