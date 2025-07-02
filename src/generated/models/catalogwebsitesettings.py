"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
CatalogWebsiteSettingsField = Literal["id", "is_allowed_to_crawl"]


class CatalogWebsiteSettingsFields(BaseModel):
    """Pydantic model for CatalogWebsiteSettings fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    id: str = Field(None, alias="id")
    is_allowed_to_crawl: bool = Field(None, alias="is_allowed_to_crawl")
