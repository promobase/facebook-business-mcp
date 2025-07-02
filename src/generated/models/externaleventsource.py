"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
ExternalEventSourceField = Literal["id", "name", "source_type"]


class ExternalEventSourceFields(BaseModel):
    """Pydantic model for ExternalEventSource fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    id: str = Field(None, alias="id")
    name: str = Field(None, alias="name")
    source_type: str = Field(None, alias="source_type")
