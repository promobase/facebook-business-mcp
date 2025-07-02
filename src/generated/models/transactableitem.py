"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .catalogitemapplinks import CatalogItemAppLinksFields
    from .catalogsubverticallist import CatalogSubVerticalListFields


class TransactableItem_image_fetch_status(str, Enum):
    """TransactableItem_image_fetch_status enum values."""

    DIRECT_UPLOAD = "DIRECT_UPLOAD"
    FETCHED = "FETCHED"
    FETCH_FAILED = "FETCH_FAILED"
    NO_STATUS = "NO_STATUS"
    OUTDATED = "OUTDATED"
    PARTIAL_FETCH = "PARTIAL_FETCH"


class TransactableItem_visibility(str, Enum):
    """TransactableItem_visibility enum values."""

    PUBLISHED = "PUBLISHED"
    STAGING = "STAGING"


class transactableitemoverride_details_type_enum_param(str, Enum):
    """transactableitemoverride_details_type_enum_param enum values."""

    COUNTRY = "COUNTRY"
    LANGUAGE = "LANGUAGE"
    LANGUAGE_AND_COUNTRY = "LANGUAGE_AND_COUNTRY"


# Field literal type
TransactableItemField = Literal[
    "action_title",
    "applinks",
    "category_specific_fields",
    "currency",
    "description",
    "duration_time",
    "duration_type",
    "id",
    "image_fetch_status",
    "images",
    "order_index",
    "price",
    "price_type",
    "sanitized_images",
    "session_type",
    "time_padding_after_end",
    "title",
    "transactable_item_id",
    "url",
    "visibility",
]


class TransactableItemFields(BaseModel):
    """Pydantic model for TransactableItem fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    action_title: str = Field(None, alias="action_title")
    applinks: CatalogItemAppLinksFields = Field(None, alias="applinks")
    category_specific_fields: CatalogSubVerticalListFields = Field(
        None, alias="category_specific_fields"
    )
    currency: str = Field(None, alias="currency")
    description: str = Field(None, alias="description")
    duration_time: int = Field(None, alias="duration_time")
    duration_type: str = Field(None, alias="duration_type")
    id: str = Field(None, alias="id")
    image_fetch_status: dict[str, Any] = Field(None, alias="image_fetch_status")
    images: list[str] = Field(None, alias="images")
    order_index: int = Field(None, alias="order_index")
    price: str = Field(None, alias="price")
    price_type: str = Field(None, alias="price_type")
    sanitized_images: list[str] = Field(None, alias="sanitized_images")
    session_type: str = Field(None, alias="session_type")
    time_padding_after_end: int = Field(None, alias="time_padding_after_end")
    title: str = Field(None, alias="title")
    transactable_item_id: str = Field(None, alias="transactable_item_id")
    url: str = Field(None, alias="url")
    visibility: dict[str, Any] = Field(None, alias="visibility")


class TransactableItemGetOverrideDetailsParams(BaseModel):
    """Parameters for TransactableItem.get_override_details()."""

    model_config = ConfigDict(extra="forbid")
    keys: list[str] | None = Field(None, description="keys parameter")
    type: transactableitemoverride_details_type_enum_param | None = Field(
        None, description="type parameter"
    )
