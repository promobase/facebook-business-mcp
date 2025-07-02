"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .imagecopyright import ImageCopyrightFields
    from .profile import ProfileFields


# Field literal type
ImageReferenceMatchField = Literal[
    "conflicting_countries",
    "country_resolution_history",
    "creation_time",
    "current_conflict_resolved_countries",
    "displayed_match_state",
    "dispute_form_data_entries_with_translations",
    "expiration_time",
    "id",
    "match_state",
    "matched_reference_copyright",
    "matched_reference_owner",
    "modification_history",
    "reference_copyright",
    "reference_owner",
    "rejection_form_data_entries_with_translations",
    "resolution_reason",
    "update_time",
]


class ImageReferenceMatchFields(BaseModel):
    """Pydantic model for ImageReferenceMatch fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

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
    match_state: str = Field(None, alias="match_state")
    matched_reference_copyright: ImageCopyrightFields = Field(
        None, alias="matched_reference_copyright"
    )
    matched_reference_owner: ProfileFields = Field(None, alias="matched_reference_owner")
    modification_history: list[dict[str, Any]] = Field(None, alias="modification_history")
    reference_copyright: ImageCopyrightFields = Field(None, alias="reference_copyright")
    reference_owner: ProfileFields = Field(None, alias="reference_owner")
    rejection_form_data_entries_with_translations: list[dict[str, Any]] = Field(
        None, alias="rejection_form_data_entries_with_translations"
    )
    resolution_reason: str = Field(None, alias="resolution_reason")
    update_time: datetime = Field(None, alias="update_time")
