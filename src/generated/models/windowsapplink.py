"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
WindowsAppLinkField = Literal["app_id", "app_name", "package_family_name", "url"]


class WindowsAppLinkFields(BaseModel):
    """Pydantic model for WindowsAppLink fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    app_id: str = Field(None, alias="app_id")
    app_name: str = Field(None, alias="app_name")
    package_family_name: str = Field(None, alias="package_family_name")
    url: str = Field(None, alias="url")
