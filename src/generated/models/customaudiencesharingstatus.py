"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
CustomAudienceSharingStatusField = Literal["sharing_relationship_id", "status"]


class CustomAudienceSharingStatusFields(BaseModel):
    """Pydantic model for CustomAudienceSharingStatus fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    sharing_relationship_id: int = Field(None, alias="sharing_relationship_id")
    status: str = Field(None, alias="status")
