"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .igshoppingreviewstatusonsiteeligibility import (
        IGShoppingReviewStatusOnsiteEligibilityFields,
    )
    from .igshoppingreviewstatusreasonwithhelpmessage import (
        IGShoppingReviewStatusReasonWithHelpMessageFields,
    )


# Field literal type
IGShoppingReviewStatusField = Literal["onsite_eligibility", "reasons", "status"]


class IGShoppingReviewStatusFields(BaseModel):
    """Pydantic model for IGShoppingReviewStatus fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    onsite_eligibility: IGShoppingReviewStatusOnsiteEligibilityFields = Field(
        None, alias="onsite_eligibility"
    )
    reasons: list[IGShoppingReviewStatusReasonWithHelpMessageFields] = Field(None, alias="reasons")
    status: str = Field(None, alias="status")
