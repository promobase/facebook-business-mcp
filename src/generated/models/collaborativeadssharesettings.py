"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .business import BusinessFields


# Field literal type
CollaborativeAdsShareSettingsField = Literal[
    "agency_business", "id", "product_catalog_proxy_id", "utm_campaign", "utm_medium", "utm_source"
]


class CollaborativeAdsShareSettingsFields(BaseModel):
    """Pydantic model for CollaborativeAdsShareSettings fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    agency_business: BusinessFields = Field(None, alias="agency_business")
    id: str = Field(None, alias="id")
    product_catalog_proxy_id: str = Field(None, alias="product_catalog_proxy_id")
    utm_campaign: str = Field(None, alias="utm_campaign")
    utm_medium: str = Field(None, alias="utm_medium")
    utm_source: str = Field(None, alias="utm_source")
