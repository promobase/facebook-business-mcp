"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .business import BusinessFields
    from .user import UserFields


# Field literal type
AdAccountCreationRequestField = Literal[
    "ad_accounts_currency",
    "ad_accounts_info",
    "additional_comment",
    "address_in_chinese",
    "address_in_english",
    "address_in_local_language",
    "advertiser_business",
    "appeal_reason",
    "business",
    "business_registration_id",
    "chinese_legal_entity_name",
    "contact",
    "creator",
    "credit_card_id",
    "disapproval_reasons",
    "english_legal_entity_name",
    "extended_credit_id",
    "id",
    "is_smb",
    "is_test",
    "legal_entity_name_in_local_language",
    "oe_request_id",
    "official_website_url",
    "planning_agency_business",
    "planning_agency_business_id",
    "promotable_app_ids",
    "promotable_page_ids",
    "promotable_urls",
    "request_change_reasons",
    "status",
    "subvertical",
    "subvertical_v2",
    "time_created",
    "vertical",
    "vertical_v2",
]


class AdAccountCreationRequestFields(BaseModel):
    """Pydantic model for AdAccountCreationRequest fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    ad_accounts_currency: str = Field(None, alias="ad_accounts_currency")
    ad_accounts_info: list[dict[str, Any]] = Field(None, alias="ad_accounts_info")
    additional_comment: str = Field(None, alias="additional_comment")
    address_in_chinese: str = Field(None, alias="address_in_chinese")
    address_in_english: dict[str, Any] = Field(None, alias="address_in_english")
    address_in_local_language: str = Field(None, alias="address_in_local_language")
    advertiser_business: BusinessFields = Field(None, alias="advertiser_business")
    appeal_reason: dict[str, Any] = Field(None, alias="appeal_reason")
    business: BusinessFields = Field(None, alias="business")
    business_registration_id: str = Field(None, alias="business_registration_id")
    chinese_legal_entity_name: str = Field(None, alias="chinese_legal_entity_name")
    contact: dict[str, Any] = Field(None, alias="contact")
    creator: UserFields = Field(None, alias="creator")
    credit_card_id: str = Field(None, alias="credit_card_id")
    disapproval_reasons: list[dict[str, Any]] = Field(None, alias="disapproval_reasons")
    english_legal_entity_name: str = Field(None, alias="english_legal_entity_name")
    extended_credit_id: str = Field(None, alias="extended_credit_id")
    id: str = Field(None, alias="id")
    is_smb: bool = Field(None, alias="is_smb")
    is_test: bool = Field(None, alias="is_test")
    legal_entity_name_in_local_language: str = Field(
        None, alias="legal_entity_name_in_local_language"
    )
    oe_request_id: str = Field(None, alias="oe_request_id")
    official_website_url: str = Field(None, alias="official_website_url")
    planning_agency_business: BusinessFields = Field(None, alias="planning_agency_business")
    planning_agency_business_id: str = Field(None, alias="planning_agency_business_id")
    promotable_app_ids: list[str] = Field(None, alias="promotable_app_ids")
    promotable_page_ids: list[str] = Field(None, alias="promotable_page_ids")
    promotable_urls: list[str] = Field(None, alias="promotable_urls")
    request_change_reasons: list[dict[str, Any]] = Field(None, alias="request_change_reasons")
    status: str = Field(None, alias="status")
    subvertical: str = Field(None, alias="subvertical")
    subvertical_v2: str = Field(None, alias="subvertical_v2")
    time_created: datetime = Field(None, alias="time_created")
    vertical: str = Field(None, alias="vertical")
    vertical_v2: str = Field(None, alias="vertical_v2")
