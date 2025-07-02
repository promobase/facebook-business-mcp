"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .business import BusinessFields


# Field literal type
BusinessProjectField = Literal["business", "created_time", "creator", "id", "name"]


class BusinessProjectFields(BaseModel):
    """Pydantic model for BusinessProject fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    business: BusinessFields = Field(None, alias="business")
    created_time: datetime = Field(None, alias="created_time")
    creator: dict[str, Any] = Field(None, alias="creator")
    id: str = Field(None, alias="id")
    name: str = Field(None, alias="name")
