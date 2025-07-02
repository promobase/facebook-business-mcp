"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
InstagramBusinessAssetField = Literal["id", "ig_user_id", "ig_username"]


class InstagramBusinessAssetFields(BaseModel):
    """Pydantic model for InstagramBusinessAsset fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    id: str = Field(None, alias="id")
    ig_user_id: str = Field(None, alias="ig_user_id")
    ig_username: str = Field(None, alias="ig_username")
