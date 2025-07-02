"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .adaccount import AdAccountFields


# Field literal type
AdsCreationSavedStateField = Literal[
    "ad_account", "id", "serialized_store_data", "time_updated", "user"
]


class AdsCreationSavedStateFields(BaseModel):
    """Pydantic model for AdsCreationSavedState fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    ad_account: AdAccountFields = Field(None, alias="ad_account")
    id: str = Field(None, alias="id")
    serialized_store_data: str = Field(None, alias="serialized_store_data")
    time_updated: datetime = Field(None, alias="time_updated")
    user: dict[str, Any] = Field(None, alias="user")
