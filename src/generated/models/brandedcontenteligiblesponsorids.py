"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .iguser import IGUserFields
    from .page import PageFields


# Field literal type
BrandedContentEligibleSponsorIDsField = Literal["fb_page", "ig_account_v2", "ig_approval_needed"]


class BrandedContentEligibleSponsorIDsFields(BaseModel):
    """Pydantic model for BrandedContentEligibleSponsorIDs fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    fb_page: PageFields = Field(None, alias="fb_page")
    ig_account_v2: IGUserFields = Field(None, alias="ig_account_v2")
    ig_approval_needed: bool = Field(None, alias="ig_approval_needed")
