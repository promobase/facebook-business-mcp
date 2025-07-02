"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
AdCreativeFacebookBrandedContentField = Literal[
    "shared_to_sponsor_status", "sponsor_page_id", "sponsor_relationship"
]


class AdCreativeFacebookBrandedContentFields(BaseModel):
    """Pydantic model for AdCreativeFacebookBrandedContent fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    shared_to_sponsor_status: str = Field(None, alias="shared_to_sponsor_status")
    sponsor_page_id: str = Field(None, alias="sponsor_page_id")
    sponsor_relationship: str = Field(None, alias="sponsor_relationship")
