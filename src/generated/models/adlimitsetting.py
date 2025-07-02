"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
AdLimitSettingField = Literal["limit_allocation_by_page_advertisers"]


class AdLimitSettingFields(BaseModel):
    """Pydantic model for AdLimitSetting fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    limit_allocation_by_page_advertisers: list[dict[str, int]] = Field(
        None, alias="limit_allocation_by_page_advertisers"
    )
