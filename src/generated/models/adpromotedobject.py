"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .adplacepageset import AdPlacePageSetFields
    from .productset import ProductSetFields


class AdPromotedObject_custom_event_type(str, Enum):
    """AdPromotedObject_custom_event_type enum values."""

    ACHIEVEMENT_UNLOCKED = "ACHIEVEMENT_UNLOCKED"
    ADD_PAYMENT_INFO = "ADD_PAYMENT_INFO"
    ADD_TO_CART = "ADD_TO_CART"
    ADD_TO_WISHLIST = "ADD_TO_WISHLIST"
    AD_IMPRESSION = "AD_IMPRESSION"
    COMPLETE_REGISTRATION = "COMPLETE_REGISTRATION"
    CONTACT = "CONTACT"
    CONTENT_VIEW = "CONTENT_VIEW"
    CUSTOMIZE_PRODUCT = "CUSTOMIZE_PRODUCT"
    D2_RETENTION = "D2_RETENTION"
    D7_RETENTION = "D7_RETENTION"
    DONATE = "DONATE"
    FIND_LOCATION = "FIND_LOCATION"
    INITIATED_CHECKOUT = "INITIATED_CHECKOUT"
    LEAD = "LEAD"
    LEVEL_ACHIEVED = "LEVEL_ACHIEVED"
    LISTING_INTERACTION = "LISTING_INTERACTION"
    MESSAGING_CONVERSATION_STARTED_7D = "MESSAGING_CONVERSATION_STARTED_7D"
    OTHER = "OTHER"
    PURCHASE = "PURCHASE"
    RATE = "RATE"
    SCHEDULE = "SCHEDULE"
    SEARCH = "SEARCH"
    SERVICE_BOOKING_REQUEST = "SERVICE_BOOKING_REQUEST"
    SPENT_CREDITS = "SPENT_CREDITS"
    START_TRIAL = "START_TRIAL"
    SUBMIT_APPLICATION = "SUBMIT_APPLICATION"
    SUBSCRIBE = "SUBSCRIBE"
    TUTORIAL_COMPLETION = "TUTORIAL_COMPLETION"


class AdPromotedObject_lead_ads_custom_event_type(str, Enum):
    """AdPromotedObject_lead_ads_custom_event_type enum values."""

    ACHIEVEMENT_UNLOCKED = "ACHIEVEMENT_UNLOCKED"
    ADD_PAYMENT_INFO = "ADD_PAYMENT_INFO"
    ADD_TO_CART = "ADD_TO_CART"
    ADD_TO_WISHLIST = "ADD_TO_WISHLIST"
    AD_IMPRESSION = "AD_IMPRESSION"
    COMPLETE_REGISTRATION = "COMPLETE_REGISTRATION"
    CONTACT = "CONTACT"
    CONTENT_VIEW = "CONTENT_VIEW"
    CUSTOMIZE_PRODUCT = "CUSTOMIZE_PRODUCT"
    D2_RETENTION = "D2_RETENTION"
    D7_RETENTION = "D7_RETENTION"
    DONATE = "DONATE"
    FIND_LOCATION = "FIND_LOCATION"
    INITIATED_CHECKOUT = "INITIATED_CHECKOUT"
    LEAD = "LEAD"
    LEVEL_ACHIEVED = "LEVEL_ACHIEVED"
    LISTING_INTERACTION = "LISTING_INTERACTION"
    MESSAGING_CONVERSATION_STARTED_7D = "MESSAGING_CONVERSATION_STARTED_7D"
    OTHER = "OTHER"
    PURCHASE = "PURCHASE"
    RATE = "RATE"
    SCHEDULE = "SCHEDULE"
    SEARCH = "SEARCH"
    SERVICE_BOOKING_REQUEST = "SERVICE_BOOKING_REQUEST"
    SPENT_CREDITS = "SPENT_CREDITS"
    START_TRIAL = "START_TRIAL"
    SUBMIT_APPLICATION = "SUBMIT_APPLICATION"
    SUBSCRIBE = "SUBSCRIBE"
    TUTORIAL_COMPLETION = "TUTORIAL_COMPLETION"


# Field literal type
AdPromotedObjectField = Literal[
    "application_id",
    "boosted_product_set_id",
    "conversion_goal_id",
    "custom_conversion_id",
    "custom_event_str",
    "custom_event_type",
    "event_id",
    "fundraiser_campaign_id",
    "lead_ads_custom_event_str",
    "lead_ads_custom_event_type",
    "lead_ads_form_event_source_type",
    "lead_ads_offsite_conversion_type",
    "mcme_conversion_id",
    "object_store_url",
    "offer_id",
    "offline_conversion_data_set_id",
    "offsite_conversion_event_id",
    "omnichannel_object",
    "page_id",
    "pixel_aggregation_rule",
    "pixel_id",
    "pixel_rule",
    "place_page_set",
    "place_page_set_id",
    "product_catalog_id",
    "product_item_id",
    "product_set",
    "product_set_id",
    "product_set_optimization",
    "retention_days",
    "value_semantic_type",
    "variation",
    "whats_app_business_phone_number_id",
    "whatsapp_phone_number",
]


class AdPromotedObjectFields(BaseModel):
    """Pydantic model for AdPromotedObject fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    application_id: str = Field(None, alias="application_id")
    boosted_product_set_id: str = Field(None, alias="boosted_product_set_id")
    conversion_goal_id: str = Field(None, alias="conversion_goal_id")
    custom_conversion_id: str = Field(None, alias="custom_conversion_id")
    custom_event_str: str = Field(None, alias="custom_event_str")
    custom_event_type: dict[str, Any] = Field(None, alias="custom_event_type")
    event_id: str = Field(None, alias="event_id")
    fundraiser_campaign_id: str = Field(None, alias="fundraiser_campaign_id")
    lead_ads_custom_event_str: str = Field(None, alias="lead_ads_custom_event_str")
    lead_ads_custom_event_type: dict[str, Any] = Field(None, alias="lead_ads_custom_event_type")
    lead_ads_form_event_source_type: str = Field(None, alias="lead_ads_form_event_source_type")
    lead_ads_offsite_conversion_type: str = Field(None, alias="lead_ads_offsite_conversion_type")
    mcme_conversion_id: str = Field(None, alias="mcme_conversion_id")
    object_store_url: str = Field(None, alias="object_store_url")
    offer_id: str = Field(None, alias="offer_id")
    offline_conversion_data_set_id: str = Field(None, alias="offline_conversion_data_set_id")
    offsite_conversion_event_id: str = Field(None, alias="offsite_conversion_event_id")
    omnichannel_object: dict[str, Any] = Field(None, alias="omnichannel_object")
    page_id: str = Field(None, alias="page_id")
    pixel_aggregation_rule: str = Field(None, alias="pixel_aggregation_rule")
    pixel_id: str = Field(None, alias="pixel_id")
    pixel_rule: str = Field(None, alias="pixel_rule")
    place_page_set: AdPlacePageSetFields = Field(None, alias="place_page_set")
    place_page_set_id: str = Field(None, alias="place_page_set_id")
    product_catalog_id: str = Field(None, alias="product_catalog_id")
    product_item_id: str = Field(None, alias="product_item_id")
    product_set: ProductSetFields = Field(None, alias="product_set")
    product_set_id: str = Field(None, alias="product_set_id")
    product_set_optimization: str = Field(None, alias="product_set_optimization")
    retention_days: str = Field(None, alias="retention_days")
    value_semantic_type: str = Field(None, alias="value_semantic_type")
    variation: str = Field(None, alias="variation")
    whats_app_business_phone_number_id: str = Field(
        None, alias="whats_app_business_phone_number_id"
    )
    whatsapp_phone_number: str = Field(None, alias="whatsapp_phone_number")
