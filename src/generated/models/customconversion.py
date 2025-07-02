"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .adspixel import AdsPixelFields
    from .business import BusinessFields
    from .externaleventsource import ExternalEventSourceFields
    from .offlineconversiondataset import OfflineConversionDataSetFields


class CustomConversion_custom_event_type(str, Enum):
    """CustomConversion_custom_event_type enum values."""

    ADD_PAYMENT_INFO = "ADD_PAYMENT_INFO"
    ADD_TO_CART = "ADD_TO_CART"
    ADD_TO_WISHLIST = "ADD_TO_WISHLIST"
    COMPLETE_REGISTRATION = "COMPLETE_REGISTRATION"
    CONTACT = "CONTACT"
    CONTENT_VIEW = "CONTENT_VIEW"
    CUSTOMIZE_PRODUCT = "CUSTOMIZE_PRODUCT"
    DONATE = "DONATE"
    FACEBOOK_SELECTED = "FACEBOOK_SELECTED"
    FIND_LOCATION = "FIND_LOCATION"
    INITIATED_CHECKOUT = "INITIATED_CHECKOUT"
    LEAD = "LEAD"
    LISTING_INTERACTION = "LISTING_INTERACTION"
    OTHER = "OTHER"
    PURCHASE = "PURCHASE"
    SCHEDULE = "SCHEDULE"
    SEARCH = "SEARCH"
    START_TRIAL = "START_TRIAL"
    SUBMIT_APPLICATION = "SUBMIT_APPLICATION"
    SUBSCRIBE = "SUBSCRIBE"


class customconversionstats_aggregation_enum_param(str, Enum):
    """customconversionstats_aggregation_enum_param enum values."""

    count = "count"
    device_type = "device_type"
    host = "host"
    pixel_fire = "pixel_fire"
    unmatched_count = "unmatched_count"
    unmatched_usd_amount = "unmatched_usd_amount"
    url = "url"
    usd_amount = "usd_amount"


# Field literal type
CustomConversionField = Literal[
    "account_id",
    "aggregation_rule",
    "business",
    "creation_time",
    "custom_event_type",
    "data_sources",
    "default_conversion_value",
    "description",
    "event_source_type",
    "first_fired_time",
    "id",
    "is_archived",
    "is_unavailable",
    "last_fired_time",
    "name",
    "offline_conversion_data_set",
    "pixel",
    "retention_days",
    "rule",
]


class CustomConversionFields(BaseModel):
    """Pydantic model for CustomConversion fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    account_id: str = Field(None, alias="account_id")
    aggregation_rule: str = Field(None, alias="aggregation_rule")
    business: BusinessFields = Field(None, alias="business")
    creation_time: datetime = Field(None, alias="creation_time")
    custom_event_type: dict[str, Any] = Field(None, alias="custom_event_type")
    data_sources: list[ExternalEventSourceFields] = Field(None, alias="data_sources")
    default_conversion_value: int = Field(None, alias="default_conversion_value")
    description: str = Field(None, alias="description")
    event_source_type: str = Field(None, alias="event_source_type")
    first_fired_time: datetime = Field(None, alias="first_fired_time")
    id: str = Field(None, alias="id")
    is_archived: bool = Field(None, alias="is_archived")
    is_unavailable: bool = Field(None, alias="is_unavailable")
    last_fired_time: datetime = Field(None, alias="last_fired_time")
    name: str = Field(None, alias="name")
    offline_conversion_data_set: OfflineConversionDataSetFields = Field(
        None, alias="offline_conversion_data_set"
    )
    pixel: AdsPixelFields = Field(None, alias="pixel")
    retention_days: int = Field(None, alias="retention_days")
    rule: str = Field(None, alias="rule")


class CustomConversionGetStatsParams(BaseModel):
    """Parameters for CustomConversion.get_stats()."""

    model_config = ConfigDict(extra="forbid")
    aggregation: customconversionstats_aggregation_enum_param | None = Field(
        None, description="aggregation parameter"
    )
    end_time: datetime | None = Field(None, description="end_time parameter")
    start_time: datetime | None = Field(None, description="start_time parameter")
