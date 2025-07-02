"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .business import BusinessFields


class admonetizationpropertyadnetworkanalytics_ordering_type_enum_param(str, Enum):
    """admonetizationpropertyadnetworkanalytics_ordering_type_enum_param enum values."""

    ASCENDING = "ASCENDING"
    DESCENDING = "DESCENDING"


class admonetizationpropertyadnetworkanalytics_aggregation_period_enum_param(str, Enum):
    """admonetizationpropertyadnetworkanalytics_aggregation_period_enum_param enum values."""

    DAY = "DAY"
    TOTAL = "TOTAL"


class admonetizationpropertyadnetworkanalytics_ordering_column_enum_param(str, Enum):
    """admonetizationpropertyadnetworkanalytics_ordering_column_enum_param enum values."""

    METRIC = "METRIC"
    TIME = "TIME"
    VALUE = "VALUE"


class admonetizationpropertyadnetworkanalytics_metrics_enum_param(str, Enum):
    """admonetizationpropertyadnetworkanalytics_metrics_enum_param enum values."""

    FB_AD_NETWORK_BIDDING_BID_RATE = "FB_AD_NETWORK_BIDDING_BID_RATE"
    FB_AD_NETWORK_BIDDING_REQUEST = "FB_AD_NETWORK_BIDDING_REQUEST"
    FB_AD_NETWORK_BIDDING_RESPONSE = "FB_AD_NETWORK_BIDDING_RESPONSE"
    FB_AD_NETWORK_BIDDING_REVENUE = "FB_AD_NETWORK_BIDDING_REVENUE"
    FB_AD_NETWORK_BIDDING_WIN_RATE = "FB_AD_NETWORK_BIDDING_WIN_RATE"
    FB_AD_NETWORK_CLICK = "FB_AD_NETWORK_CLICK"
    FB_AD_NETWORK_CPM = "FB_AD_NETWORK_CPM"
    FB_AD_NETWORK_CTR = "FB_AD_NETWORK_CTR"
    FB_AD_NETWORK_FILLED_REQUEST = "FB_AD_NETWORK_FILLED_REQUEST"
    FB_AD_NETWORK_FILL_RATE = "FB_AD_NETWORK_FILL_RATE"
    FB_AD_NETWORK_IMP = "FB_AD_NETWORK_IMP"
    FB_AD_NETWORK_IMPRESSION_RATE = "FB_AD_NETWORK_IMPRESSION_RATE"
    FB_AD_NETWORK_REQUEST = "FB_AD_NETWORK_REQUEST"
    FB_AD_NETWORK_REVENUE = "FB_AD_NETWORK_REVENUE"
    FB_AD_NETWORK_SHOW_RATE = "FB_AD_NETWORK_SHOW_RATE"
    FB_AD_NETWORK_VIDEO_GUARANTEE_REVENUE = "FB_AD_NETWORK_VIDEO_GUARANTEE_REVENUE"
    FB_AD_NETWORK_VIDEO_MRC = "FB_AD_NETWORK_VIDEO_MRC"
    FB_AD_NETWORK_VIDEO_MRC_RATE = "FB_AD_NETWORK_VIDEO_MRC_RATE"
    FB_AD_NETWORK_VIDEO_VIEW = "FB_AD_NETWORK_VIDEO_VIEW"
    FB_AD_NETWORK_VIDEO_VIEW_RATE = "FB_AD_NETWORK_VIDEO_VIEW_RATE"


class admonetizationpropertyadnetworkanalytics_breakdowns_enum_param(str, Enum):
    """admonetizationpropertyadnetworkanalytics_breakdowns_enum_param enum values."""

    AD_SERVER_CAMPAIGN_ID = "AD_SERVER_CAMPAIGN_ID"
    AD_SPACE = "AD_SPACE"
    AGE = "AGE"
    APP = "APP"
    CLICKED_VIEW_TAG = "CLICKED_VIEW_TAG"
    COUNTRY = "COUNTRY"
    DEAL = "DEAL"
    DEAL_AD = "DEAL_AD"
    DEAL_PAGE = "DEAL_PAGE"
    DELIVERY_METHOD = "DELIVERY_METHOD"
    DISPLAY_FORMAT = "DISPLAY_FORMAT"
    FAIL_REASON = "FAIL_REASON"
    GENDER = "GENDER"
    INSTANT_ARTICLE_ID = "INSTANT_ARTICLE_ID"
    INSTANT_ARTICLE_PAGE_ID = "INSTANT_ARTICLE_PAGE_ID"
    IS_DEAL_BACKFILL = "IS_DEAL_BACKFILL"
    PLACEMENT = "PLACEMENT"
    PLACEMENT_NAME = "PLACEMENT_NAME"
    PLATFORM = "PLATFORM"
    PROPERTY = "PROPERTY"
    SDK_VERSION = "SDK_VERSION"


# Field literal type
AdMonetizationPropertyField = Literal["owner_business"]


class AdMonetizationPropertyFields(BaseModel):
    """Pydantic model for AdMonetizationProperty fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    owner_business: BusinessFields = Field(None, alias="owner_business")


class AdMonetizationPropertyGetAdNetworkanalyticsParams(BaseModel):
    """Parameters for AdMonetizationProperty.get_ad_networkanalytics()."""

    model_config = ConfigDict(extra="forbid")
    aggregation_period: (
        admonetizationpropertyadnetworkanalytics_aggregation_period_enum_param | None
    ) = Field(None, description="aggregation_period parameter")
    breakdowns: list[admonetizationpropertyadnetworkanalytics_breakdowns_enum_param] | None = Field(
        None, description="breakdowns parameter"
    )
    filters: list[dict[str, Any]] | None = Field(None, description="filters parameter")
    limit: int | None = Field(None, description="limit parameter")
    metrics: list[admonetizationpropertyadnetworkanalytics_metrics_enum_param] | None = Field(
        None, description="metrics parameter"
    )
    ordering_column: admonetizationpropertyadnetworkanalytics_ordering_column_enum_param | None = (
        Field(None, description="ordering_column parameter")
    )
    ordering_type: admonetizationpropertyadnetworkanalytics_ordering_type_enum_param | None = Field(
        None, description="ordering_type parameter"
    )
    should_include_until: bool | None = Field(None, description="should_include_until parameter")
    since: datetime | None = Field(None, description="since parameter")
    until: datetime | None = Field(None, description="until parameter")


class AdMonetizationPropertyCreateAdNetworkanalyticParams(BaseModel):
    """Parameters for AdMonetizationProperty.create_ad_networkanalytic()."""

    model_config = ConfigDict(extra="forbid")
    aggregation_period: (
        admonetizationpropertyadnetworkanalytics_aggregation_period_enum_param | None
    ) = Field(None, description="aggregation_period parameter")
    breakdowns: list[admonetizationpropertyadnetworkanalytics_breakdowns_enum_param] | None = Field(
        None, description="breakdowns parameter"
    )
    filters: list[dict[str, Any]] | None = Field(None, description="filters parameter")
    limit: int | None = Field(None, description="limit parameter")
    metrics: list[admonetizationpropertyadnetworkanalytics_metrics_enum_param] | None = Field(
        None, description="metrics parameter"
    )
    ordering_column: admonetizationpropertyadnetworkanalytics_ordering_column_enum_param | None = (
        Field(None, description="ordering_column parameter")
    )
    ordering_type: admonetizationpropertyadnetworkanalytics_ordering_type_enum_param | None = Field(
        None, description="ordering_type parameter"
    )
    since: datetime | None = Field(None, description="since parameter")
    until: datetime | None = Field(None, description="until parameter")


class AdMonetizationPropertyGetAdnetworkanalyticsResultsParams(BaseModel):
    """Parameters for AdMonetizationProperty.get_adnetworkanalytics_results()."""

    model_config = ConfigDict(extra="forbid")
    query_ids: list[str] | None = Field(None, description="query_ids parameter")
