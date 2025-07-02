"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .business import BusinessFields


# Field literal type
BusinessCreativeFolderField = Literal[
    "business",
    "creation_time",
    "creative_insight_permissions",
    "description",
    "id",
    "media_library_url",
    "name",
    "owner_business",
]


class BusinessCreativeFolderFields(BaseModel):
    """Pydantic model for BusinessCreativeFolder fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    business: BusinessFields = Field(None, alias="business")
    creation_time: datetime = Field(None, alias="creation_time")
    creative_insight_permissions: list[dict[str, str]] = Field(
        None, alias="creative_insight_permissions"
    )
    description: str = Field(None, alias="description")
    id: str = Field(None, alias="id")
    media_library_url: str = Field(None, alias="media_library_url")
    name: str = Field(None, alias="name")
    owner_business: BusinessFields = Field(None, alias="owner_business")
