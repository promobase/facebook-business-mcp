"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
AdCreativeRegionalRegulationDisclaimerField = Literal[
    "australia_finserv",
    "india_finserv",
    "singapore_universal",
    "taiwan_finserv",
    "taiwan_universal",
]


class AdCreativeRegionalRegulationDisclaimerFields(BaseModel):
    """Pydantic model for AdCreativeRegionalRegulationDisclaimer fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    australia_finserv: dict[str, Any] = Field(None, alias="australia_finserv")
    india_finserv: dict[str, Any] = Field(None, alias="india_finserv")
    singapore_universal: dict[str, Any] = Field(None, alias="singapore_universal")
    taiwan_finserv: dict[str, Any] = Field(None, alias="taiwan_finserv")
    taiwan_universal: dict[str, Any] = Field(None, alias="taiwan_universal")
