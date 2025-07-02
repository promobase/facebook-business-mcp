"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .business import BusinessFields
    from .profile import ProfileFields


# Field literal type
AdCustomDerivedMetricsField = Literal[
    "ad_account_id",
    "business",
    "creation_time",
    "creator",
    "custom_derived_metric_type",
    "deletion_time",
    "deletor",
    "description",
    "format_type",
    "formula",
    "has_attribution_windows",
    "has_inline_attribution_window",
    "id",
    "name",
    "permission",
    "saved_report_id",
    "scope",
]


class AdCustomDerivedMetricsFields(BaseModel):
    """Pydantic model for AdCustomDerivedMetrics fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    ad_account_id: str = Field(None, alias="ad_account_id")
    business: BusinessFields = Field(None, alias="business")
    creation_time: datetime = Field(None, alias="creation_time")
    creator: ProfileFields = Field(None, alias="creator")
    custom_derived_metric_type: str = Field(None, alias="custom_derived_metric_type")
    deletion_time: datetime = Field(None, alias="deletion_time")
    deletor: ProfileFields = Field(None, alias="deletor")
    description: str = Field(None, alias="description")
    format_type: str = Field(None, alias="format_type")
    formula: str = Field(None, alias="formula")
    has_attribution_windows: bool = Field(None, alias="has_attribution_windows")
    has_inline_attribution_window: bool = Field(None, alias="has_inline_attribution_window")
    id: str = Field(None, alias="id")
    name: str = Field(None, alias="name")
    permission: str = Field(None, alias="permission")
    saved_report_id: str = Field(None, alias="saved_report_id")
    scope: str = Field(None, alias="scope")
