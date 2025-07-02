"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .user import UserFields


# Field literal type
AdExportPresetField = Literal["created_time", "fields", "id", "name", "owner", "updated_time"]


class AdExportPresetFields(BaseModel):
    """Pydantic model for AdExportPreset fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    created_time: datetime = Field(None, alias="created_time")
    fields: list[str] = Field(None, alias="fields")
    id: str = Field(None, alias="id")
    name: str = Field(None, alias="name")
    owner: UserFields = Field(None, alias="owner")
    updated_time: datetime = Field(None, alias="updated_time")
