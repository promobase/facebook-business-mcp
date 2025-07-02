"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
RegionalRegulationIdentitiesField = Literal[
    "australia_finserv_beneficiary",
    "australia_finserv_payer",
    "india_finserv_beneficiary",
    "india_finserv_payer",
    "singapore_universal_beneficiary",
    "singapore_universal_payer",
    "taiwan_finserv_beneficiary",
    "taiwan_finserv_payer",
    "taiwan_universal_beneficiary",
    "taiwan_universal_payer",
]


class RegionalRegulationIdentitiesFields(BaseModel):
    """Pydantic model for RegionalRegulationIdentities fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    australia_finserv_beneficiary: str = Field(None, alias="australia_finserv_beneficiary")
    australia_finserv_payer: str = Field(None, alias="australia_finserv_payer")
    india_finserv_beneficiary: str = Field(None, alias="india_finserv_beneficiary")
    india_finserv_payer: str = Field(None, alias="india_finserv_payer")
    singapore_universal_beneficiary: str = Field(None, alias="singapore_universal_beneficiary")
    singapore_universal_payer: str = Field(None, alias="singapore_universal_payer")
    taiwan_finserv_beneficiary: str = Field(None, alias="taiwan_finserv_beneficiary")
    taiwan_finserv_payer: str = Field(None, alias="taiwan_finserv_payer")
    taiwan_universal_beneficiary: str = Field(None, alias="taiwan_universal_beneficiary")
    taiwan_universal_payer: str = Field(None, alias="taiwan_universal_payer")
