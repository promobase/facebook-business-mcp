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


class HomeListing_image_fetch_status(str, Enum):
    """HomeListing_image_fetch_status enum values."""

    DIRECT_UPLOAD = "DIRECT_UPLOAD"
    FETCHED = "FETCHED"
    FETCH_FAILED = "FETCH_FAILED"
    NO_STATUS = "NO_STATUS"
    OUTDATED = "OUTDATED"
    PARTIAL_FETCH = "PARTIAL_FETCH"


class HomeListing_visibility(str, Enum):
    """HomeListing_visibility enum values."""

    PUBLISHED = "PUBLISHED"
    STAGING = "STAGING"


class homelistingoverride_details_type_enum_param(str, Enum):
    """homelistingoverride_details_type_enum_param enum values."""

    COUNTRY = "COUNTRY"
    LANGUAGE = "LANGUAGE"
    LANGUAGE_AND_COUNTRY = "LANGUAGE_AND_COUNTRY"


# Field literal type
HomeListingField = Literal[
    "ac_type",
    "additional_fees_description",
    "address",
    "agent_company",
    "agent_email",
    "agent_fb_page_id",
    "agent_name",
    "agent_phone",
    "applinks",
    "area_size",
    "area_unit",
    "availability",
    "category_specific_fields",
    "co_2_emission_rating_eu",
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
    "days_on_market",
    "description",
    "energy_rating_eu",
    "furnish_type",
    "group_id",
    "heating_type",
    "home_listing_id",
    "id",
    "image_fetch_status",
    "images",
    "laundry_type",
    "listing_type",
    "max_currency",
    "max_price",
    "min_currency",
    "min_price",
    "name",
    "num_baths",
    "num_beds",
    "num_rooms",
    "num_units",
    "parking_type",
    "partner_verification",
    "pet_policy",
    "price",
    "property_type",
    "sanitized_images",
    "securitydeposit_currency",
    "securitydeposit_price",
    "tags",
    "unit_price",
    "url",
    "visibility",
    "year_built",
]


class HomeListingFields(BaseModel):
    """Pydantic model for HomeListing fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    ac_type: str = Field(None, alias="ac_type")
    additional_fees_description: str = Field(None, alias="additional_fees_description")
    address: dict[str, Any] = Field(None, alias="address")
    agent_company: str = Field(None, alias="agent_company")
    agent_email: str = Field(None, alias="agent_email")
    agent_fb_page_id: PageFields = Field(None, alias="agent_fb_page_id")
    agent_name: str = Field(None, alias="agent_name")
    agent_phone: str = Field(None, alias="agent_phone")
    applinks: CatalogItemAppLinksFields = Field(None, alias="applinks")
    area_size: int = Field(None, alias="area_size")
    area_unit: str = Field(None, alias="area_unit")
    availability: str = Field(None, alias="availability")
    category_specific_fields: CatalogSubVerticalListFields = Field(
        None, alias="category_specific_fields"
    )
    co_2_emission_rating_eu: dict[str, Any] = Field(None, alias="co_2_emission_rating_eu")
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
    days_on_market: int = Field(None, alias="days_on_market")
    description: str = Field(None, alias="description")
    energy_rating_eu: dict[str, Any] = Field(None, alias="energy_rating_eu")
    furnish_type: str = Field(None, alias="furnish_type")
    group_id: str = Field(None, alias="group_id")
    heating_type: str = Field(None, alias="heating_type")
    home_listing_id: str = Field(None, alias="home_listing_id")
    id: str = Field(None, alias="id")
    image_fetch_status: dict[str, Any] = Field(None, alias="image_fetch_status")
    images: list[str] = Field(None, alias="images")
    laundry_type: str = Field(None, alias="laundry_type")
    listing_type: str = Field(None, alias="listing_type")
    max_currency: str = Field(None, alias="max_currency")
    max_price: str = Field(None, alias="max_price")
    min_currency: str = Field(None, alias="min_currency")
    min_price: str = Field(None, alias="min_price")
    name: str = Field(None, alias="name")
    num_baths: float = Field(None, alias="num_baths")
    num_beds: float = Field(None, alias="num_beds")
    num_rooms: float = Field(None, alias="num_rooms")
    num_units: int = Field(None, alias="num_units")
    parking_type: str = Field(None, alias="parking_type")
    partner_verification: str = Field(None, alias="partner_verification")
    pet_policy: str = Field(None, alias="pet_policy")
    price: str = Field(None, alias="price")
    property_type: str = Field(None, alias="property_type")
    sanitized_images: list[str] = Field(None, alias="sanitized_images")
    securitydeposit_currency: str = Field(None, alias="securitydeposit_currency")
    securitydeposit_price: str = Field(None, alias="securitydeposit_price")
    tags: list[str] = Field(None, alias="tags")
    unit_price: dict[str, Any] = Field(None, alias="unit_price")
    url: str = Field(None, alias="url")
    visibility: dict[str, Any] = Field(None, alias="visibility")
    year_built: int = Field(None, alias="year_built")


class HomeListingGetOverrideDetailsParams(BaseModel):
    """Parameters for HomeListing.get_override_details()."""

    model_config = ConfigDict(extra="forbid")
    keys: list[str] | None = Field(None, description="keys parameter")
    type: homelistingoverride_details_type_enum_param | None = Field(
        None, description="type parameter"
    )
