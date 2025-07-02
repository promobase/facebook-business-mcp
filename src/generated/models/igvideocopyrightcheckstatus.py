"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
IGVideoCopyrightCheckStatusField = Literal["matches_found", "status"]


class IGVideoCopyrightCheckStatusFields(BaseModel):
    """Pydantic model for IGVideoCopyrightCheckStatus fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    matches_found: bool = Field(None, alias="matches_found")
    status: str = Field(None, alias="status")
