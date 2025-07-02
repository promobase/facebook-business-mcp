"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
BusinessProductCatalogTOSField = Literal["accepted", "content"]


class BusinessProductCatalogTOSFields(BaseModel):
    """Pydantic model for BusinessProductCatalogTOS fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    accepted: bool = Field(None, alias="accepted")
    content: str = Field(None, alias="content")
