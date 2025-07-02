"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .catalogitemapplinks import CatalogItemAppLinksFields
    from .catalogsubverticallist import CatalogSubVerticalListFields


class Flight_image_fetch_status(str, Enum):
    """Flight_image_fetch_status enum values."""

    DIRECT_UPLOAD = "DIRECT_UPLOAD"
    FETCHED = "FETCHED"
    FETCH_FAILED = "FETCH_FAILED"
    NO_STATUS = "NO_STATUS"
    OUTDATED = "OUTDATED"
    PARTIAL_FETCH = "PARTIAL_FETCH"


class Flight_visibility(str, Enum):
    """Flight_visibility enum values."""

    PUBLISHED = "PUBLISHED"
    STAGING = "STAGING"


class flightoverride_details_type_enum_param(str, Enum):
    """flightoverride_details_type_enum_param enum values."""

    COUNTRY = "COUNTRY"
    LANGUAGE = "LANGUAGE"
    LANGUAGE_AND_COUNTRY = "LANGUAGE_AND_COUNTRY"


# Field literal type
FlightField = Literal[
    "applinks",
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
    "destination_airport",
    "destination_city",
    "flight_id",
    "id",
    "image_fetch_status",
    "images",
    "oneway_currency",
    "oneway_price",
    "origin_airport",
    "origin_city",
    "price",
    "product_priority_0",
    "product_priority_1",
    "product_priority_2",
    "product_priority_3",
    "product_priority_4",
    "sanitized_images",
    "tags",
    "unit_price",
    "url",
    "visibility",
]


class FlightFields(BaseModel):
    """Pydantic model for Flight fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    applinks: CatalogItemAppLinksFields = Field(None, alias="applinks")
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
    destination_airport: str = Field(None, alias="destination_airport")
    destination_city: str = Field(None, alias="destination_city")
    flight_id: str = Field(None, alias="flight_id")
    id: str = Field(None, alias="id")
    image_fetch_status: dict[str, Any] = Field(None, alias="image_fetch_status")
    images: list[str] = Field(None, alias="images")
    oneway_currency: str = Field(None, alias="oneway_currency")
    oneway_price: str = Field(None, alias="oneway_price")
    origin_airport: str = Field(None, alias="origin_airport")
    origin_city: str = Field(None, alias="origin_city")
    price: str = Field(None, alias="price")
    product_priority_0: float = Field(None, alias="product_priority_0")
    product_priority_1: float = Field(None, alias="product_priority_1")
    product_priority_2: float = Field(None, alias="product_priority_2")
    product_priority_3: float = Field(None, alias="product_priority_3")
    product_priority_4: float = Field(None, alias="product_priority_4")
    sanitized_images: list[str] = Field(None, alias="sanitized_images")
    tags: list[str] = Field(None, alias="tags")
    unit_price: dict[str, Any] = Field(None, alias="unit_price")
    url: str = Field(None, alias="url")
    visibility: dict[str, Any] = Field(None, alias="visibility")


class FlightGetOverrideDetailsParams(BaseModel):
    """Parameters for Flight.get_override_details()."""

    model_config = ConfigDict(extra="forbid")
    keys: list[str] | None = Field(None, description="keys parameter")
    type: flightoverride_details_type_enum_param | None = Field(None, description="type parameter")
