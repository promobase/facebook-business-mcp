"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
PageUserWithLeadsAccessField = Literal[
    "active_on_business", "business_role", "can_access_leads", "page_role"
]


class PageUserWithLeadsAccessFields(BaseModel):
    """Pydantic model for PageUserWithLeadsAccess fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    active_on_business: bool = Field(None, alias="active_on_business")
    business_role: str = Field(None, alias="business_role")
    can_access_leads: bool = Field(None, alias="can_access_leads")
    page_role: str = Field(None, alias="page_role")
