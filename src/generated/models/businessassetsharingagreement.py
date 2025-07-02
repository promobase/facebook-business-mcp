"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .business import BusinessFields


# Field literal type
BusinessAssetSharingAgreementField = Literal[
    "id", "initiator", "recipient", "relationship_type", "request_status", "request_type"
]


class BusinessAssetSharingAgreementFields(BaseModel):
    """Pydantic model for BusinessAssetSharingAgreement fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    id: str = Field(None, alias="id")
    initiator: BusinessFields = Field(None, alias="initiator")
    recipient: BusinessFields = Field(None, alias="recipient")
    relationship_type: list[str] = Field(None, alias="relationship_type")
    request_status: str = Field(None, alias="request_status")
    request_type: str = Field(None, alias="request_type")
