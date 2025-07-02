"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
AdCampaignGroupStructureTreeField = Literal["children", "id", "name", "time_updated"]


class AdCampaignGroupStructureTreeFields(BaseModel):
    """Pydantic model for AdCampaignGroupStructureTree fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    children: list[AdCampaignGroupStructureTreeFields] = Field(None, alias="children")
    id: str = Field(None, alias="id")
    name: str = Field(None, alias="name")
    time_updated: int = Field(None, alias="time_updated")
