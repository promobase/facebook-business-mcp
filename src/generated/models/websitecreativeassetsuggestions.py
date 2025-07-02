"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
WebsiteCreativeAssetSuggestionsField = Literal[
    "ad_account_id", "extraction_status", "id", "link_url"
]


class WebsiteCreativeAssetSuggestionsFields(BaseModel):
    """Pydantic model for WebsiteCreativeAssetSuggestions fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    ad_account_id: str = Field(None, alias="ad_account_id")
    extraction_status: str = Field(None, alias="extraction_status")
    id: str = Field(None, alias="id")
    link_url: str = Field(None, alias="link_url")
