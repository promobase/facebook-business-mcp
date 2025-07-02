"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
TargetingGeoLocationLocationClusterField = Literal["key"]


class TargetingGeoLocationLocationClusterFields(BaseModel):
    """Pydantic model for TargetingGeoLocationLocationCluster fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    key: int = Field(None, alias="key")
