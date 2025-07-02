"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
WebsiteCreativeAssetSourceField = Literal["id", "source_url"]


class WebsiteCreativeAssetSourceFields(BaseModel):
    """Pydantic model for WebsiteCreativeAssetSource fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    id: str = Field(None, alias="id")
    source_url: str = Field(None, alias="source_url")
