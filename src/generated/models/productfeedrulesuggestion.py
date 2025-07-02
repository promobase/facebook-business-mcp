"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
ProductFeedRuleSuggestionField = Literal["attribute", "params", "type"]


class ProductFeedRuleSuggestionFields(BaseModel):
    """Pydantic model for ProductFeedRuleSuggestion fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    attribute: str = Field(None, alias="attribute")
    params: list[dict[str, str]] = Field(None, alias="params")
    type: str = Field(None, alias="type")
