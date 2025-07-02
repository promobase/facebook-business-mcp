"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .catalogitemapplinks import CatalogItemAppLinksFields
    from .catalogsubverticallist import CatalogSubVerticalListFields


class VehicleOffer_image_fetch_status(str, Enum):
    """VehicleOffer_image_fetch_status enum values."""

    DIRECT_UPLOAD = "DIRECT_UPLOAD"
    FETCHED = "FETCHED"
    FETCH_FAILED = "FETCH_FAILED"
    NO_STATUS = "NO_STATUS"
    OUTDATED = "OUTDATED"
    PARTIAL_FETCH = "PARTIAL_FETCH"


class VehicleOffer_visibility(str, Enum):
    """VehicleOffer_visibility enum values."""

    PUBLISHED = "PUBLISHED"
    STAGING = "STAGING"


class vehicleofferoverride_details_type_enum_param(str, Enum):
    """vehicleofferoverride_details_type_enum_param enum values."""

    COUNTRY = "COUNTRY"
    LANGUAGE = "LANGUAGE"
    LANGUAGE_AND_COUNTRY = "LANGUAGE_AND_COUNTRY"


# Field literal type
VehicleOfferField = Literal[
    "amount_currency",
    "amount_percentage",
    "amount_price",
    "amount_qualifier",
    "applinks",
    "availability",
    "body_style",
    "cashback_currency",
    "cashback_price",
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
    "dma_codes",
    "downpayment_currency",
    "downpayment_price",
    "downpayment_qualifier",
    "drivetrain",
    "end_date",
    "end_time",
    "exterior_color",
    "fuel_type",
    "generation",
    "id",
    "image_fetch_status",
    "images",
    "interior_color",
    "interior_upholstery",
    "make",
    "model",
    "offer_description",
    "offer_disclaimer",
    "offer_type",
    "price",
    "product_priority_0",
    "product_priority_1",
    "product_priority_2",
    "product_priority_3",
    "product_priority_4",
    "sanitized_images",
    "start_date",
    "start_time",
    "tags",
    "term_length",
    "term_qualifier",
    "title",
    "transmission",
    "trim",
    "unit_price",
    "url",
    "vehicle_offer_id",
    "visibility",
    "year",
]


class VehicleOfferFields(BaseModel):
    """Pydantic model for VehicleOffer fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    amount_currency: str = Field(None, alias="amount_currency")
    amount_percentage: float = Field(None, alias="amount_percentage")
    amount_price: str = Field(None, alias="amount_price")
    amount_qualifier: str = Field(None, alias="amount_qualifier")
    applinks: CatalogItemAppLinksFields = Field(None, alias="applinks")
    availability: str = Field(None, alias="availability")
    body_style: str = Field(None, alias="body_style")
    cashback_currency: str = Field(None, alias="cashback_currency")
    cashback_price: str = Field(None, alias="cashback_price")
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
    dma_codes: list[str] = Field(None, alias="dma_codes")
    downpayment_currency: str = Field(None, alias="downpayment_currency")
    downpayment_price: str = Field(None, alias="downpayment_price")
    downpayment_qualifier: str = Field(None, alias="downpayment_qualifier")
    drivetrain: str = Field(None, alias="drivetrain")
    end_date: str = Field(None, alias="end_date")
    end_time: int = Field(None, alias="end_time")
    exterior_color: str = Field(None, alias="exterior_color")
    fuel_type: str = Field(None, alias="fuel_type")
    generation: str = Field(None, alias="generation")
    id: str = Field(None, alias="id")
    image_fetch_status: dict[str, Any] = Field(None, alias="image_fetch_status")
    images: list[str] = Field(None, alias="images")
    interior_color: str = Field(None, alias="interior_color")
    interior_upholstery: str = Field(None, alias="interior_upholstery")
    make: str = Field(None, alias="make")
    model: str = Field(None, alias="model")
    offer_description: str = Field(None, alias="offer_description")
    offer_disclaimer: str = Field(None, alias="offer_disclaimer")
    offer_type: str = Field(None, alias="offer_type")
    price: str = Field(None, alias="price")
    product_priority_0: float = Field(None, alias="product_priority_0")
    product_priority_1: float = Field(None, alias="product_priority_1")
    product_priority_2: float = Field(None, alias="product_priority_2")
    product_priority_3: float = Field(None, alias="product_priority_3")
    product_priority_4: float = Field(None, alias="product_priority_4")
    sanitized_images: list[str] = Field(None, alias="sanitized_images")
    start_date: str = Field(None, alias="start_date")
    start_time: int = Field(None, alias="start_time")
    tags: list[str] = Field(None, alias="tags")
    term_length: int = Field(None, alias="term_length")
    term_qualifier: str = Field(None, alias="term_qualifier")
    title: str = Field(None, alias="title")
    transmission: str = Field(None, alias="transmission")
    trim: str = Field(None, alias="trim")
    unit_price: dict[str, Any] = Field(None, alias="unit_price")
    url: str = Field(None, alias="url")
    vehicle_offer_id: str = Field(None, alias="vehicle_offer_id")
    visibility: dict[str, Any] = Field(None, alias="visibility")
    year: int = Field(None, alias="year")


class VehicleOfferGetOverrideDetailsParams(BaseModel):
    """Parameters for VehicleOffer.get_override_details()."""

    model_config = ConfigDict(extra="forbid")
    keys: list[str] | None = Field(None, description="keys parameter")
    type: vehicleofferoverride_details_type_enum_param | None = Field(
        None, description="type parameter"
    )
