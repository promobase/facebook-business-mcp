"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .page import PageFields
    from .pagechangeproposal import PageChangeProposalFields


# Field literal type
PageUpcomingChangeField = Literal[
    "change_type", "effective_time", "id", "page", "proposal", "timer_status"
]


class PageUpcomingChangeFields(BaseModel):
    """Pydantic model for PageUpcomingChange fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    change_type: str = Field(None, alias="change_type")
    effective_time: datetime = Field(None, alias="effective_time")
    id: str = Field(None, alias="id")
    page: PageFields = Field(None, alias="page")
    proposal: PageChangeProposalFields = Field(None, alias="proposal")
    timer_status: str = Field(None, alias="timer_status")
