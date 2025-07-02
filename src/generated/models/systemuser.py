"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .user import UserFields


# Field literal type
SystemUserField = Literal[
    "created_by", "created_time", "finance_permission", "id", "ip_permission", "name"
]


class SystemUserFields(BaseModel):
    """Pydantic model for SystemUser fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    created_by: UserFields = Field(None, alias="created_by")
    created_time: datetime = Field(None, alias="created_time")
    finance_permission: str = Field(None, alias="finance_permission")
    id: str = Field(None, alias="id")
    ip_permission: str = Field(None, alias="ip_permission")
    name: str = Field(None, alias="name")


class SystemUserGetAssignedBusinessAssetGroupsParams(BaseModel):
    """Parameters for SystemUser.get_assigned_business_asset_groups()."""

    model_config = ConfigDict(extra="forbid")
    contained_asset_id: str | None = Field(None, description="contained_asset_id parameter")


class SystemUserGetAssignedPagesParams(BaseModel):
    """Parameters for SystemUser.get_assigned_pages()."""

    model_config = ConfigDict(extra="forbid")
    pages: list[int] | None = Field(None, description="pages parameter")
