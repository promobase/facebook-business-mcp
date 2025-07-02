"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .business import BusinessFields


# Field literal type
PagePartnerWithLeadsAccessField = Literal["can_access_leads", "partner_business", "permitted_tasks"]


class PagePartnerWithLeadsAccessFields(BaseModel):
    """Pydantic model for PagePartnerWithLeadsAccess fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    can_access_leads: bool = Field(None, alias="can_access_leads")
    partner_business: BusinessFields = Field(None, alias="partner_business")
    permitted_tasks: list[str] = Field(None, alias="permitted_tasks")
