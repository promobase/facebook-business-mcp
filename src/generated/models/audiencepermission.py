"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .customaudience import CustomAudienceFields


# Field literal type
AudiencePermissionField = Literal["audience", "share_account_id", "share_account_name"]


class AudiencePermissionFields(BaseModel):
    """Pydantic model for AudiencePermission fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    audience: CustomAudienceFields = Field(None, alias="audience")
    share_account_id: str = Field(None, alias="share_account_id")
    share_account_name: str = Field(None, alias="share_account_name")
