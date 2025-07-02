"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
ChinaBusinessOnboardingVettingRequestField = Literal[
    "ad_account_creation_request_status",
    "ad_account_limit",
    "ad_account_number",
    "ad_accounts_info",
    "advertiser_business_id",
    "advertiser_business_name",
    "business_manager_id",
    "business_registration",
    "business_registration_id",
    "business_verification_status",
    "chinese_address",
    "chinese_legal_entity_name",
    "city",
    "contact",
    "coupon_code",
    "disapprove_reason",
    "english_business_name",
    "id",
    "official_website_url",
    "org_ad_account_count",
    "payment_type",
    "planning_agency_id",
    "planning_agency_name",
    "promotable_app_ids",
    "promotable_page_ids",
    "promotable_pages",
    "promotable_urls",
    "request_changes_reason",
    "reviewed_user",
    "spend_limit",
    "status",
    "subvertical",
    "subvertical_v2",
    "supporting_document",
    "time_changes_requested",
    "time_created",
    "time_updated",
    "time_zone",
    "used_reseller_link",
    "user_id",
    "user_name",
    "vertical",
    "vertical_v2",
    "viewed_by_reseller",
    "zip_code",
]


class ChinaBusinessOnboardingVettingRequestFields(BaseModel):
    """Pydantic model for ChinaBusinessOnboardingVettingRequest fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    ad_account_creation_request_status: str = Field(
        None, alias="ad_account_creation_request_status"
    )
    ad_account_limit: int = Field(None, alias="ad_account_limit")
    ad_account_number: str = Field(None, alias="ad_account_number")
    ad_accounts_info: list[dict[str, Any]] = Field(None, alias="ad_accounts_info")
    advertiser_business_id: str = Field(None, alias="advertiser_business_id")
    advertiser_business_name: str = Field(None, alias="advertiser_business_name")
    business_manager_id: str = Field(None, alias="business_manager_id")
    business_registration: str = Field(None, alias="business_registration")
    business_registration_id: str = Field(None, alias="business_registration_id")
    business_verification_status: str = Field(None, alias="business_verification_status")
    chinese_address: str = Field(None, alias="chinese_address")
    chinese_legal_entity_name: str = Field(None, alias="chinese_legal_entity_name")
    city: str = Field(None, alias="city")
    contact: str = Field(None, alias="contact")
    coupon_code: str = Field(None, alias="coupon_code")
    disapprove_reason: str = Field(None, alias="disapprove_reason")
    english_business_name: str = Field(None, alias="english_business_name")
    id: str = Field(None, alias="id")
    official_website_url: str = Field(None, alias="official_website_url")
    org_ad_account_count: int = Field(None, alias="org_ad_account_count")
    payment_type: str = Field(None, alias="payment_type")
    planning_agency_id: str = Field(None, alias="planning_agency_id")
    planning_agency_name: str = Field(None, alias="planning_agency_name")
    promotable_app_ids: list[str] = Field(None, alias="promotable_app_ids")
    promotable_page_ids: list[str] = Field(None, alias="promotable_page_ids")
    promotable_pages: list[dict[str, Any]] = Field(None, alias="promotable_pages")
    promotable_urls: list[str] = Field(None, alias="promotable_urls")
    request_changes_reason: str = Field(None, alias="request_changes_reason")
    reviewed_user: str = Field(None, alias="reviewed_user")
    spend_limit: int = Field(None, alias="spend_limit")
    status: str = Field(None, alias="status")
    subvertical: str = Field(None, alias="subvertical")
    subvertical_v2: str = Field(None, alias="subvertical_v2")
    supporting_document: str = Field(None, alias="supporting_document")
    time_changes_requested: datetime = Field(None, alias="time_changes_requested")
    time_created: datetime = Field(None, alias="time_created")
    time_updated: datetime = Field(None, alias="time_updated")
    time_zone: str = Field(None, alias="time_zone")
    used_reseller_link: bool = Field(None, alias="used_reseller_link")
    user_id: str = Field(None, alias="user_id")
    user_name: str = Field(None, alias="user_name")
    vertical: str = Field(None, alias="vertical")
    vertical_v2: str = Field(None, alias="vertical_v2")
    viewed_by_reseller: bool = Field(None, alias="viewed_by_reseller")
    zip_code: str = Field(None, alias="zip_code")
