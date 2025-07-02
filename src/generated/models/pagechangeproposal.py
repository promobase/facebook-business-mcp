"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .pageupcomingchange import PageUpcomingChangeFields


# Field literal type
PageChangeProposalField = Literal["acceptance_status", "category", "id", "upcoming_change_info"]


class PageChangeProposalFields(BaseModel):
    """Pydantic model for PageChangeProposal fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    acceptance_status: str = Field(None, alias="acceptance_status")
    category: str = Field(None, alias="category")
    id: str = Field(None, alias="id")
    upcoming_change_info: PageUpcomingChangeFields = Field(None, alias="upcoming_change_info")
