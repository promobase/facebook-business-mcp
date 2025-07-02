"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .advideo import AdVideoFields


# Field literal type
DynamicVideoMetadataField = Literal["id", "tags", "url", "video"]


class DynamicVideoMetadataFields(BaseModel):
    """Pydantic model for DynamicVideoMetadata fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    id: str = Field(None, alias="id")
    tags: list[str] = Field(None, alias="tags")
    url: str = Field(None, alias="url")
    video: AdVideoFields = Field(None, alias="video")
