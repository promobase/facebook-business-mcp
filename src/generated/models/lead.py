"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .homelisting import HomeListingFields
    from .leadgenpostsubmissioncheckresult import LeadGenPostSubmissionCheckResultFields
    from .link import LinkFields
    from .userleadgendisclaimerresponse import UserLeadGenDisclaimerResponseFields
    from .userleadgenfielddata import UserLeadGenFieldDataFields
    from .vehicle import VehicleFields


# Field literal type
LeadField = Literal[
    "ad_id",
    "ad_name",
    "adset_id",
    "adset_name",
    "campaign_id",
    "campaign_name",
    "created_time",
    "custom_disclaimer_responses",
    "field_data",
    "form_id",
    "home_listing",
    "id",
    "is_organic",
    "partner_name",
    "platform",
    "post",
    "post_submission_check_result",
    "retailer_item_id",
    "vehicle",
]


class LeadFields(BaseModel):
    """Pydantic model for Lead fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    ad_id: str = Field(None, alias="ad_id")
    ad_name: str = Field(None, alias="ad_name")
    adset_id: str = Field(None, alias="adset_id")
    adset_name: str = Field(None, alias="adset_name")
    campaign_id: str = Field(None, alias="campaign_id")
    campaign_name: str = Field(None, alias="campaign_name")
    created_time: datetime = Field(None, alias="created_time")
    custom_disclaimer_responses: list[UserLeadGenDisclaimerResponseFields] = Field(
        None, alias="custom_disclaimer_responses"
    )
    field_data: list[UserLeadGenFieldDataFields] = Field(None, alias="field_data")
    form_id: str = Field(None, alias="form_id")
    home_listing: HomeListingFields = Field(None, alias="home_listing")
    id: str = Field(None, alias="id")
    is_organic: bool = Field(None, alias="is_organic")
    partner_name: str = Field(None, alias="partner_name")
    platform: str = Field(None, alias="platform")
    post: LinkFields = Field(None, alias="post")
    post_submission_check_result: LeadGenPostSubmissionCheckResultFields = Field(
        None, alias="post_submission_check_result"
    )
    retailer_item_id: str = Field(None, alias="retailer_item_id")
    vehicle: VehicleFields = Field(None, alias="vehicle")
