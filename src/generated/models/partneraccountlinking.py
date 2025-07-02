"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .adaccount import AdAccountFields
    from .application import ApplicationFields
    from .business import BusinessFields


# Field literal type
PartnerAccountLinkingField = Literal[
    "adaccount",
    "app",
    "business",
    "externalidentifier",
    "externalidentifieruri",
    "id",
    "partnername",
    "pixel",
]


class PartnerAccountLinkingFields(BaseModel):
    """Pydantic model for PartnerAccountLinking fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    adaccount: AdAccountFields = Field(None, alias="adaccount")
    app: ApplicationFields = Field(None, alias="app")
    business: BusinessFields = Field(None, alias="business")
    externalidentifier: str = Field(None, alias="externalidentifier")
    externalidentifieruri: str = Field(None, alias="externalidentifieruri")
    id: str = Field(None, alias="id")
    partnername: str = Field(None, alias="partnername")
    pixel: str = Field(None, alias="pixel")
