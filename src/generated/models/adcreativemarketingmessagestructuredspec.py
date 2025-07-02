"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
AdCreativeMarketingMessageStructuredSpecField = Literal[
    "buttons",
    "footer",
    "greeting",
    "is_optimized_text",
    "language",
    "referenced_adgroup_id",
    "whats_app_business_phone_number_id",
]


class AdCreativeMarketingMessageStructuredSpecFields(BaseModel):
    """Pydantic model for AdCreativeMarketingMessageStructuredSpec fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    buttons: list[dict[str, Any]] = Field(None, alias="buttons")
    footer: str = Field(None, alias="footer")
    greeting: str = Field(None, alias="greeting")
    is_optimized_text: bool = Field(None, alias="is_optimized_text")
    language: str = Field(None, alias="language")
    referenced_adgroup_id: str = Field(None, alias="referenced_adgroup_id")
    whats_app_business_phone_number_id: str = Field(
        None, alias="whats_app_business_phone_number_id"
    )
