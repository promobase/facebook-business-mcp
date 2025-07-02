"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
RevSharePolicyField = Literal["policy_id", "policy_name"]


class RevSharePolicyFields(BaseModel):
    """Pydantic model for RevSharePolicy fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    policy_id: str = Field(None, alias="policy_id")
    policy_name: str = Field(None, alias="policy_name")
