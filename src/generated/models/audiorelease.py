"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
AudioReleaseField = Literal[
    "album_title",
    "asset_availability_status",
    "audio_availability_status",
    "audio_release_image_uri",
    "created_time",
    "displayed_artist",
    "ean",
    "genre",
    "grid",
    "id",
    "isrc",
    "label_name",
    "original_release_date",
    "parental_warning_type",
    "proprietary_id",
    "upc",
]


class AudioReleaseFields(BaseModel):
    """Pydantic model for AudioRelease fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    album_title: str = Field(None, alias="album_title")
    asset_availability_status: list[dict[int, dict[str, Any]]] = Field(
        None, alias="asset_availability_status"
    )
    audio_availability_status: str = Field(None, alias="audio_availability_status")
    audio_release_image_uri: str = Field(None, alias="audio_release_image_uri")
    created_time: datetime = Field(None, alias="created_time")
    displayed_artist: str = Field(None, alias="displayed_artist")
    ean: str = Field(None, alias="ean")
    genre: str = Field(None, alias="genre")
    grid: str = Field(None, alias="grid")
    id: str = Field(None, alias="id")
    isrc: str = Field(None, alias="isrc")
    label_name: str = Field(None, alias="label_name")
    original_release_date: datetime = Field(None, alias="original_release_date")
    parental_warning_type: str = Field(None, alias="parental_warning_type")
    proprietary_id: str = Field(None, alias="proprietary_id")
    upc: str = Field(None, alias="upc")
