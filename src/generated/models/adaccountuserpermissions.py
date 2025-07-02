"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .business import BusinessFields
    from .user import UserFields


# Field literal type
AdAccountUserPermissionsField = Literal[
    "business",
    "business_persona",
    "created_by",
    "created_time",
    "email",
    "status",
    "tasks",
    "updated_by",
    "updated_time",
    "user",
]


class AdAccountUserPermissionsFields(BaseModel):
    """Pydantic model for AdAccountUserPermissions fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    business: BusinessFields = Field(None, alias="business")
    business_persona: dict[str, Any] = Field(None, alias="business_persona")
    created_by: UserFields = Field(None, alias="created_by")
    created_time: datetime = Field(None, alias="created_time")
    email: str = Field(None, alias="email")
    status: str = Field(None, alias="status")
    tasks: list[str] = Field(None, alias="tasks")
    updated_by: UserFields = Field(None, alias="updated_by")
    updated_time: datetime = Field(None, alias="updated_time")
    user: UserFields = Field(None, alias="user")
