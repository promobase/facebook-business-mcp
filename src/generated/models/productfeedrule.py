"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
ProductFeedRuleField = Literal["attribute", "id", "params", "rule_type"]


class ProductFeedRuleFields(BaseModel):
    """Pydantic model for ProductFeedRule fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    attribute: str = Field(None, alias="attribute")
    id: str = Field(None, alias="id")
    params: list[dict[str, str]] = Field(None, alias="params")
    rule_type: str = Field(None, alias="rule_type")
