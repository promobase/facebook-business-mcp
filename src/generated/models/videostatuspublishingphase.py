"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .videostatuserror import VideoStatusErrorFields


# Field literal type
VideoStatusPublishingPhaseField = Literal["errors", "publish_status", "publish_time", "status"]


class VideoStatusPublishingPhaseFields(BaseModel):
    """Pydantic model for VideoStatusPublishingPhase fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    errors: list[VideoStatusErrorFields] = Field(None, alias="errors")
    publish_status: str = Field(None, alias="publish_status")
    publish_time: datetime = Field(None, alias="publish_time")
    status: str = Field(None, alias="status")
