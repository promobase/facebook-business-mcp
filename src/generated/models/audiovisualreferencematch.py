"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .profile import ProfileFields


# Field literal type
AudioVisualReferenceMatchField = Literal[
    "audio_conflicting_segments",
    "audio_current_conflict_resolved_segments",
    "audio_segment_resolution_history",
    "conflict_status",
    "conflict_type",
    "conflicting_countries",
    "country_resolution_history",
    "creation_time",
    "current_conflict_resolved_countries",
    "displayed_match_state",
    "dispute_form_data_entries_with_translations",
    "expiration_time",
    "id",
    "is_disputable",
    "match_state",
    "matched_overlap_percentage",
    "matched_owner_match_duration_in_sec",
    "matched_reference_owner",
    "modification_history",
    "num_matches_on_matched_side",
    "num_matches_on_ref_side",
    "ref_owner_match_duration_in_sec",
    "reference_overlap_percentage",
    "reference_owner",
    "rejection_form_data_entries_with_translations",
    "resolution_details",
    "resolution_reason",
    "update_time",
    "views_on_matched_side",
    "visual_conflicting_segments",
    "visual_current_conflict_resolved_segments",
    "visual_segment_resolution_history",
]


class AudioVisualReferenceMatchFields(BaseModel):
    """Pydantic model for AudioVisualReferenceMatch fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    audio_conflicting_segments: list[dict[str, Any]] = Field(
        None, alias="audio_conflicting_segments"
    )
    audio_current_conflict_resolved_segments: list[dict[str, Any]] = Field(
        None, alias="audio_current_conflict_resolved_segments"
    )
    audio_segment_resolution_history: list[dict[str, Any]] = Field(
        None, alias="audio_segment_resolution_history"
    )
    conflict_status: str = Field(None, alias="conflict_status")
    conflict_type: str = Field(None, alias="conflict_type")
    conflicting_countries: list[str] = Field(None, alias="conflicting_countries")
    country_resolution_history: list[dict[str, list[dict[str, Any]]]] = Field(
        None, alias="country_resolution_history"
    )
    creation_time: datetime = Field(None, alias="creation_time")
    current_conflict_resolved_countries: list[dict[str, dict[str, Any]]] = Field(
        None, alias="current_conflict_resolved_countries"
    )
    displayed_match_state: str = Field(None, alias="displayed_match_state")
    dispute_form_data_entries_with_translations: list[dict[str, Any]] = Field(
        None, alias="dispute_form_data_entries_with_translations"
    )
    expiration_time: datetime = Field(None, alias="expiration_time")
    id: str = Field(None, alias="id")
    is_disputable: bool = Field(None, alias="is_disputable")
    match_state: str = Field(None, alias="match_state")
    matched_overlap_percentage: float = Field(None, alias="matched_overlap_percentage")
    matched_owner_match_duration_in_sec: float = Field(
        None, alias="matched_owner_match_duration_in_sec"
    )
    matched_reference_owner: ProfileFields = Field(None, alias="matched_reference_owner")
    modification_history: list[dict[str, Any]] = Field(None, alias="modification_history")
    num_matches_on_matched_side: int = Field(None, alias="num_matches_on_matched_side")
    num_matches_on_ref_side: int = Field(None, alias="num_matches_on_ref_side")
    ref_owner_match_duration_in_sec: float = Field(None, alias="ref_owner_match_duration_in_sec")
    reference_overlap_percentage: float = Field(None, alias="reference_overlap_percentage")
    reference_owner: ProfileFields = Field(None, alias="reference_owner")
    rejection_form_data_entries_with_translations: list[dict[str, Any]] = Field(
        None, alias="rejection_form_data_entries_with_translations"
    )
    resolution_details: str = Field(None, alias="resolution_details")
    resolution_reason: str = Field(None, alias="resolution_reason")
    update_time: datetime = Field(None, alias="update_time")
    views_on_matched_side: int = Field(None, alias="views_on_matched_side")
    visual_conflicting_segments: list[dict[str, Any]] = Field(
        None, alias="visual_conflicting_segments"
    )
    visual_current_conflict_resolved_segments: list[dict[str, Any]] = Field(
        None, alias="visual_current_conflict_resolved_segments"
    )
    visual_segment_resolution_history: list[dict[str, Any]] = Field(
        None, alias="visual_segment_resolution_history"
    )
