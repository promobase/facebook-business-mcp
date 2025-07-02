"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field


class AdsNamingTemplate_level(str, Enum):
    """AdsNamingTemplate_level enum values."""

    ADGROUP = "ADGROUP"
    AD_ACCOUNT = "AD_ACCOUNT"
    CAMPAIGN = "CAMPAIGN"
    CAMPAIGN_GROUP = "CAMPAIGN_GROUP"
    OPPORTUNITIES = "OPPORTUNITIES"
    PRIVACY_INFO_CENTER = "PRIVACY_INFO_CENTER"
    PRODUCT = "PRODUCT"
    TOPLINE = "TOPLINE"
    UNIQUE_ADCREATIVE = "UNIQUE_ADCREATIVE"


# Field literal type
AdsNamingTemplateField = Literal[
    "api_fields",
    "api_version",
    "field_order",
    "id",
    "level",
    "separator",
    "template_version",
    "user_defined_fields",
    "value_separator",
]


class AdsNamingTemplateFields(BaseModel):
    """Pydantic model for AdsNamingTemplate fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    api_fields: list[list[dict[str, list[dict[str, str]]]]] = Field(None, alias="api_fields")
    api_version: str = Field(None, alias="api_version")
    field_order: list[str] = Field(None, alias="field_order")
    id: str = Field(None, alias="id")
    level: dict[str, Any] = Field(None, alias="level")
    separator: str = Field(None, alias="separator")
    template_version: str = Field(None, alias="template_version")
    user_defined_fields: list[list[dict[str, list[str]]]] = Field(None, alias="user_defined_fields")
    value_separator: str = Field(None, alias="value_separator")
