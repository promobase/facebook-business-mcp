"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
AudiencePermissionForActionsField = Literal[
    "can_edit",
    "can_see_insight",
    "can_share",
    "subtype_supports_lookalike",
    "supports_recipient_lookalike",
]


class AudiencePermissionForActionsFields(BaseModel):
    """Pydantic model for AudiencePermissionForActions fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    can_edit: bool = Field(None, alias="can_edit")
    can_see_insight: bool = Field(None, alias="can_see_insight")
    can_share: bool = Field(None, alias="can_share")
    subtype_supports_lookalike: bool = Field(None, alias="subtype_supports_lookalike")
    supports_recipient_lookalike: bool = Field(None, alias="supports_recipient_lookalike")
