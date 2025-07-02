"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
VoipInfoField = Literal[
    "has_mobile_app",
    "has_permission",
    "is_callable",
    "is_callable_webrtc",
    "is_pushable",
    "reason_code",
    "reason_description",
]


class VoipInfoFields(BaseModel):
    """Pydantic model for VoipInfo fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    has_mobile_app: bool = Field(None, alias="has_mobile_app")
    has_permission: bool = Field(None, alias="has_permission")
    is_callable: bool = Field(None, alias="is_callable")
    is_callable_webrtc: bool = Field(None, alias="is_callable_webrtc")
    is_pushable: bool = Field(None, alias="is_pushable")
    reason_code: int = Field(None, alias="reason_code")
    reason_description: str = Field(None, alias="reason_description")
