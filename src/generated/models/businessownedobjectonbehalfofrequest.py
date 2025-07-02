"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .business import BusinessFields


# Field literal type
BusinessOwnedObjectOnBehalfOfRequestField = Literal[
    "business_owned_object", "id", "receiving_business", "requesting_business", "status"
]


class BusinessOwnedObjectOnBehalfOfRequestFields(BaseModel):
    """Pydantic model for BusinessOwnedObjectOnBehalfOfRequest fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    business_owned_object: str = Field(None, alias="business_owned_object")
    id: str = Field(None, alias="id")
    receiving_business: BusinessFields = Field(None, alias="receiving_business")
    requesting_business: BusinessFields = Field(None, alias="requesting_business")
    status: str = Field(None, alias="status")
