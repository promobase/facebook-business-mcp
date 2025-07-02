"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .apppublisher import AppPublisherFields
    from .webpublisher import WebPublisherFields


# Field literal type
PublisherBlockListField = Literal[
    "app_publishers",
    "business_owner_id",
    "id",
    "is_auto_blocking_on",
    "is_eligible_at_campaign_level",
    "last_update_time",
    "last_update_user",
    "name",
    "owner_ad_account_id",
    "web_publishers",
]


class PublisherBlockListFields(BaseModel):
    """Pydantic model for PublisherBlockList fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    app_publishers: list[AppPublisherFields] = Field(None, alias="app_publishers")
    business_owner_id: str = Field(None, alias="business_owner_id")
    id: str = Field(None, alias="id")
    is_auto_blocking_on: bool = Field(None, alias="is_auto_blocking_on")
    is_eligible_at_campaign_level: bool = Field(None, alias="is_eligible_at_campaign_level")
    last_update_time: datetime = Field(None, alias="last_update_time")
    last_update_user: str = Field(None, alias="last_update_user")
    name: str = Field(None, alias="name")
    owner_ad_account_id: str = Field(None, alias="owner_ad_account_id")
    web_publishers: list[WebPublisherFields] = Field(None, alias="web_publishers")


class PublisherBlockListCreateAppendPublisherUrlParams(BaseModel):
    """Parameters for PublisherBlockList.create_append_publisher_url()."""

    model_config = ConfigDict(extra="forbid")
    publisher_urls: list[str] | None = Field(None, description="publisher_urls parameter")


class PublisherBlockListGetPagedWebPublishersParams(BaseModel):
    """Parameters for PublisherBlockList.get_paged_web_publishers()."""

    model_config = ConfigDict(extra="forbid")
    draft_id: str | None = Field(None, description="draft_id parameter")
