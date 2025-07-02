"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
AdStudyCellField = Literal[
    "ad_entities_count", "control_percentage", "id", "name", "treatment_percentage"
]


class AdStudyCellFields(BaseModel):
    """Pydantic model for AdStudyCell fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    ad_entities_count: int = Field(None, alias="ad_entities_count")
    control_percentage: float = Field(None, alias="control_percentage")
    id: str = Field(None, alias="id")
    name: str = Field(None, alias="name")
    treatment_percentage: float = Field(None, alias="treatment_percentage")
