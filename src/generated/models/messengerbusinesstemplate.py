"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
MessengerBusinessTemplateField = Literal[
    "category",
    "components",
    "creation_time",
    "id",
    "language",
    "language_count",
    "last_updated_time",
    "library_template_name",
    "name",
    "rejected_reason",
    "rejection_reasons",
    "specific_rejection_reasons",
    "status",
]


class MessengerBusinessTemplateFields(BaseModel):
    """Pydantic model for MessengerBusinessTemplate fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    category: str = Field(None, alias="category")
    components: list[dict[str, Any]] = Field(None, alias="components")
    creation_time: int = Field(None, alias="creation_time")
    id: str = Field(None, alias="id")
    language: str = Field(None, alias="language")
    language_count: int = Field(None, alias="language_count")
    last_updated_time: datetime = Field(None, alias="last_updated_time")
    library_template_name: str = Field(None, alias="library_template_name")
    name: str = Field(None, alias="name")
    rejected_reason: str = Field(None, alias="rejected_reason")
    rejection_reasons: dict[str, Any] = Field(None, alias="rejection_reasons")
    specific_rejection_reasons: dict[str, Any] = Field(None, alias="specific_rejection_reasons")
    status: str = Field(None, alias="status")
