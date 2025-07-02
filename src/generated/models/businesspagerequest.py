"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .page import PageFields


# Field literal type
BusinessPageRequestField = Literal["id", "page"]


class BusinessPageRequestFields(BaseModel):
    """Pydantic model for BusinessPageRequest fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    id: str = Field(None, alias="id")
    page: PageFields = Field(None, alias="page")
