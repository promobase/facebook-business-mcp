"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
PageAppWithLeadsAccessField = Literal["can_access_leads", "type"]


class PageAppWithLeadsAccessFields(BaseModel):
    """Pydantic model for PageAppWithLeadsAccess fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    can_access_leads: bool = Field(None, alias="can_access_leads")
    type: str = Field(None, alias="type")
