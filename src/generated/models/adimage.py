"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .business import BusinessFields


class AdImage_status(str, Enum):
    """AdImage_status enum values."""

    ACTIVE = "ACTIVE"
    DELETED = "DELETED"
    INTERNAL = "INTERNAL"


# Field literal type
AdImageField = Literal[
    "account_id",
    "created_time",
    "creatives",
    "hash",
    "height",
    "id",
    "is_associated_creatives_in_adgroups",
    "name",
    "original_height",
    "original_width",
    "owner_business",
    "permalink_url",
    "status",
    "updated_time",
    "url",
    "url_128",
    "width",
]


class AdImageFields(BaseModel):
    """Pydantic model for AdImage fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    account_id: str = Field(None, alias="account_id")
    created_time: datetime = Field(None, alias="created_time")
    creatives: list[str] = Field(None, alias="creatives")
    hash: str = Field(None, alias="hash")
    height: int = Field(None, alias="height")
    id: str = Field(None, alias="id")
    is_associated_creatives_in_adgroups: bool = Field(
        None, alias="is_associated_creatives_in_adgroups"
    )
    name: str = Field(None, alias="name")
    original_height: int = Field(None, alias="original_height")
    original_width: int = Field(None, alias="original_width")
    owner_business: BusinessFields = Field(None, alias="owner_business")
    permalink_url: str = Field(None, alias="permalink_url")
    status: dict[str, Any] = Field(None, alias="status")
    updated_time: datetime = Field(None, alias="updated_time")
    url: str = Field(None, alias="url")
    url_128: str = Field(None, alias="url_128")
    width: int = Field(None, alias="width")
