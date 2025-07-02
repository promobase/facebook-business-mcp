"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
URLField = Literal["engagement", "id", "og_object", "ownership_permissions", "scopes"]


class URLFields(BaseModel):
    """Pydantic model for URL fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    engagement: dict[str, Any] = Field(None, alias="engagement")
    id: str = Field(None, alias="id")
    og_object: dict[str, Any] = Field(None, alias="og_object")
    ownership_permissions: dict[str, Any] = Field(None, alias="ownership_permissions")
    scopes: dict[str, Any] = Field(None, alias="scopes")
