"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
AnalyticsFunnelQueryResultField = Literal["query_id", "status"]


class AnalyticsFunnelQueryResultFields(BaseModel):
    """Pydantic model for AnalyticsFunnelQueryResult fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    query_id: str = Field(None, alias="query_id")
    status: str = Field(None, alias="status")
