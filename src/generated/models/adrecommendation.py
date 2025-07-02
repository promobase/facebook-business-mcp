"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .adrecommendationdata import AdRecommendationDataFields


class AdRecommendation_confidence(str, Enum):
    """AdRecommendation_confidence enum values."""

    HIGH = "HIGH"
    LOW = "LOW"
    MEDIUM = "MEDIUM"


class AdRecommendation_importance(str, Enum):
    """AdRecommendation_importance enum values."""

    HIGH = "HIGH"
    LOW = "LOW"
    MEDIUM = "MEDIUM"


# Field literal type
AdRecommendationField = Literal[
    "blame_field",
    "code",
    "confidence",
    "importance",
    "message",
    "recommendation_data",
    "title",
    "value",
]


class AdRecommendationFields(BaseModel):
    """Pydantic model for AdRecommendation fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    blame_field: str = Field(None, alias="blame_field")
    code: int = Field(None, alias="code")
    confidence: dict[str, Any] = Field(None, alias="confidence")
    importance: dict[str, Any] = Field(None, alias="importance")
    message: str = Field(None, alias="message")
    recommendation_data: AdRecommendationDataFields = Field(None, alias="recommendation_data")
    title: str = Field(None, alias="title")
    value: str = Field(None, alias="value")
