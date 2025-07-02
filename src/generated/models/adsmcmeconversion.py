"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
AdsMcmeConversionField = Literal[
    "creation_time",
    "description",
    "id",
    "is_archived",
    "mcme_conversion_type",
    "name",
    "omnichannel_object_id",
]


class AdsMcmeConversionFields(BaseModel):
    """Pydantic model for AdsMcmeConversion fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    creation_time: datetime = Field(None, alias="creation_time")
    description: str = Field(None, alias="description")
    id: str = Field(None, alias="id")
    is_archived: bool = Field(None, alias="is_archived")
    mcme_conversion_type: str = Field(None, alias="mcme_conversion_type")
    name: str = Field(None, alias="name")
    omnichannel_object_id: str = Field(None, alias="omnichannel_object_id")
