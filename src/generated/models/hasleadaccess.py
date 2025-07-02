"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
HasLeadAccessField = Literal[
    "app_has_leads_permission",
    "can_access_lead",
    "enabled_lead_access_manager",
    "failure_reason",
    "failure_resolution",
    "is_page_admin",
    "page_id",
    "user_has_leads_permission",
    "user_id",
]


class HasLeadAccessFields(BaseModel):
    """Pydantic model for HasLeadAccess fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    app_has_leads_permission: bool = Field(None, alias="app_has_leads_permission")
    can_access_lead: bool = Field(None, alias="can_access_lead")
    enabled_lead_access_manager: bool = Field(None, alias="enabled_lead_access_manager")
    failure_reason: str = Field(None, alias="failure_reason")
    failure_resolution: str = Field(None, alias="failure_resolution")
    is_page_admin: bool = Field(None, alias="is_page_admin")
    page_id: str = Field(None, alias="page_id")
    user_has_leads_permission: bool = Field(None, alias="user_has_leads_permission")
    user_id: str = Field(None, alias="user_id")
