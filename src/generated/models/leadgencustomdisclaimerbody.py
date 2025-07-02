"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .leadgenurlentityatranges import LeadGenURLEntityAtRangesFields


# Field literal type
LeadGenCustomDisclaimerBodyField = Literal["text", "url_entities"]


class LeadGenCustomDisclaimerBodyFields(BaseModel):
    """Pydantic model for LeadGenCustomDisclaimerBody fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    text: str = Field(None, alias="text")
    url_entities: list[LeadGenURLEntityAtRangesFields] = Field(None, alias="url_entities")
