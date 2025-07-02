"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .catalogitemapplinks import CatalogItemAppLinksFields
    from .catalogsubverticallist import CatalogSubVerticalListFields
    from .page import PageFields


class Vehicle_image_fetch_status(str, Enum):
    """Vehicle_image_fetch_status enum values."""

    DIRECT_UPLOAD = "DIRECT_UPLOAD"
    FETCHED = "FETCHED"
    FETCH_FAILED = "FETCH_FAILED"
    NO_STATUS = "NO_STATUS"
    OUTDATED = "OUTDATED"
    PARTIAL_FETCH = "PARTIAL_FETCH"


class Vehicle_visibility(str, Enum):
    """Vehicle_visibility enum values."""

    PUBLISHED = "PUBLISHED"
    STAGING = "STAGING"


class vehicleoverride_details_type_enum_param(str, Enum):
    """vehicleoverride_details_type_enum_param enum values."""

    COUNTRY = "COUNTRY"
    LANGUAGE = "LANGUAGE"
    LANGUAGE_AND_COUNTRY = "LANGUAGE_AND_COUNTRY"


# Field literal type
VehicleField = Literal[
    "address",
    "applinks",
    "availability",
    "availability_circle_radius",
    "availability_circle_radius_unit",
    "body_style",
    "category_specific_fields",
    "condition",
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
    "date_first_on_lot",
    "dealer_communication_channel",
    "dealer_email",
    "dealer_id",
    "dealer_name",
    "dealer_phone",
    "dealer_privacy_policy_url",
    "description",
    "drivetrain",
    "exterior_color",
    "fb_page_id",
    "features",
    "fuel_type",
    "id",
    "image_fetch_status",
    "images",
    "interior_color",
    "legal_disclosure_impressum_url",
    "make",
    "mileage",
    "model",
    "previous_currency",
    "previous_price",
    "price",
    "product_priority_0",
    "product_priority_1",
    "product_priority_2",
    "product_priority_3",
    "product_priority_4",
    "sale_currency",
    "sale_price",
    "sanitized_images",
    "state_of_vehicle",
    "tags",
    "title",
    "transmission",
    "trim",
    "unit_price",
    "url",
    "vehicle_id",
    "vehicle_registration_plate",
    "vehicle_specifications",
    "vehicle_type",
    "vin",
    "visibility",
    "year",
]


class VehicleFields(BaseModel):
    """Pydantic model for Vehicle fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    address: dict[str, Any] = Field(None, alias="address")
    applinks: CatalogItemAppLinksFields = Field(None, alias="applinks")
    availability: str = Field(None, alias="availability")
    availability_circle_radius: float = Field(None, alias="availability_circle_radius")
    availability_circle_radius_unit: str = Field(None, alias="availability_circle_radius_unit")
    body_style: str = Field(None, alias="body_style")
    category_specific_fields: CatalogSubVerticalListFields = Field(
        None, alias="category_specific_fields"
    )
    condition: str = Field(None, alias="condition")
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
    date_first_on_lot: str = Field(None, alias="date_first_on_lot")
    dealer_communication_channel: str = Field(None, alias="dealer_communication_channel")
    dealer_email: str = Field(None, alias="dealer_email")
    dealer_id: str = Field(None, alias="dealer_id")
    dealer_name: str = Field(None, alias="dealer_name")
    dealer_phone: str = Field(None, alias="dealer_phone")
    dealer_privacy_policy_url: str = Field(None, alias="dealer_privacy_policy_url")
    description: str = Field(None, alias="description")
    drivetrain: str = Field(None, alias="drivetrain")
    exterior_color: str = Field(None, alias="exterior_color")
    fb_page_id: PageFields = Field(None, alias="fb_page_id")
    features: list[dict[str, Any]] = Field(None, alias="features")
    fuel_type: str = Field(None, alias="fuel_type")
    id: str = Field(None, alias="id")
    image_fetch_status: dict[str, Any] = Field(None, alias="image_fetch_status")
    images: list[str] = Field(None, alias="images")
    interior_color: str = Field(None, alias="interior_color")
    legal_disclosure_impressum_url: str = Field(None, alias="legal_disclosure_impressum_url")
    make: str = Field(None, alias="make")
    mileage: dict[str, Any] = Field(None, alias="mileage")
    model: str = Field(None, alias="model")
    previous_currency: str = Field(None, alias="previous_currency")
    previous_price: str = Field(None, alias="previous_price")
    price: str = Field(None, alias="price")
    product_priority_0: float = Field(None, alias="product_priority_0")
    product_priority_1: float = Field(None, alias="product_priority_1")
    product_priority_2: float = Field(None, alias="product_priority_2")
    product_priority_3: float = Field(None, alias="product_priority_3")
    product_priority_4: float = Field(None, alias="product_priority_4")
    sale_currency: str = Field(None, alias="sale_currency")
    sale_price: str = Field(None, alias="sale_price")
    sanitized_images: list[str] = Field(None, alias="sanitized_images")
    state_of_vehicle: str = Field(None, alias="state_of_vehicle")
    tags: list[str] = Field(None, alias="tags")
    title: str = Field(None, alias="title")
    transmission: str = Field(None, alias="transmission")
    trim: str = Field(None, alias="trim")
    unit_price: dict[str, Any] = Field(None, alias="unit_price")
    url: str = Field(None, alias="url")
    vehicle_id: str = Field(None, alias="vehicle_id")
    vehicle_registration_plate: str = Field(None, alias="vehicle_registration_plate")
    vehicle_specifications: list[dict[str, Any]] = Field(None, alias="vehicle_specifications")
    vehicle_type: str = Field(None, alias="vehicle_type")
    vin: str = Field(None, alias="vin")
    visibility: dict[str, Any] = Field(None, alias="visibility")
    year: int = Field(None, alias="year")


class VehicleGetOverrideDetailsParams(BaseModel):
    """Parameters for Vehicle.get_override_details()."""

    model_config = ConfigDict(extra="forbid")
    keys: list[str] | None = Field(None, description="keys parameter")
    type: vehicleoverride_details_type_enum_param | None = Field(None, description="type parameter")
