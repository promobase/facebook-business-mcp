"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .business import BusinessFields


# Field literal type
OwnedDomainField = Literal["domain_name", "id", "owner_business", "status", "verification_code"]


class OwnedDomainFields(BaseModel):
    """Pydantic model for OwnedDomain fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    domain_name: str = Field(None, alias="domain_name")
    id: str = Field(None, alias="id")
    owner_business: BusinessFields = Field(None, alias="owner_business")
    status: str = Field(None, alias="status")
    verification_code: str = Field(None, alias="verification_code")
