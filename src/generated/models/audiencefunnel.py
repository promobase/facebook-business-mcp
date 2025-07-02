"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
AudienceFunnelField = Literal[
    "audience_type_param_name", "audience_type_param_tags", "custom_audience_groups_info"
]


class AudienceFunnelFields(BaseModel):
    """Pydantic model for AudienceFunnel fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    audience_type_param_name: str = Field(None, alias="audience_type_param_name")
    audience_type_param_tags: list[dict[str, str]] = Field(None, alias="audience_type_param_tags")
    custom_audience_groups_info: list[dict[str, list[str]]] = Field(
        None, alias="custom_audience_groups_info"
    )
