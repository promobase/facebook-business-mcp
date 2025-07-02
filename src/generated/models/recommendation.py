"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .user import UserFields


# Field literal type
RecommendationField = Literal[
    "created_time",
    "has_rating",
    "has_review",
    "open_graph_story",
    "rating",
    "recommendation_type",
    "review_text",
    "reviewer",
]


class RecommendationFields(BaseModel):
    """Pydantic model for Recommendation fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    created_time: datetime = Field(None, alias="created_time")
    has_rating: bool = Field(None, alias="has_rating")
    has_review: bool = Field(None, alias="has_review")
    open_graph_story: dict[str, Any] = Field(None, alias="open_graph_story")
    rating: int = Field(None, alias="rating")
    recommendation_type: str = Field(None, alias="recommendation_type")
    review_text: str = Field(None, alias="review_text")
    reviewer: UserFields = Field(None, alias="reviewer")
