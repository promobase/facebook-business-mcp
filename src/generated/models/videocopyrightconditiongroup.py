"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
VideoCopyrightConditionGroupField = Literal["action", "conditions", "validity_status"]


class VideoCopyrightConditionGroupFields(BaseModel):
    """Pydantic model for VideoCopyrightConditionGroup fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    action: str = Field(None, alias="action")
    conditions: list[dict[str, Any]] = Field(None, alias="conditions")
    validity_status: str = Field(None, alias="validity_status")
