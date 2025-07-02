"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .adspixel import AdsPixelFields
    from .application import ApplicationFields
    from .offlineconversiondataset import OfflineConversionDataSetFields
    from .page import PageFields
    from .productcatalog import ProductCatalogFields


# Field literal type
PartnerIntegrationLinkedField = Literal[
    "ads_pixel",
    "application",
    "completed_integration_types",
    "external_business_connection_id",
    "external_id",
    "has_oauth_token",
    "id",
    "mbe_app_id",
    "mbe_asset_id",
    "mbe_external_business_id",
    "name",
    "offline_conversion_data_set",
    "page",
    "partner",
    "product_catalog",
    "setup_status",
]


class PartnerIntegrationLinkedFields(BaseModel):
    """Pydantic model for PartnerIntegrationLinked fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    ads_pixel: AdsPixelFields = Field(None, alias="ads_pixel")
    application: ApplicationFields = Field(None, alias="application")
    completed_integration_types: list[str] = Field(None, alias="completed_integration_types")
    external_business_connection_id: str = Field(None, alias="external_business_connection_id")
    external_id: str = Field(None, alias="external_id")
    has_oauth_token: bool = Field(None, alias="has_oauth_token")
    id: str = Field(None, alias="id")
    mbe_app_id: str = Field(None, alias="mbe_app_id")
    mbe_asset_id: str = Field(None, alias="mbe_asset_id")
    mbe_external_business_id: str = Field(None, alias="mbe_external_business_id")
    name: str = Field(None, alias="name")
    offline_conversion_data_set: OfflineConversionDataSetFields = Field(
        None, alias="offline_conversion_data_set"
    )
    page: PageFields = Field(None, alias="page")
    partner: str = Field(None, alias="partner")
    product_catalog: ProductCatalogFields = Field(None, alias="product_catalog")
    setup_status: str = Field(None, alias="setup_status")
