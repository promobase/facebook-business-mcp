"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .adgroupplacementspecificreviewfeedback import AdgroupPlacementSpecificReviewFeedbackFields


# Field literal type
AdgroupReviewFeedbackField = Literal["global", "placement_specific"]


class AdgroupReviewFeedbackFields(BaseModel):
    """Pydantic model for AdgroupReviewFeedback fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    global_: dict[str, str] = Field(None, alias="global")
    placement_specific: AdgroupPlacementSpecificReviewFeedbackFields = Field(
        None, alias="placement_specific"
    )
