"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
ShadowIGMediaCollaboratorsField = Literal["id", "invite_status", "username"]


class ShadowIGMediaCollaboratorsFields(BaseModel):
    """Pydantic model for ShadowIGMediaCollaborators fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    id: str = Field(None, alias="id")
    invite_status: str = Field(None, alias="invite_status")
    username: str = Field(None, alias="username")
