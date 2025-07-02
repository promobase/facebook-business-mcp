"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
AdNetworkAnalyticsSyncQueryResultField = Literal["omitted_results", "query_id", "results"]


class AdNetworkAnalyticsSyncQueryResultFields(BaseModel):
    """Pydantic model for AdNetworkAnalyticsSyncQueryResult fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    omitted_results: list[dict[str, Any]] = Field(None, alias="omitted_results")
    query_id: str = Field(None, alias="query_id")
    results: list[dict[str, Any]] = Field(None, alias="results")
