"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
ProductFeedRulePreviewSampleField = Literal["properties_after", "properties_before"]


class ProductFeedRulePreviewSampleFields(BaseModel):
    """Pydantic model for ProductFeedRulePreviewSample fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    properties_after: list[dict[str, str]] = Field(None, alias="properties_after")
    properties_before: list[dict[str, str]] = Field(None, alias="properties_before")
