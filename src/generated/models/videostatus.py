"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .videocopyrightcheckstatus import VideoCopyrightCheckStatusFields
    from .videostatusprocessingphase import VideoStatusProcessingPhaseFields
    from .videostatuspublishingphase import VideoStatusPublishingPhaseFields
    from .videostatusuploadingphase import VideoStatusUploadingPhaseFields


# Field literal type
VideoStatusField = Literal[
    "copyright_check_status",
    "processing_phase",
    "processing_progress",
    "publishing_phase",
    "uploading_phase",
    "video_status",
]


class VideoStatusFields(BaseModel):
    """Pydantic model for VideoStatus fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    copyright_check_status: VideoCopyrightCheckStatusFields = Field(
        None, alias="copyright_check_status"
    )
    processing_phase: VideoStatusProcessingPhaseFields = Field(None, alias="processing_phase")
    processing_progress: int = Field(None, alias="processing_progress")
    publishing_phase: VideoStatusPublishingPhaseFields = Field(None, alias="publishing_phase")
    uploading_phase: VideoStatusUploadingPhaseFields = Field(None, alias="uploading_phase")
    video_status: str = Field(None, alias="video_status")
