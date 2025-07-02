"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
WorkUserBadgesField = Literal["category", "description", "icon", "id", "name"]


class WorkUserBadgesFields(BaseModel):
    """Pydantic model for WorkUserBadges fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    category: str = Field(None, alias="category")
    description: str = Field(None, alias="description")
    icon: str = Field(None, alias="icon")
    id: str = Field(None, alias="id")
    name: str = Field(None, alias="name")
