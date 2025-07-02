"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .catalogitemapplinks import CatalogItemAppLinksFields
    from .catalogsubverticallist import CatalogSubVerticalListFields
    from .productitemlocalinfo import ProductItemLocalInfoFields


class LocalServiceBusiness_availability(str, Enum):
    """LocalServiceBusiness_availability enum values."""

    AVAILABLE_FOR_ORDER = "AVAILABLE_FOR_ORDER"
    DISCONTINUED = "DISCONTINUED"
    IN_STOCK = "IN_STOCK"
    MARK_AS_SOLD = "MARK_AS_SOLD"
    OUT_OF_STOCK = "OUT_OF_STOCK"
    PENDING = "PENDING"
    PREORDER = "PREORDER"


class LocalServiceBusiness_condition(str, Enum):
    """LocalServiceBusiness_condition enum values."""

    PC_CPO = "PC_CPO"
    PC_NEW = "PC_NEW"
    PC_OPEN_BOX_NEW = "PC_OPEN_BOX_NEW"
    PC_REFURBISHED = "PC_REFURBISHED"
    PC_USED = "PC_USED"
    PC_USED_FAIR = "PC_USED_FAIR"
    PC_USED_GOOD = "PC_USED_GOOD"
    PC_USED_LIKE_NEW = "PC_USED_LIKE_NEW"


class LocalServiceBusiness_image_fetch_status(str, Enum):
    """LocalServiceBusiness_image_fetch_status enum values."""

    DIRECT_UPLOAD = "DIRECT_UPLOAD"
    FETCHED = "FETCHED"
    FETCH_FAILED = "FETCH_FAILED"
    NO_STATUS = "NO_STATUS"
    OUTDATED = "OUTDATED"
    PARTIAL_FETCH = "PARTIAL_FETCH"


class LocalServiceBusiness_visibility(str, Enum):
    """LocalServiceBusiness_visibility enum values."""

    PUBLISHED = "PUBLISHED"
    STAGING = "STAGING"


class localservicebusinessoverride_details_type_enum_param(str, Enum):
    """localservicebusinessoverride_details_type_enum_param enum values."""

    COUNTRY = "COUNTRY"
    LANGUAGE = "LANGUAGE"
    LANGUAGE_AND_COUNTRY = "LANGUAGE_AND_COUNTRY"


# Field literal type
LocalServiceBusinessField = Literal[
    "address",
    "applinks",
    "availability",
    "brand",
    "category",
    "category_specific_fields",
    "condition",
    "cuisine_type",
    "currency",
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
    "expiration_date",
    "gtin",
    "id",
    "image_fetch_status",
    "images",
    "local_info",
    "local_service_business_id",
    "main_local_info",
    "phone",
    "price",
    "price_range",
    "retailer_category",
    "sanitized_images",
    "size",
    "tags",
    "title",
    "unit_price",
    "url",
    "vendor_id",
    "visibility",
]


class LocalServiceBusinessFields(BaseModel):
    """Pydantic model for LocalServiceBusiness fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    address: dict[str, Any] = Field(None, alias="address")
    applinks: CatalogItemAppLinksFields = Field(None, alias="applinks")
    availability: dict[str, Any] = Field(None, alias="availability")
    brand: str = Field(None, alias="brand")
    category: str = Field(None, alias="category")
    category_specific_fields: CatalogSubVerticalListFields = Field(
        None, alias="category_specific_fields"
    )
    condition: dict[str, Any] = Field(None, alias="condition")
    cuisine_type: str = Field(None, alias="cuisine_type")
    currency: str = Field(None, alias="currency")
    custom_label_0: str = Field(None, alias="custom_label_0")
    custom_label_1: str = Field(None, alias="custom_label_1")
    custom_label_2: str = Field(None, alias="custom_label_2")
    custom_label_3: str = Field(None, alias="custom_label_3")
    custom_label_4: str = Field(None, alias="custom_label_4")
    custom_number_0: int = Field(None, alias="custom_number_0")
    custom_number_1: int = Field(None, alias="custom_number_1")
    custom_number_2: int = Field(None, alias="custom_number_2")
    custom_number_3: int = Field(None, alias="custom_number_3")
    custom_number_4: int = Field(None, alias="custom_number_4")
    description: str = Field(None, alias="description")
    expiration_date: str = Field(None, alias="expiration_date")
    gtin: str = Field(None, alias="gtin")
    id: str = Field(None, alias="id")
    image_fetch_status: dict[str, Any] = Field(None, alias="image_fetch_status")
    images: list[str] = Field(None, alias="images")
    local_info: ProductItemLocalInfoFields = Field(None, alias="local_info")
    local_service_business_id: str = Field(None, alias="local_service_business_id")
    main_local_info: ProductItemLocalInfoFields = Field(None, alias="main_local_info")
    phone: str = Field(None, alias="phone")
    price: str = Field(None, alias="price")
    price_range: str = Field(None, alias="price_range")
    retailer_category: str = Field(None, alias="retailer_category")
    sanitized_images: list[str] = Field(None, alias="sanitized_images")
    size: str = Field(None, alias="size")
    tags: list[str] = Field(None, alias="tags")
    title: str = Field(None, alias="title")
    unit_price: dict[str, Any] = Field(None, alias="unit_price")
    url: str = Field(None, alias="url")
    vendor_id: str = Field(None, alias="vendor_id")
    visibility: dict[str, Any] = Field(None, alias="visibility")


class LocalServiceBusinessGetOverrideDetailsParams(BaseModel):
    """Parameters for LocalServiceBusiness.get_override_details()."""

    model_config = ConfigDict(extra="forbid")
    keys: list[str] | None = Field(None, description="keys parameter")
    type: localservicebusinessoverride_details_type_enum_param | None = Field(
        None, description="type parameter"
    )
