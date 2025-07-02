"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
AdAccountTargetingUnifiedField = Literal[
    "audience_size_lower_bound",
    "audience_size_upper_bound",
    "conversion_lift",
    "description",
    "id",
    "img",
    "info",
    "info_title",
    "is_recommendation",
    "key",
    "link",
    "name",
    "parent",
    "partner",
    "path",
    "performance_rating",
    "raw_name",
    "recommendation_model",
    "search_interest_id",
    "source",
    "spend",
    "type",
    "valid",
]


class AdAccountTargetingUnifiedFields(BaseModel):
    """Pydantic model for AdAccountTargetingUnified fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    audience_size_lower_bound: int = Field(None, alias="audience_size_lower_bound")
    audience_size_upper_bound: int = Field(None, alias="audience_size_upper_bound")
    conversion_lift: float = Field(None, alias="conversion_lift")
    description: str = Field(None, alias="description")
    id: str = Field(None, alias="id")
    img: str = Field(None, alias="img")
    info: str = Field(None, alias="info")
    info_title: str = Field(None, alias="info_title")
    is_recommendation: bool = Field(None, alias="is_recommendation")
    key: str = Field(None, alias="key")
    link: str = Field(None, alias="link")
    name: str = Field(None, alias="name")
    parent: str = Field(None, alias="parent")
    partner: str = Field(None, alias="partner")
    path: list[str] = Field(None, alias="path")
    performance_rating: int = Field(None, alias="performance_rating")
    raw_name: str = Field(None, alias="raw_name")
    recommendation_model: str = Field(None, alias="recommendation_model")
    search_interest_id: str = Field(None, alias="search_interest_id")
    source: str = Field(None, alias="source")
    spend: float = Field(None, alias="spend")
    type: str = Field(None, alias="type")
    valid: bool = Field(None, alias="valid")
