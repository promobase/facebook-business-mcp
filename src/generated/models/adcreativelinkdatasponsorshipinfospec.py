"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
AdCreativeLinkDataSponsorshipInfoSpecField = Literal["sponsor_image_url", "sponsor_name"]


class AdCreativeLinkDataSponsorshipInfoSpecFields(BaseModel):
    """Pydantic model for AdCreativeLinkDataSponsorshipInfoSpec fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    sponsor_image_url: str = Field(None, alias="sponsor_image_url")
    sponsor_name: str = Field(None, alias="sponsor_name")
