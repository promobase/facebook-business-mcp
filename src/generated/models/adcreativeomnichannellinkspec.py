"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
AdCreativeOmnichannelLinkSpecField = Literal["app", "web"]


class AdCreativeOmnichannelLinkSpecFields(BaseModel):
    """Pydantic model for AdCreativeOmnichannelLinkSpec fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    app: dict[str, Any] = Field(None, alias="app")
    web: dict[str, Any] = Field(None, alias="web")
