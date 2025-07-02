"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
IGUserSubscribedAppsDataField = Literal["app_id", "subscribed_fields"]


class IGUserSubscribedAppsDataFields(BaseModel):
    """Pydantic model for IGUserSubscribedAppsData fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    app_id: str = Field(None, alias="app_id")
    subscribed_fields: list[str] = Field(None, alias="subscribed_fields")
