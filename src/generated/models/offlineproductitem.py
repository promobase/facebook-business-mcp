"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .catalogitemapplinks import CatalogItemAppLinksFields
    from .catalogsubverticallist import CatalogSubVerticalListFields


class OfflineProductItem_image_fetch_status(str, Enum):
    """OfflineProductItem_image_fetch_status enum values."""

    DIRECT_UPLOAD = "DIRECT_UPLOAD"
    FETCHED = "FETCHED"
    FETCH_FAILED = "FETCH_FAILED"
    NO_STATUS = "NO_STATUS"
    OUTDATED = "OUTDATED"
    PARTIAL_FETCH = "PARTIAL_FETCH"


class OfflineProductItem_visibility(str, Enum):
    """OfflineProductItem_visibility enum values."""

    PUBLISHED = "PUBLISHED"
    STAGING = "STAGING"


class offlineproductitemoverride_details_type_enum_param(str, Enum):
    """offlineproductitemoverride_details_type_enum_param enum values."""

    COUNTRY = "COUNTRY"
    LANGUAGE = "LANGUAGE"
    LANGUAGE_AND_COUNTRY = "LANGUAGE_AND_COUNTRY"


# Field literal type
OfflineProductItemField = Literal[
    "applinks",
    "brand",
    "category",
    "category_specific_fields",
    "currency",
    "description",
    "id",
    "image_fetch_status",
    "image_url",
    "images",
    "name",
    "offline_product_item_id",
    "price",
    "sanitized_images",
    "url",
    "visibility",
]


class OfflineProductItemFields(BaseModel):
    """Pydantic model for OfflineProductItem fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    applinks: CatalogItemAppLinksFields = Field(None, alias="applinks")
    brand: str = Field(None, alias="brand")
    category: str = Field(None, alias="category")
    category_specific_fields: CatalogSubVerticalListFields = Field(
        None, alias="category_specific_fields"
    )
    currency: str = Field(None, alias="currency")
    description: str = Field(None, alias="description")
    id: str = Field(None, alias="id")
    image_fetch_status: dict[str, Any] = Field(None, alias="image_fetch_status")
    image_url: str = Field(None, alias="image_url")
    images: list[str] = Field(None, alias="images")
    name: str = Field(None, alias="name")
    offline_product_item_id: str = Field(None, alias="offline_product_item_id")
    price: str = Field(None, alias="price")
    sanitized_images: list[str] = Field(None, alias="sanitized_images")
    url: str = Field(None, alias="url")
    visibility: dict[str, Any] = Field(None, alias="visibility")


class OfflineProductItemGetOverrideDetailsParams(BaseModel):
    """Parameters for OfflineProductItem.get_override_details()."""

    model_config = ConfigDict(extra="forbid")
    keys: list[str] | None = Field(None, description="keys parameter")
    type: offlineproductitemoverride_details_type_enum_param | None = Field(
        None, description="type parameter"
    )
