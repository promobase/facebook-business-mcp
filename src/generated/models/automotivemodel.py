"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .catalogitemapplinks import CatalogItemAppLinksFields
    from .catalogsubverticallist import CatalogSubVerticalListFields


class AutomotiveModel_image_fetch_status(str, Enum):
    """AutomotiveModel_image_fetch_status enum values."""

    DIRECT_UPLOAD = "DIRECT_UPLOAD"
    FETCHED = "FETCHED"
    FETCH_FAILED = "FETCH_FAILED"
    NO_STATUS = "NO_STATUS"
    OUTDATED = "OUTDATED"
    PARTIAL_FETCH = "PARTIAL_FETCH"


class AutomotiveModel_visibility(str, Enum):
    """AutomotiveModel_visibility enum values."""

    PUBLISHED = "PUBLISHED"
    STAGING = "STAGING"


class automotivemodeloverride_details_type_enum_param(str, Enum):
    """automotivemodeloverride_details_type_enum_param enum values."""

    COUNTRY = "COUNTRY"
    LANGUAGE = "LANGUAGE"
    LANGUAGE_AND_COUNTRY = "LANGUAGE_AND_COUNTRY"


# Field literal type
AutomotiveModelField = Literal[
    "applinks",
    "automotive_model_id",
    "availability",
    "body_style",
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
    "drivetrain",
    "exterior_color",
    "finance_description",
    "finance_type",
    "fuel_type",
    "generation",
    "id",
    "image_fetch_status",
    "images",
    "interior_color",
    "interior_upholstery",
    "make",
    "model",
    "price",
    "sanitized_images",
    "title",
    "transmission",
    "trim",
    "unit_price",
    "url",
    "visibility",
    "year",
]


class AutomotiveModelFields(BaseModel):
    """Pydantic model for AutomotiveModel fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    applinks: CatalogItemAppLinksFields = Field(None, alias="applinks")
    automotive_model_id: str = Field(None, alias="automotive_model_id")
    availability: str = Field(None, alias="availability")
    body_style: str = Field(None, alias="body_style")
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
    drivetrain: str = Field(None, alias="drivetrain")
    exterior_color: str = Field(None, alias="exterior_color")
    finance_description: str = Field(None, alias="finance_description")
    finance_type: str = Field(None, alias="finance_type")
    fuel_type: str = Field(None, alias="fuel_type")
    generation: str = Field(None, alias="generation")
    id: str = Field(None, alias="id")
    image_fetch_status: dict[str, Any] = Field(None, alias="image_fetch_status")
    images: list[str] = Field(None, alias="images")
    interior_color: str = Field(None, alias="interior_color")
    interior_upholstery: str = Field(None, alias="interior_upholstery")
    make: str = Field(None, alias="make")
    model: str = Field(None, alias="model")
    price: str = Field(None, alias="price")
    sanitized_images: list[str] = Field(None, alias="sanitized_images")
    title: str = Field(None, alias="title")
    transmission: str = Field(None, alias="transmission")
    trim: str = Field(None, alias="trim")
    unit_price: dict[str, Any] = Field(None, alias="unit_price")
    url: str = Field(None, alias="url")
    visibility: dict[str, Any] = Field(None, alias="visibility")
    year: int = Field(None, alias="year")


class AutomotiveModelGetOverrideDetailsParams(BaseModel):
    """Parameters for AutomotiveModel.get_override_details()."""

    model_config = ConfigDict(extra="forbid")
    keys: list[str] | None = Field(None, description="keys parameter")
    type: automotivemodeloverride_details_type_enum_param | None = Field(
        None, description="type parameter"
    )
