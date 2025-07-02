"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
OpenBridgeConfigurationField = Literal[
    "active",
    "cloud_provider",
    "cloud_region",
    "destination_id",
    "endpoint",
    "fallback_domain",
    "first_party_domain",
    "host_business_id",
    "id",
    "instance_id",
    "instance_version",
    "is_sgw_instance",
    "is_sgw_pixel_from_meta_pixel",
    "partner_name",
    "pixel_id",
    "sgw_account_id",
    "sgw_instance_url",
    "sgw_pixel_id",
]


class OpenBridgeConfigurationFields(BaseModel):
    """Pydantic model for OpenBridgeConfiguration fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    active: bool = Field(None, alias="active")
    cloud_provider: str = Field(None, alias="cloud_provider")
    cloud_region: str = Field(None, alias="cloud_region")
    destination_id: str = Field(None, alias="destination_id")
    endpoint: str = Field(None, alias="endpoint")
    fallback_domain: str = Field(None, alias="fallback_domain")
    first_party_domain: str = Field(None, alias="first_party_domain")
    host_business_id: str = Field(None, alias="host_business_id")
    id: str = Field(None, alias="id")
    instance_id: str = Field(None, alias="instance_id")
    instance_version: str = Field(None, alias="instance_version")
    is_sgw_instance: bool = Field(None, alias="is_sgw_instance")
    is_sgw_pixel_from_meta_pixel: bool = Field(None, alias="is_sgw_pixel_from_meta_pixel")
    partner_name: str = Field(None, alias="partner_name")
    pixel_id: str = Field(None, alias="pixel_id")
    sgw_account_id: str = Field(None, alias="sgw_account_id")
    sgw_instance_url: str = Field(None, alias="sgw_instance_url")
    sgw_pixel_id: str = Field(None, alias="sgw_pixel_id")
