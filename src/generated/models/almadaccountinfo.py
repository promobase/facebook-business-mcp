"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
ALMAdAccountInfoField = Literal[
    "ad_account_id",
    "id",
    "managed_by",
    "owned_by",
    "parent_advertiser_id",
    "sub_vertical",
    "tag",
    "user_ids",
    "vertical",
]


class ALMAdAccountInfoFields(BaseModel):
    """Pydantic model for ALMAdAccountInfo fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    ad_account_id: str = Field(None, alias="ad_account_id")
    id: str = Field(None, alias="id")
    managed_by: str = Field(None, alias="managed_by")
    owned_by: str = Field(None, alias="owned_by")
    parent_advertiser_id: str = Field(None, alias="parent_advertiser_id")
    sub_vertical: str = Field(None, alias="sub_vertical")
    tag: list[str] = Field(None, alias="tag")
    user_ids: list[str] = Field(None, alias="user_ids")
    vertical: str = Field(None, alias="vertical")
