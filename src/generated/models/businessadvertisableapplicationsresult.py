"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .business import BusinessFields


# Field literal type
BusinessAdvertisableApplicationsResultField = Literal[
    "are_app_events_unavailable", "business", "has_insight_permission", "id", "name", "photo_url"
]


class BusinessAdvertisableApplicationsResultFields(BaseModel):
    """Pydantic model for BusinessAdvertisableApplicationsResult fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    are_app_events_unavailable: bool = Field(None, alias="are_app_events_unavailable")
    business: BusinessFields = Field(None, alias="business")
    has_insight_permission: bool = Field(None, alias="has_insight_permission")
    id: str = Field(None, alias="id")
    name: str = Field(None, alias="name")
    photo_url: str = Field(None, alias="photo_url")
