"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .page import PageFields


# Field literal type
PlaceTagField = Literal["created_time", "id", "place"]


class PlaceTagFields(BaseModel):
    """Pydantic model for PlaceTag fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    created_time: datetime = Field(None, alias="created_time")
    id: str = Field(None, alias="id")
    place: PageFields = Field(None, alias="place")
