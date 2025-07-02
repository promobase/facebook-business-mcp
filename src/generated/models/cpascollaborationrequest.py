"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .business import BusinessFields


# Field literal type
CPASCollaborationRequestField = Literal[
    "brands",
    "contact_email",
    "contact_first_name",
    "contact_last_name",
    "id",
    "phone_number",
    "receiver_business",
    "requester_agency_or_brand",
    "sender_client_business",
    "status",
]


class CPASCollaborationRequestFields(BaseModel):
    """Pydantic model for CPASCollaborationRequest fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    brands: list[str] = Field(None, alias="brands")
    contact_email: str = Field(None, alias="contact_email")
    contact_first_name: str = Field(None, alias="contact_first_name")
    contact_last_name: str = Field(None, alias="contact_last_name")
    id: str = Field(None, alias="id")
    phone_number: str = Field(None, alias="phone_number")
    receiver_business: BusinessFields = Field(None, alias="receiver_business")
    requester_agency_or_brand: str = Field(None, alias="requester_agency_or_brand")
    sender_client_business: BusinessFields = Field(None, alias="sender_client_business")
    status: str = Field(None, alias="status")
