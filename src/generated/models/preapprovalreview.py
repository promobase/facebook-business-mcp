"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
PreapprovalReviewField = Literal[
    "comp_type", "crow_component_id", "is_human_reviewed", "is_reviewed", "policy_info"
]


class PreapprovalReviewFields(BaseModel):
    """Pydantic model for PreapprovalReview fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    comp_type: str = Field(None, alias="comp_type")
    crow_component_id: int = Field(None, alias="crow_component_id")
    is_human_reviewed: bool = Field(None, alias="is_human_reviewed")
    is_reviewed: bool = Field(None, alias="is_reviewed")
    policy_info: list[dict[str, dict[str, Any]]] = Field(None, alias="policy_info")
