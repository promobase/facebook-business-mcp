"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
WebPublisherField = Literal["domain_url", "id", "publisher_name"]


class WebPublisherFields(BaseModel):
    """Pydantic model for WebPublisher fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    domain_url: str = Field(None, alias="domain_url")
    id: str = Field(None, alias="id")
    publisher_name: str = Field(None, alias="publisher_name")
