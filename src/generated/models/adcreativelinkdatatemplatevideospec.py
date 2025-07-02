"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
AdCreativeLinkDataTemplateVideoSpecField = Literal[
    "categorization_criteria", "customization", "template_id"
]


class AdCreativeLinkDataTemplateVideoSpecFields(BaseModel):
    """Pydantic model for AdCreativeLinkDataTemplateVideoSpec fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    categorization_criteria: str = Field(None, alias="categorization_criteria")
    customization: list[dict[str, str]] = Field(None, alias="customization")
    template_id: str = Field(None, alias="template_id")
