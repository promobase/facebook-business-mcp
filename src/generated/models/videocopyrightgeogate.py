"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
VideoCopyrightGeoGateField = Literal["excluded_countries", "included_countries"]


class VideoCopyrightGeoGateFields(BaseModel):
    """Pydantic model for VideoCopyrightGeoGate fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    excluded_countries: list[str] = Field(None, alias="excluded_countries")
    included_countries: list[str] = Field(None, alias="included_countries")
