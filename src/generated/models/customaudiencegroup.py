"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
CustomAudienceGroupField = Literal[
    "audience_type_param_name", "existing_customer_tag", "new_customer_tag"
]


class CustomAudienceGroupFields(BaseModel):
    """Pydantic model for CustomAudienceGroup fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    audience_type_param_name: str = Field(None, alias="audience_type_param_name")
    existing_customer_tag: str = Field(None, alias="existing_customer_tag")
    new_customer_tag: str = Field(None, alias="new_customer_tag")
