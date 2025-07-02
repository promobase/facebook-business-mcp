"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .igresumablevideouploadstatus import IGResumableVideoUploadStatusFields
    from .igvideocopyrightcheckstatus import IGVideoCopyrightCheckStatusFields


# Field literal type
ShadowIGMediaBuilderField = Literal[
    "copyright_check_status", "id", "status", "status_code", "video_status"
]


class ShadowIGMediaBuilderFields(BaseModel):
    """Pydantic model for ShadowIGMediaBuilder fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    copyright_check_status: IGVideoCopyrightCheckStatusFields = Field(
        None, alias="copyright_check_status"
    )
    id: str = Field(None, alias="id")
    status: str = Field(None, alias="status")
    status_code: str = Field(None, alias="status_code")
    video_status: IGResumableVideoUploadStatusFields = Field(None, alias="video_status")
