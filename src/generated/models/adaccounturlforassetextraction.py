"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
AdAccountURLForAssetExtractionField = Literal["source_type", "source_url"]


class AdAccountURLForAssetExtractionFields(BaseModel):
    """Pydantic model for AdAccountURLForAssetExtraction fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    source_type: str = Field(None, alias="source_type")
    source_url: str = Field(None, alias="source_url")
