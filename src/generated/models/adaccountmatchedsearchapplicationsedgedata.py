"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
AdAccountMatchedSearchApplicationsEdgeDataField = Literal[
    "app_id",
    "are_app_events_unavailable",
    "icon_url",
    "name",
    "search_source_store",
    "store",
    "unique_id",
    "url",
]


class AdAccountMatchedSearchApplicationsEdgeDataFields(BaseModel):
    """Pydantic model for AdAccountMatchedSearchApplicationsEdgeData fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    app_id: str = Field(None, alias="app_id")
    are_app_events_unavailable: bool = Field(None, alias="are_app_events_unavailable")
    icon_url: str = Field(None, alias="icon_url")
    name: str = Field(None, alias="name")
    search_source_store: str = Field(None, alias="search_source_store")
    store: str = Field(None, alias="store")
    unique_id: str = Field(None, alias="unique_id")
    url: str = Field(None, alias="url")
