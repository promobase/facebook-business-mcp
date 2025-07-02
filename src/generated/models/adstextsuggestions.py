"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
AdsTextSuggestionsField = Literal[
    "ad_account_id", "bodies", "descriptions", "inactive_session_tally", "long", "short", "titles"
]


class AdsTextSuggestionsFields(BaseModel):
    """Pydantic model for AdsTextSuggestions fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    ad_account_id: str = Field(None, alias="ad_account_id")
    bodies: list[dict[str, Any]] = Field(None, alias="bodies")
    descriptions: list[dict[str, Any]] = Field(None, alias="descriptions")
    inactive_session_tally: int = Field(None, alias="inactive_session_tally")
    long: list[dict[str, Any]] = Field(None, alias="long")
    short: list[dict[str, Any]] = Field(None, alias="short")
    titles: list[dict[str, Any]] = Field(None, alias="titles")
