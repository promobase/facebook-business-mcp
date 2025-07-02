"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .business import BusinessFields


class businessassetgroupassigned_users_page_tasks_enum_param(str, Enum):
    """businessassetgroupassigned_users_page_tasks_enum_param enum values."""

    ADVERTISE = "ADVERTISE"
    ANALYZE = "ANALYZE"
    CASHIER_ROLE = "CASHIER_ROLE"
    CREATE_CONTENT = "CREATE_CONTENT"
    GLOBAL_STRUCTURE_MANAGEMENT = "GLOBAL_STRUCTURE_MANAGEMENT"
    MANAGE = "MANAGE"
    MANAGE_JOBS = "MANAGE_JOBS"
    MANAGE_LEADS = "MANAGE_LEADS"
    MESSAGING = "MESSAGING"
    MODERATE = "MODERATE"
    MODERATE_COMMUNITY = "MODERATE_COMMUNITY"
    PAGES_MESSAGING = "PAGES_MESSAGING"
    PAGES_MESSAGING_SUBSCRIPTIONS = "PAGES_MESSAGING_SUBSCRIPTIONS"
    PROFILE_PLUS_ADVERTISE = "PROFILE_PLUS_ADVERTISE"
    PROFILE_PLUS_ANALYZE = "PROFILE_PLUS_ANALYZE"
    PROFILE_PLUS_CREATE_CONTENT = "PROFILE_PLUS_CREATE_CONTENT"
    PROFILE_PLUS_FACEBOOK_ACCESS = "PROFILE_PLUS_FACEBOOK_ACCESS"
    PROFILE_PLUS_FULL_CONTROL = "PROFILE_PLUS_FULL_CONTROL"
    PROFILE_PLUS_MANAGE = "PROFILE_PLUS_MANAGE"
    PROFILE_PLUS_MANAGE_LEADS = "PROFILE_PLUS_MANAGE_LEADS"
    PROFILE_PLUS_MESSAGING = "PROFILE_PLUS_MESSAGING"
    PROFILE_PLUS_MODERATE = "PROFILE_PLUS_MODERATE"
    PROFILE_PLUS_MODERATE_DELEGATE_COMMUNITY = "PROFILE_PLUS_MODERATE_DELEGATE_COMMUNITY"
    PROFILE_PLUS_REVENUE = "PROFILE_PLUS_REVENUE"
    READ_PAGE_MAILBOXES = "READ_PAGE_MAILBOXES"
    VIEW_MONETIZATION_INSIGHTS = "VIEW_MONETIZATION_INSIGHTS"


class businessassetgroupassigned_users_offline_conversion_data_set_tasks_enum_param(str, Enum):
    """businessassetgroupassigned_users_offline_conversion_data_set_tasks_enum_param enum values."""

    AA_ANALYZE = "AA_ANALYZE"
    ADVERTISE = "ADVERTISE"
    MANAGE = "MANAGE"
    UPLOAD = "UPLOAD"
    VIEW = "VIEW"


class businessassetgroupassigned_users_pixel_tasks_enum_param(str, Enum):
    """businessassetgroupassigned_users_pixel_tasks_enum_param enum values."""

    AA_ANALYZE = "AA_ANALYZE"
    ADVERTISE = "ADVERTISE"
    ANALYZE = "ANALYZE"
    EDIT = "EDIT"
    UPLOAD = "UPLOAD"


class businessassetgroupassigned_users_adaccount_tasks_enum_param(str, Enum):
    """businessassetgroupassigned_users_adaccount_tasks_enum_param enum values."""

    AA_ANALYZE = "AA_ANALYZE"
    ADVERTISE = "ADVERTISE"
    ANALYZE = "ANALYZE"
    DRAFT = "DRAFT"
    MANAGE = "MANAGE"


# Field literal type
BusinessAssetGroupField = Literal["id", "name", "owner_business"]


class BusinessAssetGroupFields(BaseModel):
    """Pydantic model for BusinessAssetGroup fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    id: str = Field(None, alias="id")
    name: str = Field(None, alias="name")
    owner_business: BusinessFields = Field(None, alias="owner_business")


class BusinessAssetGroupDeleteAssignedUsersParams(BaseModel):
    """Parameters for BusinessAssetGroup.delete_assigned_users()."""

    model_config = ConfigDict(extra="forbid")
    user: int | None = Field(None, description="user parameter")


class BusinessAssetGroupGetAssignedUsersParams(BaseModel):
    """Parameters for BusinessAssetGroup.get_assigned_users()."""

    model_config = ConfigDict(extra="forbid")
    business: str | None = Field(None, description="business parameter")


class BusinessAssetGroupCreateAssignedUserParams(BaseModel):
    """Parameters for BusinessAssetGroup.create_assigned_user()."""

    model_config = ConfigDict(extra="forbid")
    adaccount_tasks: list[businessassetgroupassigned_users_adaccount_tasks_enum_param] | None = (
        Field(None, description="adaccount_tasks parameter")
    )
    offline_conversion_data_set_tasks: (
        list[businessassetgroupassigned_users_offline_conversion_data_set_tasks_enum_param] | None
    ) = Field(None, description="offline_conversion_data_set_tasks parameter")
    page_tasks: list[businessassetgroupassigned_users_page_tasks_enum_param] | None = Field(
        None, description="page_tasks parameter"
    )
    pixel_tasks: list[businessassetgroupassigned_users_pixel_tasks_enum_param] | None = Field(
        None, description="pixel_tasks parameter"
    )
    user: int | None = Field(None, description="user parameter")


class BusinessAssetGroupDeleteContainedAdaccountsParams(BaseModel):
    """Parameters for BusinessAssetGroup.delete_contained_adaccounts()."""

    model_config = ConfigDict(extra="forbid")
    asset_id: str | None = Field(None, description="asset_id parameter")


class BusinessAssetGroupCreateContainedAdaccountParams(BaseModel):
    """Parameters for BusinessAssetGroup.create_contained_adaccount()."""

    model_config = ConfigDict(extra="forbid")
    asset_id: str | None = Field(None, description="asset_id parameter")


class BusinessAssetGroupDeleteContainedApplicationsParams(BaseModel):
    """Parameters for BusinessAssetGroup.delete_contained_applications()."""

    model_config = ConfigDict(extra="forbid")
    asset_id: str | None = Field(None, description="asset_id parameter")


class BusinessAssetGroupCreateContainedApplicationParams(BaseModel):
    """Parameters for BusinessAssetGroup.create_contained_application()."""

    model_config = ConfigDict(extra="forbid")
    asset_id: str | None = Field(None, description="asset_id parameter")


class BusinessAssetGroupDeleteContainedCustomConversionsParams(BaseModel):
    """Parameters for BusinessAssetGroup.delete_contained_custom_conversions()."""

    model_config = ConfigDict(extra="forbid")
    asset_id: str | None = Field(None, description="asset_id parameter")


class BusinessAssetGroupCreateContainedCustomConversionParams(BaseModel):
    """Parameters for BusinessAssetGroup.create_contained_custom_conversion()."""

    model_config = ConfigDict(extra="forbid")
    asset_id: str | None = Field(None, description="asset_id parameter")


class BusinessAssetGroupDeleteContainedInstagramAccountsParams(BaseModel):
    """Parameters for BusinessAssetGroup.delete_contained_instagram_accounts()."""

    model_config = ConfigDict(extra="forbid")
    asset_id: str | None = Field(None, description="asset_id parameter")


class BusinessAssetGroupCreateContainedInstagramAccountParams(BaseModel):
    """Parameters for BusinessAssetGroup.create_contained_instagram_account()."""

    model_config = ConfigDict(extra="forbid")
    asset_id: str | None = Field(None, description="asset_id parameter")


class BusinessAssetGroupDeleteContainedPagesParams(BaseModel):
    """Parameters for BusinessAssetGroup.delete_contained_pages()."""

    model_config = ConfigDict(extra="forbid")
    asset_id: str | None = Field(None, description="asset_id parameter")


class BusinessAssetGroupCreateContainedPageParams(BaseModel):
    """Parameters for BusinessAssetGroup.create_contained_page()."""

    model_config = ConfigDict(extra="forbid")
    asset_id: str | None = Field(None, description="asset_id parameter")


class BusinessAssetGroupDeleteContainedPixelsParams(BaseModel):
    """Parameters for BusinessAssetGroup.delete_contained_pixels()."""

    model_config = ConfigDict(extra="forbid")
    asset_id: str | None = Field(None, description="asset_id parameter")


class BusinessAssetGroupCreateContainedPixelParams(BaseModel):
    """Parameters for BusinessAssetGroup.create_contained_pixel()."""

    model_config = ConfigDict(extra="forbid")
    asset_id: str | None = Field(None, description="asset_id parameter")


class BusinessAssetGroupDeleteContainedProductCatalogsParams(BaseModel):
    """Parameters for BusinessAssetGroup.delete_contained_product_catalogs()."""

    model_config = ConfigDict(extra="forbid")
    asset_id: str | None = Field(None, description="asset_id parameter")


class BusinessAssetGroupCreateContainedProductCatalogParams(BaseModel):
    """Parameters for BusinessAssetGroup.create_contained_product_catalog()."""

    model_config = ConfigDict(extra="forbid")
    asset_id: str | None = Field(None, description="asset_id parameter")
