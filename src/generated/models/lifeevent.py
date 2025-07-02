"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .page import PageFields


# Field literal type
LifeEventField = Literal[
    "description", "end_time", "from", "id", "is_hidden", "start_time", "title", "updated_time"
]


class LifeEventFields(BaseModel):
    """Pydantic model for LifeEvent fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    description: str = Field(None, alias="description")
    end_time: datetime = Field(None, alias="end_time")
    from_: PageFields = Field(None, alias="from")
    id: str = Field(None, alias="id")
    is_hidden: bool = Field(None, alias="is_hidden")
    start_time: datetime = Field(None, alias="start_time")
    title: str = Field(None, alias="title")
    updated_time: datetime = Field(None, alias="updated_time")
