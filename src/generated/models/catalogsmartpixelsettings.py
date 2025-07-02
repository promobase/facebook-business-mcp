"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .adspixel import AdsPixelFields
    from .productcatalog import ProductCatalogFields


# Field literal type
CatalogSmartPixelSettingsField = Literal[
    "allowed_domains",
    "available_property_filters",
    "catalog",
    "cbb_custom_override_filters",
    "cbb_default_filter",
    "defaults",
    "filters",
    "id",
    "is_cbb_enabled",
    "is_create_enabled",
    "is_delete_enabled",
    "is_update_enabled",
    "microdata_format_precedence",
    "pixel",
    "property_filter",
    "trusted_domains",
]


class CatalogSmartPixelSettingsFields(BaseModel):
    """Pydantic model for CatalogSmartPixelSettings fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    allowed_domains: list[str] = Field(None, alias="allowed_domains")
    available_property_filters: list[str] = Field(None, alias="available_property_filters")
    catalog: ProductCatalogFields = Field(None, alias="catalog")
    cbb_custom_override_filters: list[dict[str, Any]] = Field(
        None, alias="cbb_custom_override_filters"
    )
    cbb_default_filter: list[dict[str, list[str]]] = Field(None, alias="cbb_default_filter")
    defaults: list[dict[str, str]] = Field(None, alias="defaults")
    filters: list[dict[str, list[str]]] = Field(None, alias="filters")
    id: str = Field(None, alias="id")
    is_cbb_enabled: bool = Field(None, alias="is_cbb_enabled")
    is_create_enabled: bool = Field(None, alias="is_create_enabled")
    is_delete_enabled: bool = Field(None, alias="is_delete_enabled")
    is_update_enabled: bool = Field(None, alias="is_update_enabled")
    microdata_format_precedence: list[str] = Field(None, alias="microdata_format_precedence")
    pixel: AdsPixelFields = Field(None, alias="pixel")
    property_filter: list[str] = Field(None, alias="property_filter")
    trusted_domains: list[str] = Field(None, alias="trusted_domains")
