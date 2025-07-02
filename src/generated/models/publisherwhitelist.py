"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
PublisherWhiteListField = Literal[
    "business_owner_id", "id", "last_updated_time", "last_updated_user", "name", "placement_type"
]


class PublisherWhiteListFields(BaseModel):
    """Pydantic model for PublisherWhiteList fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    business_owner_id: str = Field(None, alias="business_owner_id")
    id: str = Field(None, alias="id")
    last_updated_time: datetime = Field(None, alias="last_updated_time")
    last_updated_user: str = Field(None, alias="last_updated_user")
    name: str = Field(None, alias="name")
    placement_type: str = Field(None, alias="placement_type")
