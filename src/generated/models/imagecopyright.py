"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .photo import PhotoFields
    from .videocopyrightgeogate import VideoCopyrightGeoGateFields


# Field literal type
ImageCopyrightField = Literal[
    "artist",
    "copyright_monitoring_status",
    "creation_time",
    "creator",
    "custom_id",
    "description",
    "filename",
    "id",
    "image",
    "matches_count",
    "original_content_creation_date",
    "ownership_countries",
    "tags",
    "title",
    "update_time",
]


class ImageCopyrightFields(BaseModel):
    """Pydantic model for ImageCopyright fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    artist: str = Field(None, alias="artist")
    copyright_monitoring_status: str = Field(None, alias="copyright_monitoring_status")
    creation_time: datetime = Field(None, alias="creation_time")
    creator: str = Field(None, alias="creator")
    custom_id: str = Field(None, alias="custom_id")
    description: str = Field(None, alias="description")
    filename: str = Field(None, alias="filename")
    id: str = Field(None, alias="id")
    image: PhotoFields = Field(None, alias="image")
    matches_count: int = Field(None, alias="matches_count")
    original_content_creation_date: datetime = Field(None, alias="original_content_creation_date")
    ownership_countries: VideoCopyrightGeoGateFields = Field(None, alias="ownership_countries")
    tags: list[str] = Field(None, alias="tags")
    title: str = Field(None, alias="title")
    update_time: datetime = Field(None, alias="update_time")
