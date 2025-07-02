"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
InstagramShoppingMerchantReviewMessageField = Literal["help_url", "message"]


class InstagramShoppingMerchantReviewMessageFields(BaseModel):
    """Pydantic model for InstagramShoppingMerchantReviewMessage fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    help_url: str = Field(None, alias="help_url")
    message: str = Field(None, alias="message")
