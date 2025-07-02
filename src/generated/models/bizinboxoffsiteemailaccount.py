"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
BizInboxOffsiteEmailAccountField = Literal["email_address", "id"]


class BizInboxOffsiteEmailAccountFields(BaseModel):
    """Pydantic model for BizInboxOffsiteEmailAccount fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    email_address: str = Field(None, alias="email_address")
    id: str = Field(None, alias="id")
