"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
ArAdsDataContainerField = Literal[
    "camera_facing_override",
    "creation_time",
    "effect",
    "id",
    "is_published",
    "last_modified_time",
    "name",
]


class ArAdsDataContainerFields(BaseModel):
    """Pydantic model for ArAdsDataContainer fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    camera_facing_override: str = Field(None, alias="camera_facing_override")
    creation_time: datetime = Field(None, alias="creation_time")
    effect: list[dict[str, Any]] = Field(None, alias="effect")
    id: str = Field(None, alias="id")
    is_published: bool = Field(None, alias="is_published")
    last_modified_time: datetime = Field(None, alias="last_modified_time")
    name: str = Field(None, alias="name")
