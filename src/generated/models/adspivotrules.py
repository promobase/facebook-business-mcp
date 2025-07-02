"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .profile import ProfileFields


# Field literal type
AdsPivotRulesField = Literal[
    "creation_time",
    "creator",
    "description",
    "id",
    "name",
    "permission",
    "rules",
    "scope",
    "update_by",
    "update_time",
]


class AdsPivotRulesFields(BaseModel):
    """Pydantic model for AdsPivotRules fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    creation_time: datetime = Field(None, alias="creation_time")
    creator: ProfileFields = Field(None, alias="creator")
    description: str = Field(None, alias="description")
    id: str = Field(None, alias="id")
    name: str = Field(None, alias="name")
    permission: str = Field(None, alias="permission")
    rules: list[dict[str, Any]] = Field(None, alias="rules")
    scope: str = Field(None, alias="scope")
    update_by: ProfileFields = Field(None, alias="update_by")
    update_time: datetime = Field(None, alias="update_time")
