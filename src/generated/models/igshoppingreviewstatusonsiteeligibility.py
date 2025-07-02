"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .igshoppingreviewstatusreasonwithhelpmessage import (
        IGShoppingReviewStatusReasonWithHelpMessageFields,
    )


# Field literal type
IGShoppingReviewStatusOnsiteEligibilityField = Literal["is_eligible", "reasons"]


class IGShoppingReviewStatusOnsiteEligibilityFields(BaseModel):
    """Pydantic model for IGShoppingReviewStatusOnsiteEligibility fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    is_eligible: bool = Field(None, alias="is_eligible")
    reasons: list[IGShoppingReviewStatusReasonWithHelpMessageFields] = Field(None, alias="reasons")
