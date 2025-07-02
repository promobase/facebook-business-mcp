"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
WearableDevicePublicKeyField = Literal[
    "base64_encoded_public_key",
    "creation_time_on_device",
    "device_uuid",
    "id",
    "key_type",
    "owner_id",
    "product_use_case",
    "version",
]


class WearableDevicePublicKeyFields(BaseModel):
    """Pydantic model for WearableDevicePublicKey fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    base64_encoded_public_key: str = Field(None, alias="base64_encoded_public_key")
    creation_time_on_device: datetime = Field(None, alias="creation_time_on_device")
    device_uuid: str = Field(None, alias="device_uuid")
    id: str = Field(None, alias="id")
    key_type: str = Field(None, alias="key_type")
    owner_id: str = Field(None, alias="owner_id")
    product_use_case: str = Field(None, alias="product_use_case")
    version: str = Field(None, alias="version")
