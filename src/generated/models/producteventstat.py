"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .externaleventsource import ExternalEventSourceFields


class ProductEventStat_device_type(str, Enum):
    """ProductEventStat_device_type enum values."""

    desktop = "desktop"
    mobile_android_phone = "mobile_android_phone"
    mobile_android_tablet = "mobile_android_tablet"
    mobile_ipad = "mobile_ipad"
    mobile_iphone = "mobile_iphone"
    mobile_ipod = "mobile_ipod"
    mobile_phone = "mobile_phone"
    mobile_tablet = "mobile_tablet"
    mobile_windows_phone = "mobile_windows_phone"
    unknown = "unknown"


class ProductEventStat_event(str, Enum):
    """ProductEventStat_event enum values."""

    AddToCart = "AddToCart"
    AddToWishlist = "AddToWishlist"
    InitiateCheckout = "InitiateCheckout"
    Lead = "Lead"
    Purchase = "Purchase"
    Search = "Search"
    Subscribe = "Subscribe"
    ViewContent = "ViewContent"


# Field literal type
ProductEventStatField = Literal[
    "date_start",
    "date_stop",
    "device_type",
    "event",
    "event_source",
    "total_content_ids_matched_other_catalogs",
    "total_matched_content_ids",
    "total_unmatched_content_ids",
    "unique_content_ids_matched_other_catalogs",
    "unique_matched_content_ids",
    "unique_unmatched_content_ids",
]


class ProductEventStatFields(BaseModel):
    """Pydantic model for ProductEventStat fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    date_start: str = Field(None, alias="date_start")
    date_stop: str = Field(None, alias="date_stop")
    device_type: dict[str, Any] = Field(None, alias="device_type")
    event: dict[str, Any] = Field(None, alias="event")
    event_source: ExternalEventSourceFields = Field(None, alias="event_source")
    total_content_ids_matched_other_catalogs: int = Field(
        None, alias="total_content_ids_matched_other_catalogs"
    )
    total_matched_content_ids: int = Field(None, alias="total_matched_content_ids")
    total_unmatched_content_ids: int = Field(None, alias="total_unmatched_content_ids")
    unique_content_ids_matched_other_catalogs: int = Field(
        None, alias="unique_content_ids_matched_other_catalogs"
    )
    unique_matched_content_ids: int = Field(None, alias="unique_matched_content_ids")
    unique_unmatched_content_ids: int = Field(None, alias="unique_unmatched_content_ids")
