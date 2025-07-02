"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
IGProductTaggingInvalidationErrorField = Literal["description", "taggability_state", "title"]


class IGProductTaggingInvalidationErrorFields(BaseModel):
    """Pydantic model for IGProductTaggingInvalidationError fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    description: str = Field(None, alias="description")
    taggability_state: str = Field(None, alias="taggability_state")
    title: str = Field(None, alias="title")
