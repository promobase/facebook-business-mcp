"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
PhotoMetadataField = Literal[
    "camera_make",
    "camera_model",
    "datetime_modified",
    "datetime_taken",
    "exposure",
    "focal_length",
    "fstop",
    "iso_speed",
    "offline_id",
    "orientation",
    "original_height",
    "original_width",
]


class PhotoMetadataFields(BaseModel):
    """Pydantic model for PhotoMetadata fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    camera_make: str = Field(None, alias="camera_make")
    camera_model: str = Field(None, alias="camera_model")
    datetime_modified: datetime = Field(None, alias="datetime_modified")
    datetime_taken: datetime = Field(None, alias="datetime_taken")
    exposure: str = Field(None, alias="exposure")
    focal_length: str = Field(None, alias="focal_length")
    fstop: str = Field(None, alias="fstop")
    iso_speed: int = Field(None, alias="iso_speed")
    offline_id: str = Field(None, alias="offline_id")
    orientation: str = Field(None, alias="orientation")
    original_height: str = Field(None, alias="original_height")
    original_width: str = Field(None, alias="original_width")
