"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field


class adgroupfacebookfeedbackcomments_order_enum_param(str, Enum):
    """adgroupfacebookfeedbackcomments_order_enum_param enum values."""

    chronological = "chronological"
    reverse_chronological = "reverse_chronological"


# Field literal type
AdgroupFacebookFeedbackField = Literal["id", "preview"]


class AdgroupFacebookFeedbackFields(BaseModel):
    """Pydantic model for AdgroupFacebookFeedback fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    id: str = Field(None, alias="id")
    preview: str = Field(None, alias="preview")


class AdgroupFacebookFeedbackGetCommentsParams(BaseModel):
    """Parameters for AdgroupFacebookFeedback.get_comments()."""

    model_config = ConfigDict(extra="forbid")
    order: adgroupfacebookfeedbackcomments_order_enum_param | None = Field(
        None, description="order parameter"
    )
