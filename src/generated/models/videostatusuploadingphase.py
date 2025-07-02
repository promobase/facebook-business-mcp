"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .videostatuserror import VideoStatusErrorFields


# Field literal type
VideoStatusUploadingPhaseField = Literal[
    "bytes_transferred", "errors", "source_file_size", "status"
]


class VideoStatusUploadingPhaseFields(BaseModel):
    """Pydantic model for VideoStatusUploadingPhase fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    bytes_transferred: int = Field(None, alias="bytes_transferred")
    errors: list[VideoStatusErrorFields] = Field(None, alias="errors")
    source_file_size: int = Field(None, alias="source_file_size")
    status: str = Field(None, alias="status")
