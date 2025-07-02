"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .user import UserFields


# Field literal type
MediaCopyrightUpdateRecordField = Literal[
    "action_types",
    "actor",
    "actor_type",
    "creation_time",
    "id",
    "ownership_countries",
    "whitelisted_accounts",
]


class MediaCopyrightUpdateRecordFields(BaseModel):
    """Pydantic model for MediaCopyrightUpdateRecord fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    action_types: list[str] = Field(None, alias="action_types")
    actor: UserFields = Field(None, alias="actor")
    actor_type: str = Field(None, alias="actor_type")
    creation_time: datetime = Field(None, alias="creation_time")
    id: str = Field(None, alias="id")
    ownership_countries: list[dict[str, Any]] = Field(None, alias="ownership_countries")
    whitelisted_accounts: list[dict[str, Any]] = Field(None, alias="whitelisted_accounts")
