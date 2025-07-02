"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
CPASLsbImageBankField = Literal["ad_group_id", "catalog_segment_proxy_id", "id"]


class CPASLsbImageBankFields(BaseModel):
    """Pydantic model for CPASLsbImageBank fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    ad_group_id: str = Field(None, alias="ad_group_id")
    catalog_segment_proxy_id: str = Field(None, alias="catalog_segment_proxy_id")
    id: str = Field(None, alias="id")
