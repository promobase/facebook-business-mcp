"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .business import BusinessFields


# Field literal type
BusinessObjectTransferOwnershipAgreementField = Literal[
    "id", "receiving_business", "requesting_business", "status"
]


class BusinessObjectTransferOwnershipAgreementFields(BaseModel):
    """Pydantic model for BusinessObjectTransferOwnershipAgreement fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    id: str = Field(None, alias="id")
    receiving_business: BusinessFields = Field(None, alias="receiving_business")
    requesting_business: BusinessFields = Field(None, alias="requesting_business")
    status: str = Field(None, alias="status")
