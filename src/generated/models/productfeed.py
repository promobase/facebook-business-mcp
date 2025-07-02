"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .productfeedschedule import ProductFeedScheduleFields
    from .productfeedupload import ProductFeedUploadFields


class ProductFeed_delimiter(str, Enum):
    """ProductFeed_delimiter enum values."""

    AUTODETECT = "AUTODETECT"
    BAR = "BAR"
    COMMA = "COMMA"
    SEMICOLON = "SEMICOLON"
    TAB = "TAB"
    TILDE = "TILDE"


class ProductFeed_ingestion_source_type(str, Enum):
    """ProductFeed_ingestion_source_type enum values."""

    primary_feed = "primary_feed"
    supplementary_feed = "supplementary_feed"


class ProductFeed_quoted_fields_mode(str, Enum):
    """ProductFeed_quoted_fields_mode enum values."""

    AUTODETECT = "AUTODETECT"
    OFF = "OFF"
    ON = "ON"


class productfeedrules_rule_type_enum_param(str, Enum):
    """productfeedrules_rule_type_enum_param enum values."""

    fallback_rule = "fallback_rule"
    letter_case_rule = "letter_case_rule"
    mapping_rule = "mapping_rule"
    regex_replace_rule = "regex_replace_rule"
    value_mapping_rule = "value_mapping_rule"


class productfeedproducts_error_priority_enum_param(str, Enum):
    """productfeedproducts_error_priority_enum_param enum values."""

    HIGH = "HIGH"
    LOW = "LOW"
    MEDIUM = "MEDIUM"


class productfeedproducts_error_type_enum_param(str, Enum):
    """productfeedproducts_error_type_enum_param enum values."""

    ADDRESS_BLOCKLISTED_IN_MARKET = "ADDRESS_BLOCKLISTED_IN_MARKET"
    AGGREGATED_LOCALIZATION_ISSUES = "AGGREGATED_LOCALIZATION_ISSUES"
    APP_HAS_NO_AEM_SETUP = "APP_HAS_NO_AEM_SETUP"
    AR_DELETED_DUE_TO_UPDATE = "AR_DELETED_DUE_TO_UPDATE"
    AR_POLICY_VIOLATED = "AR_POLICY_VIOLATED"
    AVAILABLE = "AVAILABLE"
    BAD_QUALITY_IMAGE = "BAD_QUALITY_IMAGE"
    BIG_CATALOG_WITH_ALL_ITEMS_IN_STOCK = "BIG_CATALOG_WITH_ALL_ITEMS_IN_STOCK"
    BIZ_MSG_AI_AGENT_DISABLED_BY_USER = "BIZ_MSG_AI_AGENT_DISABLED_BY_USER"
    BIZ_MSG_GEN_AI_POLICY_VIOLATED = "BIZ_MSG_GEN_AI_POLICY_VIOLATED"
    CANNOT_EDIT_SUBSCRIPTION_PRODUCTS = "CANNOT_EDIT_SUBSCRIPTION_PRODUCTS"
    CATALOG_NOT_CONNECTED_TO_EVENT_SOURCE = "CATALOG_NOT_CONNECTED_TO_EVENT_SOURCE"
    CHECKOUT_DISABLED_BY_USER = "CHECKOUT_DISABLED_BY_USER"
    COMMERCE_ACCOUNT_LEGAL_ADDRESS_INVALID = "COMMERCE_ACCOUNT_LEGAL_ADDRESS_INVALID"
    COMMERCE_ACCOUNT_NOT_LEGALLY_COMPLIANT = "COMMERCE_ACCOUNT_NOT_LEGALLY_COMPLIANT"
    CRAWLED_AVAILABILITY_MISMATCH = "CRAWLED_AVAILABILITY_MISMATCH"
    DA_DISABLED_BY_USER = "DA_DISABLED_BY_USER"
    DA_POLICY_UNFIT_FOR_AUDIENCE = "DA_POLICY_UNFIT_FOR_AUDIENCE"
    DA_POLICY_VIOLATION = "DA_POLICY_VIOLATION"
    DELETED_ITEM = "DELETED_ITEM"
    DIGITAL_GOODS_NOT_AVAILABLE_FOR_CHECKOUT = "DIGITAL_GOODS_NOT_AVAILABLE_FOR_CHECKOUT"
    DUPLICATE_IMAGES = "DUPLICATE_IMAGES"
    DUPLICATE_TITLE_AND_DESCRIPTION = "DUPLICATE_TITLE_AND_DESCRIPTION"
    EMPTY_AVAILABILITY = "EMPTY_AVAILABILITY"
    EMPTY_CONDITION = "EMPTY_CONDITION"
    EMPTY_DESCRIPTION = "EMPTY_DESCRIPTION"
    EMPTY_IMAGE_URL = "EMPTY_IMAGE_URL"
    EMPTY_PRICE = "EMPTY_PRICE"
    EMPTY_PRODUCT_URL = "EMPTY_PRODUCT_URL"
    EMPTY_SELLER_DESCRIPTION = "EMPTY_SELLER_DESCRIPTION"
    EMPTY_TITLE = "EMPTY_TITLE"
    EXTERNAL_MERCHANT_ID_MISMATCH = "EXTERNAL_MERCHANT_ID_MISMATCH"
    GENERIC_INVALID_FIELD = "GENERIC_INVALID_FIELD"
    GROUPS_DISABLED_BY_USER = "GROUPS_DISABLED_BY_USER"
    HIDDEN_UNTIL_PRODUCT_LAUNCH = "HIDDEN_UNTIL_PRODUCT_LAUNCH"
    ILLEGAL_PRODUCT_CATEGORY = "ILLEGAL_PRODUCT_CATEGORY"
    IMAGE_FETCH_FAILED = "IMAGE_FETCH_FAILED"
    IMAGE_FETCH_FAILED_BAD_GATEWAY = "IMAGE_FETCH_FAILED_BAD_GATEWAY"
    IMAGE_FETCH_FAILED_FILE_SIZE_EXCEEDED = "IMAGE_FETCH_FAILED_FILE_SIZE_EXCEEDED"
    IMAGE_FETCH_FAILED_FORBIDDEN = "IMAGE_FETCH_FAILED_FORBIDDEN"
    IMAGE_FETCH_FAILED_LINK_BROKEN = "IMAGE_FETCH_FAILED_LINK_BROKEN"
    IMAGE_FETCH_FAILED_TIMED_OUT = "IMAGE_FETCH_FAILED_TIMED_OUT"
    IMAGE_RESOLUTION_LOW = "IMAGE_RESOLUTION_LOW"
    INACTIVE_SHOPIFY_PRODUCT = "INACTIVE_SHOPIFY_PRODUCT"
    INVALID_COMMERCE_TAX_CATEGORY = "INVALID_COMMERCE_TAX_CATEGORY"
    INVALID_CONSOLIDATED_LOCALITY_INFORMATION = "INVALID_CONSOLIDATED_LOCALITY_INFORMATION"
    INVALID_CONTENT_ID = "INVALID_CONTENT_ID"
    INVALID_DEALER_COMMUNICATION_PARAMETERS = "INVALID_DEALER_COMMUNICATION_PARAMETERS"
    INVALID_DMA_CODES = "INVALID_DMA_CODES"
    INVALID_FB_PAGE_ID = "INVALID_FB_PAGE_ID"
    INVALID_IMAGES = "INVALID_IMAGES"
    INVALID_MONETIZER_RETURN_POLICY = "INVALID_MONETIZER_RETURN_POLICY"
    INVALID_OFFER_DISCLAIMER_URL = "INVALID_OFFER_DISCLAIMER_URL"
    INVALID_OFFER_END_DATE = "INVALID_OFFER_END_DATE"
    INVALID_PRE_ORDER_PARAMS = "INVALID_PRE_ORDER_PARAMS"
    INVALID_RANGE_FOR_AREA_SIZE = "INVALID_RANGE_FOR_AREA_SIZE"
    INVALID_RANGE_FOR_BUILT_UP_AREA_SIZE = "INVALID_RANGE_FOR_BUILT_UP_AREA_SIZE"
    INVALID_RANGE_FOR_NUM_OF_BATHS = "INVALID_RANGE_FOR_NUM_OF_BATHS"
    INVALID_RANGE_FOR_NUM_OF_BEDS = "INVALID_RANGE_FOR_NUM_OF_BEDS"
    INVALID_RANGE_FOR_NUM_OF_ROOMS = "INVALID_RANGE_FOR_NUM_OF_ROOMS"
    INVALID_RANGE_FOR_PARKING_SPACES = "INVALID_RANGE_FOR_PARKING_SPACES"
    INVALID_SHELTER_PAGE_ID = "INVALID_SHELTER_PAGE_ID"
    INVALID_SHIPPING_PROFILE_PARAMS = "INVALID_SHIPPING_PROFILE_PARAMS"
    INVALID_SUBSCRIPTION_DISABLE_PARAMS = "INVALID_SUBSCRIPTION_DISABLE_PARAMS"
    INVALID_SUBSCRIPTION_ENABLE_PARAMS = "INVALID_SUBSCRIPTION_ENABLE_PARAMS"
    INVALID_SUBSCRIPTION_PARAMS = "INVALID_SUBSCRIPTION_PARAMS"
    INVALID_TAX_EXTENSION_STATE = "INVALID_TAX_EXTENSION_STATE"
    INVALID_VEHICLE_STATE = "INVALID_VEHICLE_STATE"
    INVALID_VIRTUAL_TOUR_URL_DOMAIN = "INVALID_VIRTUAL_TOUR_URL_DOMAIN"
    INVENTORY_ZERO_AVAILABILITY_IN_STOCK = "INVENTORY_ZERO_AVAILABILITY_IN_STOCK"
    IN_ANOTHER_PRODUCT_LAUNCH = "IN_ANOTHER_PRODUCT_LAUNCH"
    ITEM_GROUP_NOT_SPECIFIED = "ITEM_GROUP_NOT_SPECIFIED"
    ITEM_NOT_SHIPPABLE_FOR_SCA_SHOP = "ITEM_NOT_SHIPPABLE_FOR_SCA_SHOP"
    ITEM_OVERRIDE_EMPTY_AVAILABILITY = "ITEM_OVERRIDE_EMPTY_AVAILABILITY"
    ITEM_OVERRIDE_EMPTY_PRICE = "ITEM_OVERRIDE_EMPTY_PRICE"
    ITEM_OVERRIDE_NOT_VISIBLE = "ITEM_OVERRIDE_NOT_VISIBLE"
    ITEM_PRICE_NOT_POSITIVE = "ITEM_PRICE_NOT_POSITIVE"
    ITEM_STALE_OUT_OF_STOCK = "ITEM_STALE_OUT_OF_STOCK"
    MARKETPLACE_DISABLED_BY_USER = "MARKETPLACE_DISABLED_BY_USER"
    MARKETPLACE_PARTNER_AUCTION_NO_BID_CLOSE_TIME = "MARKETPLACE_PARTNER_AUCTION_NO_BID_CLOSE_TIME"
    MARKETPLACE_PARTNER_CURRENCY_NOT_VALID = "MARKETPLACE_PARTNER_CURRENCY_NOT_VALID"
    MARKETPLACE_PARTNER_LISTING_COUNTRY_NOT_MATCH_CATALOG = (
        "MARKETPLACE_PARTNER_LISTING_COUNTRY_NOT_MATCH_CATALOG"
    )
    MARKETPLACE_PARTNER_LISTING_LIMIT_EXCEEDED = "MARKETPLACE_PARTNER_LISTING_LIMIT_EXCEEDED"
    MARKETPLACE_PARTNER_MISSING_LATLONG = "MARKETPLACE_PARTNER_MISSING_LATLONG"
    MARKETPLACE_PARTNER_MISSING_SHIPPING_COST = "MARKETPLACE_PARTNER_MISSING_SHIPPING_COST"
    MARKETPLACE_PARTNER_NOT_LOCAL_ITEM = "MARKETPLACE_PARTNER_NOT_LOCAL_ITEM"
    MARKETPLACE_PARTNER_NOT_SHIPPED_ITEM = "MARKETPLACE_PARTNER_NOT_SHIPPED_ITEM"
    MARKETPLACE_PARTNER_POLICY_VIOLATION = "MARKETPLACE_PARTNER_POLICY_VIOLATION"
    MARKETPLACE_PARTNER_RULE_LISTING_LIMIT_EXCEEDED = (
        "MARKETPLACE_PARTNER_RULE_LISTING_LIMIT_EXCEEDED"
    )
    MARKETPLACE_PARTNER_SELLER_BANNED = "MARKETPLACE_PARTNER_SELLER_BANNED"
    MARKETPLACE_PARTNER_SELLER_NOT_VALID = "MARKETPLACE_PARTNER_SELLER_NOT_VALID"
    MINI_SHOPS_DISABLED_BY_USER = "MINI_SHOPS_DISABLED_BY_USER"
    MISSING_CHECKOUT = "MISSING_CHECKOUT"
    MISSING_CHECKOUT_CURRENCY = "MISSING_CHECKOUT_CURRENCY"
    MISSING_COLOR = "MISSING_COLOR"
    MISSING_COUNTRY_OVERRIDE_IN_SHIPPING_PROFILE = "MISSING_COUNTRY_OVERRIDE_IN_SHIPPING_PROFILE"
    MISSING_EVENT = "MISSING_EVENT"
    MISSING_INDIA_COMPLIANCE_FIELDS = "MISSING_INDIA_COMPLIANCE_FIELDS"
    MISSING_SHIPPING_PROFILE = "MISSING_SHIPPING_PROFILE"
    MISSING_SIZE = "MISSING_SIZE"
    MISSING_TAX_CATEGORY = "MISSING_TAX_CATEGORY"
    NEGATIVE_COMMUNITY_FEEDBACK = "NEGATIVE_COMMUNITY_FEEDBACK"
    NEGATIVE_PRICE = "NEGATIVE_PRICE"
    NOT_ENOUGH_IMAGES = "NOT_ENOUGH_IMAGES"
    NOT_ENOUGH_UNIQUE_PRODUCTS = "NOT_ENOUGH_UNIQUE_PRODUCTS"
    NO_CONTENT_ID = "NO_CONTENT_ID"
    OVERLAY_DISCLAIMER_EXCEEDED_MAX_LENGTH = "OVERLAY_DISCLAIMER_EXCEEDED_MAX_LENGTH"
    PART_OF_PRODUCT_LAUNCH = "PART_OF_PRODUCT_LAUNCH"
    PASSING_MULTIPLE_CONTENT_IDS = "PASSING_MULTIPLE_CONTENT_IDS"
    PRODUCT_DOMINANT_CURRENCY_MISMATCH = "PRODUCT_DOMINANT_CURRENCY_MISMATCH"
    PRODUCT_EXPIRED = "PRODUCT_EXPIRED"
    PRODUCT_ITEM_HIDDEN_FROM_ALL_SHOPS = "PRODUCT_ITEM_HIDDEN_FROM_ALL_SHOPS"
    PRODUCT_ITEM_INVALID_PARTNER_TOKENS = "PRODUCT_ITEM_INVALID_PARTNER_TOKENS"
    PRODUCT_ITEM_NOT_INCLUDED_IN_ANY_SHOP = "PRODUCT_ITEM_NOT_INCLUDED_IN_ANY_SHOP"
    PRODUCT_ITEM_NOT_VISIBLE = "PRODUCT_ITEM_NOT_VISIBLE"
    PRODUCT_NOT_APPROVED = "PRODUCT_NOT_APPROVED"
    PRODUCT_NOT_DOMINANT_CURRENCY = "PRODUCT_NOT_DOMINANT_CURRENCY"
    PRODUCT_OUT_OF_STOCK = "PRODUCT_OUT_OF_STOCK"
    PRODUCT_URL_EQUALS_DOMAIN = "PRODUCT_URL_EQUALS_DOMAIN"
    PROPERTY_PRICE_CURRENCY_NOT_SUPPORTED = "PROPERTY_PRICE_CURRENCY_NOT_SUPPORTED"
    PROPERTY_PRICE_TOO_HIGH = "PROPERTY_PRICE_TOO_HIGH"
    PROPERTY_PRICE_TOO_LOW = "PROPERTY_PRICE_TOO_LOW"
    PROPERTY_UNIT_PRICE_CURRENCY_MISMATCH_ITEM_PRICE_CURRENCY = (
        "PROPERTY_UNIT_PRICE_CURRENCY_MISMATCH_ITEM_PRICE_CURRENCY"
    )
    PROPERTY_VALUE_CONTAINS_HTML_TAGS = "PROPERTY_VALUE_CONTAINS_HTML_TAGS"
    PROPERTY_VALUE_DESCRIPTION_CONTAINS_OFF_PLATFORM_LINK = (
        "PROPERTY_VALUE_DESCRIPTION_CONTAINS_OFF_PLATFORM_LINK"
    )
    PROPERTY_VALUE_FORMAT = "PROPERTY_VALUE_FORMAT"
    PROPERTY_VALUE_MISSING = "PROPERTY_VALUE_MISSING"
    PROPERTY_VALUE_MISSING_WARNING = "PROPERTY_VALUE_MISSING_WARNING"
    PROPERTY_VALUE_NON_POSITIVE = "PROPERTY_VALUE_NON_POSITIVE"
    PROPERTY_VALUE_STRING_EXCEEDS_LENGTH = "PROPERTY_VALUE_STRING_EXCEEDS_LENGTH"
    PROPERTY_VALUE_STRING_TOO_SHORT = "PROPERTY_VALUE_STRING_TOO_SHORT"
    PROPERTY_VALUE_UPPERCASE = "PROPERTY_VALUE_UPPERCASE"
    PROPERTY_VALUE_UPPERCASE_WARNING = "PROPERTY_VALUE_UPPERCASE_WARNING"
    PURCHASE_RATE_BELOW_ADDTOCART = "PURCHASE_RATE_BELOW_ADDTOCART"
    PURCHASE_RATE_BELOW_VIEWCONTENT = "PURCHASE_RATE_BELOW_VIEWCONTENT"
    QUALITY_DUPLICATED_DESCRIPTION = "QUALITY_DUPLICATED_DESCRIPTION"
    QUALITY_ITEM_LINK_BROKEN = "QUALITY_ITEM_LINK_BROKEN"
    QUALITY_ITEM_LINK_REDIRECTING = "QUALITY_ITEM_LINK_REDIRECTING"
    RETAILER_ID_NOT_PROVIDED = "RETAILER_ID_NOT_PROVIDED"
    SHOPIFY_INVALID_RETAILER_ID = "SHOPIFY_INVALID_RETAILER_ID"
    SHOPIFY_ITEM_MISSING_SHIPPING_PROFILE = "SHOPIFY_ITEM_MISSING_SHIPPING_PROFILE"
    SHOPS_POLICY_VIOLATION = "SHOPS_POLICY_VIOLATION"
    SUBSCRIPTION_INFO_NOT_ENABLED_FOR_FEED = "SUBSCRIPTION_INFO_NOT_ENABLED_FOR_FEED"
    TAX_CATEGORY_NOT_SUPPORTED_IN_UK = "TAX_CATEGORY_NOT_SUPPORTED_IN_UK"
    UNIQUE_PRODUCT_IDENTIFIER_MISSING = "UNIQUE_PRODUCT_IDENTIFIER_MISSING"
    UNMATCHED_EVENTS = "UNMATCHED_EVENTS"
    UNSUPPORTED_PRODUCT_CATEGORY = "UNSUPPORTED_PRODUCT_CATEGORY"
    VARIANT_ATTRIBUTE_ISSUE = "VARIANT_ATTRIBUTE_ISSUE"
    VIDEO_FETCH_FAILED = "VIDEO_FETCH_FAILED"
    VIDEO_FETCH_FAILED_BAD_GATEWAY = "VIDEO_FETCH_FAILED_BAD_GATEWAY"
    VIDEO_FETCH_FAILED_FILE_SIZE_EXCEEDED = "VIDEO_FETCH_FAILED_FILE_SIZE_EXCEEDED"
    VIDEO_FETCH_FAILED_FORBIDDEN = "VIDEO_FETCH_FAILED_FORBIDDEN"
    VIDEO_FETCH_FAILED_LINK_BROKEN = "VIDEO_FETCH_FAILED_LINK_BROKEN"
    VIDEO_FETCH_FAILED_TIMED_OUT = "VIDEO_FETCH_FAILED_TIMED_OUT"
    VIDEO_NOT_DOWNLOADABLE = "VIDEO_NOT_DOWNLOADABLE"
    WHATSAPP_DISABLED_BY_USER = "WHATSAPP_DISABLED_BY_USER"
    WHATSAPP_MARKETING_MESSAGE_DISABLED_BY_USER = "WHATSAPP_MARKETING_MESSAGE_DISABLED_BY_USER"
    WHATSAPP_MARKETING_MESSAGE_POLICY_VIOLATION = "WHATSAPP_MARKETING_MESSAGE_POLICY_VIOLATION"
    WHATSAPP_POLICY_VIOLATION = "WHATSAPP_POLICY_VIOLATION"


# Field literal type
ProductFeedField = Literal[
    "country",
    "created_time",
    "default_currency",
    "deletion_enabled",
    "delimiter",
    "encoding",
    "file_name",
    "id",
    "ingestion_source_type",
    "item_sub_type",
    "latest_upload",
    "migrated_from_feed_id",
    "name",
    "override_type",
    "primary_feeds",
    "product_count",
    "quoted_fields_mode",
    "schedule",
    "supplementary_feeds",
    "update_schedule",
]


class ProductFeedFields(BaseModel):
    """Pydantic model for ProductFeed fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    country: str = Field(None, alias="country")
    created_time: datetime = Field(None, alias="created_time")
    default_currency: str = Field(None, alias="default_currency")
    deletion_enabled: bool = Field(None, alias="deletion_enabled")
    delimiter: dict[str, Any] = Field(None, alias="delimiter")
    encoding: str = Field(None, alias="encoding")
    file_name: str = Field(None, alias="file_name")
    id: str = Field(None, alias="id")
    ingestion_source_type: dict[str, Any] = Field(None, alias="ingestion_source_type")
    item_sub_type: str = Field(None, alias="item_sub_type")
    latest_upload: ProductFeedUploadFields = Field(None, alias="latest_upload")
    migrated_from_feed_id: str = Field(None, alias="migrated_from_feed_id")
    name: str = Field(None, alias="name")
    override_type: str = Field(None, alias="override_type")
    primary_feeds: list[str] = Field(None, alias="primary_feeds")
    product_count: int = Field(None, alias="product_count")
    quoted_fields_mode: dict[str, Any] = Field(None, alias="quoted_fields_mode")
    schedule: ProductFeedScheduleFields = Field(None, alias="schedule")
    supplementary_feeds: list[str] = Field(None, alias="supplementary_feeds")
    update_schedule: ProductFeedScheduleFields = Field(None, alias="update_schedule")


class ProductFeedGetAutomotiveModelsParams(BaseModel):
    """Parameters for ProductFeed.get_automotive_models()."""

    model_config = ConfigDict(extra="forbid")
    bulk_pagination: bool | None = Field(None, description="bulk_pagination parameter")
    filter: dict[str, Any] | None = Field(None, description="filter parameter")


class ProductFeedGetDestinationsParams(BaseModel):
    """Parameters for ProductFeed.get_destinations()."""

    model_config = ConfigDict(extra="forbid")
    bulk_pagination: bool | None = Field(None, description="bulk_pagination parameter")
    filter: dict[str, Any] | None = Field(None, description="filter parameter")


class ProductFeedGetFlightsParams(BaseModel):
    """Parameters for ProductFeed.get_flights()."""

    model_config = ConfigDict(extra="forbid")
    bulk_pagination: bool | None = Field(None, description="bulk_pagination parameter")
    filter: dict[str, Any] | None = Field(None, description="filter parameter")


class ProductFeedGetHomeListingsParams(BaseModel):
    """Parameters for ProductFeed.get_home_listings()."""

    model_config = ConfigDict(extra="forbid")
    bulk_pagination: bool | None = Field(None, description="bulk_pagination parameter")
    filter: dict[str, Any] | None = Field(None, description="filter parameter")


class ProductFeedGetHotelsParams(BaseModel):
    """Parameters for ProductFeed.get_hotels()."""

    model_config = ConfigDict(extra="forbid")
    bulk_pagination: bool | None = Field(None, description="bulk_pagination parameter")
    filter: dict[str, Any] | None = Field(None, description="filter parameter")


class ProductFeedGetMediaTitlesParams(BaseModel):
    """Parameters for ProductFeed.get_media_titles()."""

    model_config = ConfigDict(extra="forbid")
    bulk_pagination: bool | None = Field(None, description="bulk_pagination parameter")
    filter: dict[str, Any] | None = Field(None, description="filter parameter")


class ProductFeedGetProductsParams(BaseModel):
    """Parameters for ProductFeed.get_products()."""

    model_config = ConfigDict(extra="forbid")
    bulk_pagination: bool | None = Field(None, description="bulk_pagination parameter")
    error_priority: productfeedproducts_error_priority_enum_param | None = Field(
        None, description="error_priority parameter"
    )
    error_type: productfeedproducts_error_type_enum_param | None = Field(
        None, description="error_type parameter"
    )
    filter: dict[str, Any] | None = Field(None, description="filter parameter")


class ProductFeedCreateRuleParams(BaseModel):
    """Parameters for ProductFeed.create_rule()."""

    model_config = ConfigDict(extra="forbid")
    attribute: str | None = Field(None, description="attribute parameter")
    params: dict[str, Any] | None = Field(None, description="params parameter")
    rule_type: productfeedrules_rule_type_enum_param | None = Field(
        None, description="rule_type parameter"
    )


class ProductFeedCreateSupplementaryFeedAssocParams(BaseModel):
    """Parameters for ProductFeed.create_supplementary_feed_assoc()."""

    model_config = ConfigDict(extra="forbid")
    assoc_data: list[dict[str, Any]] | None = Field(None, description="assoc_data parameter")


class ProductFeedCreateUploadScheduleParams(BaseModel):
    """Parameters for ProductFeed.create_upload_schedule()."""

    model_config = ConfigDict(extra="forbid")
    upload_schedule: str | None = Field(None, description="upload_schedule parameter")


class ProductFeedCreateUploadParams(BaseModel):
    """Parameters for ProductFeed.create_upload()."""

    model_config = ConfigDict(extra="forbid")
    fbe_external_business_id: str | None = Field(
        None, description="fbe_external_business_id parameter"
    )
    file: dict[str, Any] | None = Field(None, description="file parameter")
    password: str | None = Field(None, description="password parameter")
    update_only: bool | None = Field(None, description="update_only parameter")
    url: str | None = Field(None, description="url parameter")
    username: str | None = Field(None, description="username parameter")


class ProductFeedGetVehicleOffersParams(BaseModel):
    """Parameters for ProductFeed.get_vehicle_offers()."""

    model_config = ConfigDict(extra="forbid")
    bulk_pagination: bool | None = Field(None, description="bulk_pagination parameter")
    filter: dict[str, Any] | None = Field(None, description="filter parameter")


class ProductFeedGetVehiclesParams(BaseModel):
    """Parameters for ProductFeed.get_vehicles()."""

    model_config = ConfigDict(extra="forbid")
    bulk_pagination: bool | None = Field(None, description="bulk_pagination parameter")
    filter: dict[str, Any] | None = Field(None, description="filter parameter")
