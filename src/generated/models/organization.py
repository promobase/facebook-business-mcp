"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .business import BusinessFields


# Field literal type
OrganizationField = Literal["id", "legal_entity_name", "owner_business"]


class OrganizationFields(BaseModel):
    """Pydantic model for Organization fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    id: str = Field(None, alias="id")
    legal_entity_name: str = Field(None, alias="legal_entity_name")
    owner_business: BusinessFields = Field(None, alias="owner_business")
