"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
AudioIsrcField = Literal[
    "all_kg_featured_artists",
    "all_kg_main_artists",
    "artist_profile_picture_url",
    "id",
    "isrc",
    "publishing_rights_data",
    "top_searchable_artist_id",
    "top_searchable_artist_name",
    "top_searchable_artist_profile_pic_url",
]


class AudioIsrcFields(BaseModel):
    """Pydantic model for AudioIsrc fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    all_kg_featured_artists: str = Field(None, alias="all_kg_featured_artists")
    all_kg_main_artists: str = Field(None, alias="all_kg_main_artists")
    artist_profile_picture_url: str = Field(None, alias="artist_profile_picture_url")
    id: str = Field(None, alias="id")
    isrc: str = Field(None, alias="isrc")
    publishing_rights_data: dict[str, Any] = Field(None, alias="publishing_rights_data")
    top_searchable_artist_id: str = Field(None, alias="top_searchable_artist_id")
    top_searchable_artist_name: str = Field(None, alias="top_searchable_artist_name")
    top_searchable_artist_profile_pic_url: str = Field(
        None, alias="top_searchable_artist_profile_pic_url"
    )
