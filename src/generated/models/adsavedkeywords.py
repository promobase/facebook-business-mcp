"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .adaccount import AdAccountFields
    from .adkeywords import AdKeywordsFields


# Field literal type
AdSavedKeywordsField = Literal[
    "account", "id", "keywords", "name", "run_status", "time_created", "time_updated"
]


class AdSavedKeywordsFields(BaseModel):
    """Pydantic model for AdSavedKeywords fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    account: AdAccountFields = Field(None, alias="account")
    id: str = Field(None, alias="id")
    keywords: AdKeywordsFields = Field(None, alias="keywords")
    name: str = Field(None, alias="name")
    run_status: str = Field(None, alias="run_status")
    time_created: datetime = Field(None, alias="time_created")
    time_updated: datetime = Field(None, alias="time_updated")
