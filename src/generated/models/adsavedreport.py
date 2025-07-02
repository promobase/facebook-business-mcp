"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .application import ApplicationFields
    from .user import UserFields


# Field literal type
AdSavedReportField = Literal[
    "app_owner",
    "breakdowns",
    "builtin_column_set",
    "creation_source",
    "date_interval",
    "date_preset",
    "format_version",
    "id",
    "insights_section",
    "is_shared_unread",
    "level",
    "name",
    "normalized_filter",
    "sort",
    "user_attribution_windows",
    "user_columns",
    "user_filter",
    "user_owner",
]


class AdSavedReportFields(BaseModel):
    """Pydantic model for AdSavedReport fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    app_owner: ApplicationFields = Field(None, alias="app_owner")
    breakdowns: list[str] = Field(None, alias="breakdowns")
    builtin_column_set: str = Field(None, alias="builtin_column_set")
    creation_source: str = Field(None, alias="creation_source")
    date_interval: dict[str, Any] = Field(None, alias="date_interval")
    date_preset: str = Field(None, alias="date_preset")
    format_version: int = Field(None, alias="format_version")
    id: str = Field(None, alias="id")
    insights_section: dict[str, Any] = Field(None, alias="insights_section")
    is_shared_unread: bool = Field(None, alias="is_shared_unread")
    level: str = Field(None, alias="level")
    name: str = Field(None, alias="name")
    normalized_filter: dict[str, Any] = Field(None, alias="normalized_filter")
    sort: list[dict[str, Any]] = Field(None, alias="sort")
    user_attribution_windows: list[str] = Field(None, alias="user_attribution_windows")
    user_columns: list[str] = Field(None, alias="user_columns")
    user_filter: dict[str, Any] = Field(None, alias="user_filter")
    user_owner: UserFields = Field(None, alias="user_owner")
