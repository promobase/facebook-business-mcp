"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
PageGameBotQuotaInformationField = Literal["count", "time_window"]


class PageGameBotQuotaInformationFields(BaseModel):
    """Pydantic model for PageGameBotQuotaInformation fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    count: int = Field(None, alias="count")
    time_window: int = Field(None, alias="time_window")
