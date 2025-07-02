"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
WebAppLinkField = Literal["should_fallback", "url"]


class WebAppLinkFields(BaseModel):
    """Pydantic model for WebAppLink fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    should_fallback: bool = Field(None, alias="should_fallback")
    url: str = Field(None, alias="url")
