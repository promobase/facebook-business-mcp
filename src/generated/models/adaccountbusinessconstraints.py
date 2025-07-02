"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field


class AdAccountBusinessConstraints_status(str, Enum):
    """AdAccountBusinessConstraints_status enum values."""

    ACTIVE = "ACTIVE"
    APPLICATION_IN_PROGRESS = "APPLICATION_IN_PROGRESS"
    WITH_CAMPAIGN_ERROR = "WITH_CAMPAIGN_ERROR"


# Field literal type
AdAccountBusinessConstraintsField = Literal[
    "audience_controls", "campaigns_with_error", "placement_controls", "status"
]


class AdAccountBusinessConstraintsFields(BaseModel):
    """Pydantic model for AdAccountBusinessConstraints fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    audience_controls: dict[str, Any] = Field(None, alias="audience_controls")
    campaigns_with_error: list[str] = Field(None, alias="campaigns_with_error")
    placement_controls: dict[str, Any] = Field(None, alias="placement_controls")
    status: dict[str, Any] = Field(None, alias="status")
