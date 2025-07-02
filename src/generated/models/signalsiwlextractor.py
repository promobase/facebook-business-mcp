"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
SignalsIWLExtractorField = Literal["domain_uri", "event_type", "extractor_type", "id"]


class SignalsIWLExtractorFields(BaseModel):
    """Pydantic model for SignalsIWLExtractor fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    domain_uri: str = Field(None, alias="domain_uri")
    event_type: str = Field(None, alias="event_type")
    extractor_type: str = Field(None, alias="extractor_type")
    id: str = Field(None, alias="id")
