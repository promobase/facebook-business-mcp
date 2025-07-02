"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
PageRestaurantServicesField = Literal[
    "catering",
    "delivery",
    "groups",
    "kids",
    "outdoor",
    "pickup",
    "reserve",
    "takeout",
    "waiter",
    "walkins",
]


class PageRestaurantServicesFields(BaseModel):
    """Pydantic model for PageRestaurantServices fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    catering: bool = Field(None, alias="catering")
    delivery: bool = Field(None, alias="delivery")
    groups: bool = Field(None, alias="groups")
    kids: bool = Field(None, alias="kids")
    outdoor: bool = Field(None, alias="outdoor")
    pickup: bool = Field(None, alias="pickup")
    reserve: bool = Field(None, alias="reserve")
    takeout: bool = Field(None, alias="takeout")
    waiter: bool = Field(None, alias="waiter")
    walkins: bool = Field(None, alias="walkins")
