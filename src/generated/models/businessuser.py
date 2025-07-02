"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .business import BusinessFields
    from .businessrolerequest import BusinessRoleRequestFields


# Field literal type
BusinessUserField = Literal[
    "business",
    "business_role_request",
    "email",
    "finance_permission",
    "first_name",
    "id",
    "ip_permission",
    "last_name",
    "marked_for_removal",
    "name",
    "pending_email",
    "role",
    "tasks",
    "title",
    "two_fac_status",
]


class BusinessUserFields(BaseModel):
    """Pydantic model for BusinessUser fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    business: BusinessFields = Field(None, alias="business")
    business_role_request: BusinessRoleRequestFields = Field(None, alias="business_role_request")
    email: str = Field(None, alias="email")
    finance_permission: str = Field(None, alias="finance_permission")
    first_name: str = Field(None, alias="first_name")
    id: str = Field(None, alias="id")
    ip_permission: str = Field(None, alias="ip_permission")
    last_name: str = Field(None, alias="last_name")
    marked_for_removal: bool = Field(None, alias="marked_for_removal")
    name: str = Field(None, alias="name")
    pending_email: str = Field(None, alias="pending_email")
    role: str = Field(None, alias="role")
    tasks: list[str] = Field(None, alias="tasks")
    title: str = Field(None, alias="title")
    two_fac_status: str = Field(None, alias="two_fac_status")


class BusinessUserGetAssignedBusinessAssetGroupsParams(BaseModel):
    """Parameters for BusinessUser.get_assigned_business_asset_groups()."""

    model_config = ConfigDict(extra="forbid")
    contained_asset_id: str | None = Field(None, description="contained_asset_id parameter")


class BusinessUserGetAssignedPagesParams(BaseModel):
    """Parameters for BusinessUser.get_assigned_pages()."""

    model_config = ConfigDict(extra="forbid")
    pages: list[int] | None = Field(None, description="pages parameter")
