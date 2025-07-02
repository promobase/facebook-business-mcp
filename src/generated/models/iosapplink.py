"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
IosAppLinkField = Literal["app_name", "app_store_id", "url"]


class IosAppLinkFields(BaseModel):
    """Pydantic model for IosAppLink fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    app_name: str = Field(None, alias="app_name")
    app_store_id: str = Field(None, alias="app_store_id")
    url: str = Field(None, alias="url")
