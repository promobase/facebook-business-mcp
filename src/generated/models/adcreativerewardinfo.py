"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
AdCreativeRewardInfoField = Literal["reward_offer_id", "reward_program_id"]


class AdCreativeRewardInfoFields(BaseModel):
    """Pydantic model for AdCreativeRewardInfo fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    reward_offer_id: str = Field(None, alias="reward_offer_id")
    reward_program_id: str = Field(None, alias="reward_program_id")
