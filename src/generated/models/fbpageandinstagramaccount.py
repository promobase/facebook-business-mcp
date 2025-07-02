"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
FBPageAndInstagramAccountField = Literal[
    "ad_permissions", "bc_permission_status", "bc_permissions", "is_managed", "matched_by"
]


class FBPageAndInstagramAccountFields(BaseModel):
    """Pydantic model for FBPageAndInstagramAccount fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    ad_permissions: list[str] = Field(None, alias="ad_permissions")
    bc_permission_status: str = Field(None, alias="bc_permission_status")
    bc_permissions: list[dict[str, str]] = Field(None, alias="bc_permissions")
    is_managed: bool = Field(None, alias="is_managed")
    matched_by: str = Field(None, alias="matched_by")
