"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .user import UserFields
    from .videocopyrightconditiongroup import VideoCopyrightConditionGroupFields


# Field literal type
VideoCopyrightRuleField = Literal[
    "condition_groups", "copyrights", "created_date", "creator", "id", "is_in_migration", "name"
]


class VideoCopyrightRuleFields(BaseModel):
    """Pydantic model for VideoCopyrightRule fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    condition_groups: list[VideoCopyrightConditionGroupFields] = Field(
        None, alias="condition_groups"
    )
    copyrights: list[str] = Field(None, alias="copyrights")
    created_date: datetime = Field(None, alias="created_date")
    creator: UserFields = Field(None, alias="creator")
    id: str = Field(None, alias="id")
    is_in_migration: bool = Field(None, alias="is_in_migration")
    name: str = Field(None, alias="name")
