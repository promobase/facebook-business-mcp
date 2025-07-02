"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .aigeneratedproductimage import AIGeneratedProductImageFields
    from .catalogitemapplinks import CatalogItemAppLinksFields
    from .catalogsubverticallist import CatalogSubVerticalListFields
    from .productcatalog import ProductCatalogFields
    from .productfeed import ProductFeedFields
    from .productgroup import ProductGroupFields
    from .productitemcommerceinsights import ProductItemCommerceInsightsFields
    from .productitemerror import ProductItemErrorFields
    from .productitemimporteraddress import ProductItemImporterAddressFields
    from .productiteminvalidationerror import ProductItemInvalidationErrorFields
    from .productitemlocalinfo import ProductItemLocalInfoFields
    from .productitemvideodata import ProductItemVideoDataFields


class ProductItem_age_group(str, Enum):
    """ProductItem_age_group enum values."""

    adult = "adult"
    ALL_AGES = "all ages"
    infant = "infant"
    kids = "kids"
    newborn = "newborn"
    teen = "teen"
    toddler = "toddler"


class ProductItem_availability(str, Enum):
    """ProductItem_availability enum values."""

    AVAILABLE_FOR_ORDER = "available for order"
    discontinued = "discontinued"
    IN_STOCK = "in stock"
    mark_as_sold = "mark_as_sold"
    OUT_OF_STOCK = "out of stock"
    pending = "pending"
    preorder = "preorder"


class ProductItem_condition(str, Enum):
    """ProductItem_condition enum values."""

    cpo = "cpo"
    new = "new"
    open_box_new = "open_box_new"
    refurbished = "refurbished"
    used = "used"
    used_fair = "used_fair"
    used_good = "used_good"
    used_like_new = "used_like_new"


class ProductItem_gender(str, Enum):
    """ProductItem_gender enum values."""

    female = "female"
    male = "male"
    unisex = "unisex"


class ProductItem_image_fetch_status(str, Enum):
    """ProductItem_image_fetch_status enum values."""

    DIRECT_UPLOAD = "DIRECT_UPLOAD"
    FETCHED = "FETCHED"
    FETCH_FAILED = "FETCH_FAILED"
    NO_STATUS = "NO_STATUS"
    OUTDATED = "OUTDATED"
    PARTIAL_FETCH = "PARTIAL_FETCH"


class ProductItem_review_status(str, Enum):
    """ProductItem_review_status enum values."""

    VALUE_EMPTY = ""
    approved = "approved"
    outdated = "outdated"
    pending = "pending"
    rejected = "rejected"


class ProductItem_shipping_weight_unit(str, Enum):
    """ProductItem_shipping_weight_unit enum values."""

    g = "g"
    kg = "kg"
    lb = "lb"
    oz = "oz"


class ProductItem_video_fetch_status(str, Enum):
    """ProductItem_video_fetch_status enum values."""

    DIRECT_UPLOAD = "DIRECT_UPLOAD"
    FETCHED = "FETCHED"
    FETCH_FAILED = "FETCH_FAILED"
    NO_STATUS = "NO_STATUS"
    OUTDATED = "OUTDATED"
    PARTIAL_FETCH = "PARTIAL_FETCH"


class ProductItem_visibility(str, Enum):
    """ProductItem_visibility enum values."""

    published = "published"
    staging = "staging"


class productitemoverride_details_type_enum_param(str, Enum):
    """productitemoverride_details_type_enum_param enum values."""

    COUNTRY = "COUNTRY"
    LANGUAGE = "LANGUAGE"
    LANGUAGE_AND_COUNTRY = "LANGUAGE_AND_COUNTRY"


# Field literal type
ProductItemField = Literal[
    "additional_image_cdn_urls",
    "additional_image_urls",
    "additional_variant_attributes",
    "age_group",
    "applinks",
    "availability",
    "brand",
    "bundle_items",
    "bundle_retailer_ids",
    "capability_to_review_status",
    "category",
    "category_specific_fields",
    "color",
    "commerce_insights",
    "condition",
    "currency",
    "custom_data",
    "custom_label_0",
    "custom_label_1",
    "custom_label_2",
    "custom_label_3",
    "custom_label_4",
    "custom_number_0",
    "custom_number_1",
    "custom_number_2",
    "custom_number_3",
    "custom_number_4",
    "description",
    "errors",
    "expiration_date",
    "fb_product_category",
    "gender",
    "generated_background_images",
    "generated_background_images_ad_usage",
    "gtin",
    "id",
    "image_cdn_urls",
    "image_fetch_status",
    "image_url",
    "images",
    "importer_address",
    "importer_name",
    "invalidation_errors",
    "inventory",
    "is_bundle_hero",
    "manufacturer_info",
    "manufacturer_part_number",
    "marked_for_product_launch",
    "material",
    "mobile_link",
    "name",
    "ordering_index",
    "origin_country",
    "parent_product_id",
    "pattern",
    "post_conversion_signal_based_enforcement_appeal_eligibility",
    "price",
    "product_catalog",
    "product_feed",
    "product_group",
    "product_local_info",
    "product_relationship",
    "product_type",
    "quantity_to_sell_on_facebook",
    "retailer_id",
    "retailer_product_group_id",
    "review_rejection_reasons",
    "review_status",
    "sale_price",
    "sale_price_end_date",
    "sale_price_start_date",
    "shipping_weight_unit",
    "shipping_weight_value",
    "short_description",
    "size",
    "start_date",
    "tags",
    "url",
    "vendor_id",
    "video_fetch_status",
    "videos",
    "visibility",
    "wa_compliance_category",
]


class ProductItemFields(BaseModel):
    """Pydantic model for ProductItem fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    additional_image_cdn_urls: list[list[dict[str, str]]] = Field(
        None, alias="additional_image_cdn_urls"
    )
    additional_image_urls: list[str] = Field(None, alias="additional_image_urls")
    additional_variant_attributes: list[dict[str, str]] = Field(
        None, alias="additional_variant_attributes"
    )
    age_group: dict[str, Any] = Field(None, alias="age_group")
    applinks: CatalogItemAppLinksFields = Field(None, alias="applinks")
    availability: dict[str, Any] = Field(None, alias="availability")
    brand: str = Field(None, alias="brand")
    bundle_items: list[str] = Field(None, alias="bundle_items")
    bundle_retailer_ids: list[str] = Field(None, alias="bundle_retailer_ids")
    capability_to_review_status: list[dict[str, dict[str, Any]]] = Field(
        None, alias="capability_to_review_status"
    )
    category: str = Field(None, alias="category")
    category_specific_fields: CatalogSubVerticalListFields = Field(
        None, alias="category_specific_fields"
    )
    color: str = Field(None, alias="color")
    commerce_insights: ProductItemCommerceInsightsFields = Field(None, alias="commerce_insights")
    condition: dict[str, Any] = Field(None, alias="condition")
    currency: str = Field(None, alias="currency")
    custom_data: list[dict[str, str]] = Field(None, alias="custom_data")
    custom_label_0: str = Field(None, alias="custom_label_0")
    custom_label_1: str = Field(None, alias="custom_label_1")
    custom_label_2: str = Field(None, alias="custom_label_2")
    custom_label_3: str = Field(None, alias="custom_label_3")
    custom_label_4: str = Field(None, alias="custom_label_4")
    custom_number_0: str = Field(None, alias="custom_number_0")
    custom_number_1: str = Field(None, alias="custom_number_1")
    custom_number_2: str = Field(None, alias="custom_number_2")
    custom_number_3: str = Field(None, alias="custom_number_3")
    custom_number_4: str = Field(None, alias="custom_number_4")
    description: str = Field(None, alias="description")
    errors: list[ProductItemErrorFields] = Field(None, alias="errors")
    expiration_date: str = Field(None, alias="expiration_date")
    fb_product_category: str = Field(None, alias="fb_product_category")
    gender: dict[str, Any] = Field(None, alias="gender")
    generated_background_images: list[AIGeneratedProductImageFields] = Field(
        None, alias="generated_background_images"
    )
    generated_background_images_ad_usage: bool = Field(
        None, alias="generated_background_images_ad_usage"
    )
    gtin: str = Field(None, alias="gtin")
    id: str = Field(None, alias="id")
    image_cdn_urls: list[dict[str, str]] = Field(None, alias="image_cdn_urls")
    image_fetch_status: dict[str, Any] = Field(None, alias="image_fetch_status")
    image_url: str = Field(None, alias="image_url")
    images: list[str] = Field(None, alias="images")
    importer_address: ProductItemImporterAddressFields = Field(None, alias="importer_address")
    importer_name: str = Field(None, alias="importer_name")
    invalidation_errors: list[ProductItemInvalidationErrorFields] = Field(
        None, alias="invalidation_errors"
    )
    inventory: int = Field(None, alias="inventory")
    is_bundle_hero: bool = Field(None, alias="is_bundle_hero")
    manufacturer_info: str = Field(None, alias="manufacturer_info")
    manufacturer_part_number: str = Field(None, alias="manufacturer_part_number")
    marked_for_product_launch: str = Field(None, alias="marked_for_product_launch")
    material: str = Field(None, alias="material")
    mobile_link: str = Field(None, alias="mobile_link")
    name: str = Field(None, alias="name")
    ordering_index: int = Field(None, alias="ordering_index")
    origin_country: str = Field(None, alias="origin_country")
    parent_product_id: str = Field(None, alias="parent_product_id")
    pattern: str = Field(None, alias="pattern")
    post_conversion_signal_based_enforcement_appeal_eligibility: bool = Field(
        None, alias="post_conversion_signal_based_enforcement_appeal_eligibility"
    )
    price: str = Field(None, alias="price")
    product_catalog: ProductCatalogFields = Field(None, alias="product_catalog")
    product_feed: ProductFeedFields = Field(None, alias="product_feed")
    product_group: ProductGroupFields = Field(None, alias="product_group")
    product_local_info: ProductItemLocalInfoFields = Field(None, alias="product_local_info")
    product_relationship: str = Field(None, alias="product_relationship")
    product_type: str = Field(None, alias="product_type")
    quantity_to_sell_on_facebook: int = Field(None, alias="quantity_to_sell_on_facebook")
    retailer_id: str = Field(None, alias="retailer_id")
    retailer_product_group_id: str = Field(None, alias="retailer_product_group_id")
    review_rejection_reasons: list[str] = Field(None, alias="review_rejection_reasons")
    review_status: dict[str, Any] = Field(None, alias="review_status")
    sale_price: str = Field(None, alias="sale_price")
    sale_price_end_date: str = Field(None, alias="sale_price_end_date")
    sale_price_start_date: str = Field(None, alias="sale_price_start_date")
    shipping_weight_unit: dict[str, Any] = Field(None, alias="shipping_weight_unit")
    shipping_weight_value: float = Field(None, alias="shipping_weight_value")
    short_description: str = Field(None, alias="short_description")
    size: str = Field(None, alias="size")
    start_date: str = Field(None, alias="start_date")
    tags: list[str] = Field(None, alias="tags")
    url: str = Field(None, alias="url")
    vendor_id: str = Field(None, alias="vendor_id")
    video_fetch_status: dict[str, Any] = Field(None, alias="video_fetch_status")
    videos: list[ProductItemVideoDataFields] = Field(None, alias="videos")
    visibility: dict[str, Any] = Field(None, alias="visibility")
    wa_compliance_category: str = Field(None, alias="wa_compliance_category")


class ProductItemGetOverrideDetailsParams(BaseModel):
    """Parameters for ProductItem.get_override_details()."""

    model_config = ConfigDict(extra="forbid")
    keys: list[str] | None = Field(None, description="keys parameter")
    type: productitemoverride_details_type_enum_param | None = Field(
        None, description="type parameter"
    )
