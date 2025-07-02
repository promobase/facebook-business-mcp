"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .business import BusinessFields
    from .businessassetgroup import BusinessAssetGroupFields


# Field literal type
BusinessFranchiseConfigField = Literal[
    "active_partner_count",
    "agency_business",
    "agency_business_asset_group",
    "brand_name",
    "business",
    "business_vertical",
    "id",
    "partner_count",
    "pending_agency_business",
    "program_count",
    "shared_business_asset_group",
    "shared_creative_folder_count",
    "shared_custom_audience_count",
]


class BusinessFranchiseConfigFields(BaseModel):
    """Pydantic model for BusinessFranchiseConfig fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    active_partner_count: int = Field(None, alias="active_partner_count")
    agency_business: BusinessFields = Field(None, alias="agency_business")
    agency_business_asset_group: BusinessAssetGroupFields = Field(
        None, alias="agency_business_asset_group"
    )
    brand_name: str = Field(None, alias="brand_name")
    business: BusinessFields = Field(None, alias="business")
    business_vertical: str = Field(None, alias="business_vertical")
    id: str = Field(None, alias="id")
    partner_count: int = Field(None, alias="partner_count")
    pending_agency_business: str = Field(None, alias="pending_agency_business")
    program_count: int = Field(None, alias="program_count")
    shared_business_asset_group: BusinessAssetGroupFields = Field(
        None, alias="shared_business_asset_group"
    )
    shared_creative_folder_count: int = Field(None, alias="shared_creative_folder_count")
    shared_custom_audience_count: int = Field(None, alias="shared_custom_audience_count")
