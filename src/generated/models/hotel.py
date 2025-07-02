"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .catalogitemapplinks import CatalogItemAppLinksFields
    from .catalogsubverticallist import CatalogSubVerticalListFields


class Hotel_image_fetch_status(str, Enum):
    """Hotel_image_fetch_status enum values."""

    DIRECT_UPLOAD = "DIRECT_UPLOAD"
    FETCHED = "FETCHED"
    FETCH_FAILED = "FETCH_FAILED"
    NO_STATUS = "NO_STATUS"
    OUTDATED = "OUTDATED"
    PARTIAL_FETCH = "PARTIAL_FETCH"


class Hotel_visibility(str, Enum):
    """Hotel_visibility enum values."""

    PUBLISHED = "PUBLISHED"
    STAGING = "STAGING"


class hoteloverride_details_type_enum_param(str, Enum):
    """hoteloverride_details_type_enum_param enum values."""

    COUNTRY = "COUNTRY"
    LANGUAGE = "LANGUAGE"
    LANGUAGE_AND_COUNTRY = "LANGUAGE_AND_COUNTRY"


# Field literal type
HotelField = Literal[
    "address",
    "applinks",
    "brand",
    "category",
    "category_specific_fields",
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
    "guest_ratings",
    "hotel_id",
    "id",
    "image_fetch_status",
    "images",
    "lowest_base_price",
    "loyalty_program",
    "margin_level",
    "name",
    "phone",
    "product_priority_0",
    "product_priority_1",
    "product_priority_2",
    "product_priority_3",
    "product_priority_4",
    "sale_price",
    "sanitized_images",
    "star_rating",
    "tags",
    "unit_price",
    "url",
    "visibility",
]


class HotelFields(BaseModel):
    """Pydantic model for Hotel fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    address: str = Field(None, alias="address")
    applinks: CatalogItemAppLinksFields = Field(None, alias="applinks")
    brand: str = Field(None, alias="brand")
    category: str = Field(None, alias="category")
    category_specific_fields: CatalogSubVerticalListFields = Field(
        None, alias="category_specific_fields"
    )
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
    guest_ratings: str = Field(None, alias="guest_ratings")
    hotel_id: str = Field(None, alias="hotel_id")
    id: str = Field(None, alias="id")
    image_fetch_status: dict[str, Any] = Field(None, alias="image_fetch_status")
    images: list[str] = Field(None, alias="images")
    lowest_base_price: str = Field(None, alias="lowest_base_price")
    loyalty_program: str = Field(None, alias="loyalty_program")
    margin_level: int = Field(None, alias="margin_level")
    name: str = Field(None, alias="name")
    phone: str = Field(None, alias="phone")
    product_priority_0: float = Field(None, alias="product_priority_0")
    product_priority_1: float = Field(None, alias="product_priority_1")
    product_priority_2: float = Field(None, alias="product_priority_2")
    product_priority_3: float = Field(None, alias="product_priority_3")
    product_priority_4: float = Field(None, alias="product_priority_4")
    sale_price: str = Field(None, alias="sale_price")
    sanitized_images: list[str] = Field(None, alias="sanitized_images")
    star_rating: float = Field(None, alias="star_rating")
    tags: list[str] = Field(None, alias="tags")
    unit_price: dict[str, Any] = Field(None, alias="unit_price")
    url: str = Field(None, alias="url")
    visibility: dict[str, Any] = Field(None, alias="visibility")


class HotelGetOverrideDetailsParams(BaseModel):
    """Parameters for Hotel.get_override_details()."""

    model_config = ConfigDict(extra="forbid")
    keys: list[str] | None = Field(None, description="keys parameter")
    type: hoteloverride_details_type_enum_param | None = Field(None, description="type parameter")
