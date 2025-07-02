"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
PageGetStartedNullstateField = Literal["cta_title", "processed_greeting", "responsiveness"]


class PageGetStartedNullstateFields(BaseModel):
    """Pydantic model for PageGetStartedNullstate fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    cta_title: str = Field(None, alias="cta_title")
    processed_greeting: str = Field(None, alias="processed_greeting")
    responsiveness: str = Field(None, alias="responsiveness")
