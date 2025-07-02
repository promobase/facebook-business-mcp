"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .advideo import AdVideoFields
    from .business import BusinessFields


# Field literal type
BusinessVideoField = Literal["business", "id", "media_library_url", "name", "video"]


class BusinessVideoFields(BaseModel):
    """Pydantic model for BusinessVideo fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    business: BusinessFields = Field(None, alias="business")
    id: str = Field(None, alias="id")
    media_library_url: str = Field(None, alias="media_library_url")
    name: str = Field(None, alias="name")
    video: AdVideoFields = Field(None, alias="video")
