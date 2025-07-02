"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .user import UserFields


# Field literal type
WoodhengeSupporterField = Literal[
    "creation_time",
    "id",
    "is_gifted_subscription",
    "most_recent_subscription_time",
    "number_of_months_subscribed",
    "user",
]


class WoodhengeSupporterFields(BaseModel):
    """Pydantic model for WoodhengeSupporter fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    creation_time: datetime = Field(None, alias="creation_time")
    id: str = Field(None, alias="id")
    is_gifted_subscription: bool = Field(None, alias="is_gifted_subscription")
    most_recent_subscription_time: datetime = Field(None, alias="most_recent_subscription_time")
    number_of_months_subscribed: int = Field(None, alias="number_of_months_subscribed")
    user: UserFields = Field(None, alias="user")
