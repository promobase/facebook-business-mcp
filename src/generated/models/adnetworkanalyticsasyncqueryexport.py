"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
AdNetworkAnalyticsAsyncQueryExportField = Literal["export_link", "query_id", "status"]


class AdNetworkAnalyticsAsyncQueryExportFields(BaseModel):
    """Pydantic model for AdNetworkAnalyticsAsyncQueryExport fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    export_link: str = Field(None, alias="export_link")
    query_id: str = Field(None, alias="query_id")
    status: str = Field(None, alias="status")
