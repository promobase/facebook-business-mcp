"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
AdAccountPromotableObjectsField = Literal[
    "promotable_app_ids", "promotable_page_ids", "promotable_urls"
]


class AdAccountPromotableObjectsFields(BaseModel):
    """Pydantic model for AdAccountPromotableObjects fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    promotable_app_ids: list[str] = Field(None, alias="promotable_app_ids")
    promotable_page_ids: list[str] = Field(None, alias="promotable_page_ids")
    promotable_urls: list[str] = Field(None, alias="promotable_urls")
