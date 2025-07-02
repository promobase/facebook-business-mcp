"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .adaccount import AdAccountFields


# Field literal type
AdLabelField = Literal["account", "created_time", "id", "name", "updated_time"]


class AdLabelFields(BaseModel):
    """Pydantic model for AdLabel fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    account: AdAccountFields = Field(None, alias="account")
    created_time: datetime = Field(None, alias="created_time")
    id: str = Field(None, alias="id")
    name: str = Field(None, alias="name")
    updated_time: datetime = Field(None, alias="updated_time")
