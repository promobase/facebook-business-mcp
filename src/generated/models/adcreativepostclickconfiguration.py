"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
AdCreativePostClickConfigurationField = Literal[
    "post_click_item_description", "post_click_item_headline"
]


class AdCreativePostClickConfigurationFields(BaseModel):
    """Pydantic model for AdCreativePostClickConfiguration fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    post_click_item_description: str = Field(None, alias="post_click_item_description")
    post_click_item_headline: str = Field(None, alias="post_click_item_headline")
