"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .business import BusinessFields


# Field literal type
OffsiteSignalContainerBusinessObjectField = Literal[
    "business",
    "id",
    "is_eligible_for_sharing_to_ad_account",
    "is_eligible_for_sharing_to_business",
    "is_unavailable",
    "name",
    "primary_container_id",
]


class OffsiteSignalContainerBusinessObjectFields(BaseModel):
    """Pydantic model for OffsiteSignalContainerBusinessObject fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    business: BusinessFields = Field(None, alias="business")
    id: str = Field(None, alias="id")
    is_eligible_for_sharing_to_ad_account: bool = Field(
        None, alias="is_eligible_for_sharing_to_ad_account"
    )
    is_eligible_for_sharing_to_business: bool = Field(
        None, alias="is_eligible_for_sharing_to_business"
    )
    is_unavailable: bool = Field(None, alias="is_unavailable")
    name: str = Field(None, alias="name")
    primary_container_id: str = Field(None, alias="primary_container_id")
