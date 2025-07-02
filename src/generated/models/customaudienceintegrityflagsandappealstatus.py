"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
CustomAudienceIntegrityFlagsAndAppealStatusField = Literal[
    "closeout_time",
    "flagged_fields",
    "latest_appeal_requestor",
    "latest_appeal_time",
    "restriction_status",
]


class CustomAudienceIntegrityFlagsAndAppealStatusFields(BaseModel):
    """Pydantic model for CustomAudienceIntegrityFlagsAndAppealStatus fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    closeout_time: int = Field(None, alias="closeout_time")
    flagged_fields: list[str] = Field(None, alias="flagged_fields")
    latest_appeal_requestor: str = Field(None, alias="latest_appeal_requestor")
    latest_appeal_time: int = Field(None, alias="latest_appeal_time")
    restriction_status: str = Field(None, alias="restriction_status")
