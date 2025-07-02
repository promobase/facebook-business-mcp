"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .business import BusinessFields
    from .businessassetgroup import BusinessAssetGroupFields
    from .customaudience import CustomAudienceFields


# Field literal type
FranchiseProgramField = Literal[
    "business_asset_group",
    "creator_business",
    "description",
    "end_date",
    "id",
    "name",
    "program_access_type",
    "program_approval_type",
    "program_image_link",
    "program_url",
    "shared_custom_audience",
    "start_date",
]


class FranchiseProgramFields(BaseModel):
    """Pydantic model for FranchiseProgram fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    business_asset_group: BusinessAssetGroupFields = Field(None, alias="business_asset_group")
    creator_business: BusinessFields = Field(None, alias="creator_business")
    description: str = Field(None, alias="description")
    end_date: datetime = Field(None, alias="end_date")
    id: str = Field(None, alias="id")
    name: str = Field(None, alias="name")
    program_access_type: str = Field(None, alias="program_access_type")
    program_approval_type: str = Field(None, alias="program_approval_type")
    program_image_link: str = Field(None, alias="program_image_link")
    program_url: str = Field(None, alias="program_url")
    shared_custom_audience: CustomAudienceFields = Field(None, alias="shared_custom_audience")
    start_date: datetime = Field(None, alias="start_date")
