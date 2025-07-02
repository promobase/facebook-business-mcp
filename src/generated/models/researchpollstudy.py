"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .adaccount import AdAccountFields


# Field literal type
ResearchPollStudyField = Literal["account", "id", "name"]


class ResearchPollStudyFields(BaseModel):
    """Pydantic model for ResearchPollStudy fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    account: AdAccountFields = Field(None, alias="account")
    id: str = Field(None, alias="id")
    name: str = Field(None, alias="name")
