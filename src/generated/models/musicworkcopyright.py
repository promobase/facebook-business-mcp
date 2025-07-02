"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .videocopyrightrule import VideoCopyrightRuleFields


# Field literal type
MusicWorkCopyrightField = Literal[
    "available_ui_actions",
    "claim_status",
    "creation_time",
    "displayed_fb_matches_count",
    "displayed_ig_matches_count",
    "displayed_matches_count",
    "has_rev_share_eligible_isrcs",
    "id",
    "is_linking_required_to_monetize_for_manual_claim",
    "match_rule",
    "status",
    "tags",
    "update_time",
]


class MusicWorkCopyrightFields(BaseModel):
    """Pydantic model for MusicWorkCopyright fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    available_ui_actions: list[str] = Field(None, alias="available_ui_actions")
    claim_status: str = Field(None, alias="claim_status")
    creation_time: datetime = Field(None, alias="creation_time")
    displayed_fb_matches_count: int = Field(None, alias="displayed_fb_matches_count")
    displayed_ig_matches_count: int = Field(None, alias="displayed_ig_matches_count")
    displayed_matches_count: int = Field(None, alias="displayed_matches_count")
    has_rev_share_eligible_isrcs: bool = Field(None, alias="has_rev_share_eligible_isrcs")
    id: str = Field(None, alias="id")
    is_linking_required_to_monetize_for_manual_claim: bool = Field(
        None, alias="is_linking_required_to_monetize_for_manual_claim"
    )
    match_rule: VideoCopyrightRuleFields = Field(None, alias="match_rule")
    status: str = Field(None, alias="status")
    tags: list[str] = Field(None, alias="tags")
    update_time: datetime = Field(None, alias="update_time")
