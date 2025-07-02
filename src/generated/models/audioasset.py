"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .page import PageFields


# Field literal type
AudioAssetField = Literal[
    "all_ddex_featured_artists",
    "all_ddex_main_artists",
    "audio_cluster_id",
    "cover_image_source",
    "display_artist",
    "download_hd_url",
    "download_sd_url",
    "duration_in_ms",
    "freeform_genre",
    "grid",
    "id",
    "is_test",
    "original_release_date",
    "owner",
    "parental_warning_type",
    "subtitle",
    "title",
    "title_with_featured_artists",
    "upc",
]


class AudioAssetFields(BaseModel):
    """Pydantic model for AudioAsset fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    all_ddex_featured_artists: str = Field(None, alias="all_ddex_featured_artists")
    all_ddex_main_artists: str = Field(None, alias="all_ddex_main_artists")
    audio_cluster_id: str = Field(None, alias="audio_cluster_id")
    cover_image_source: str = Field(None, alias="cover_image_source")
    display_artist: str = Field(None, alias="display_artist")
    download_hd_url: str = Field(None, alias="download_hd_url")
    download_sd_url: str = Field(None, alias="download_sd_url")
    duration_in_ms: int = Field(None, alias="duration_in_ms")
    freeform_genre: str = Field(None, alias="freeform_genre")
    grid: str = Field(None, alias="grid")
    id: str = Field(None, alias="id")
    is_test: bool = Field(None, alias="is_test")
    original_release_date: datetime = Field(None, alias="original_release_date")
    owner: PageFields = Field(None, alias="owner")
    parental_warning_type: str = Field(None, alias="parental_warning_type")
    subtitle: str = Field(None, alias="subtitle")
    title: str = Field(None, alias="title")
    title_with_featured_artists: str = Field(None, alias="title_with_featured_artists")
    upc: str = Field(None, alias="upc")
