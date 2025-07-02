"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
CatalogCollectionField = Literal["description", "title", "url"]


class CatalogCollectionFields(BaseModel):
    """Pydantic model for CatalogCollection fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    description: str = Field(None, alias="description")
    title: str = Field(None, alias="title")
    url: str = Field(None, alias="url")
