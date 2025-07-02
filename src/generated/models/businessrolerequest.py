"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .business import BusinessFields


# Field literal type
BusinessRoleRequestField = Literal[
    "created_by",
    "created_time",
    "email",
    "expiration_time",
    "expiry_time",
    "finance_role",
    "id",
    "invite_link",
    "invited_user_type",
    "ip_role",
    "owner",
    "role",
    "status",
    "tasks",
    "updated_by",
    "updated_time",
]


class BusinessRoleRequestFields(BaseModel):
    """Pydantic model for BusinessRoleRequest fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    created_by: dict[str, Any] = Field(None, alias="created_by")
    created_time: datetime = Field(None, alias="created_time")
    email: str = Field(None, alias="email")
    expiration_time: datetime = Field(None, alias="expiration_time")
    expiry_time: datetime = Field(None, alias="expiry_time")
    finance_role: str = Field(None, alias="finance_role")
    id: str = Field(None, alias="id")
    invite_link: str = Field(None, alias="invite_link")
    invited_user_type: list[str] = Field(None, alias="invited_user_type")
    ip_role: str = Field(None, alias="ip_role")
    owner: BusinessFields = Field(None, alias="owner")
    role: str = Field(None, alias="role")
    status: str = Field(None, alias="status")
    tasks: list[str] = Field(None, alias="tasks")
    updated_by: dict[str, Any] = Field(None, alias="updated_by")
    updated_time: datetime = Field(None, alias="updated_time")
