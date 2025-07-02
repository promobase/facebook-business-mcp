"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .videostatusprocessingphase import VideoStatusProcessingPhaseFields
    from .videostatusuploadingphase import VideoStatusUploadingPhaseFields


# Field literal type
IGResumableVideoUploadStatusField = Literal["processing_phase", "uploading_phase"]


class IGResumableVideoUploadStatusFields(BaseModel):
    """Pydantic model for IGResumableVideoUploadStatus fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    processing_phase: VideoStatusProcessingPhaseFields = Field(None, alias="processing_phase")
    uploading_phase: VideoStatusUploadingPhaseFields = Field(None, alias="uploading_phase")
