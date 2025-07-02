"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .adspixel import AdsPixelFields
    from .audiencepermissionforactions import AudiencePermissionForActionsFields
    from .business import BusinessFields
    from .customaudiencedatasource import CustomAudienceDataSourceFields
    from .customaudiencesharingstatus import CustomAudienceSharingStatusFields
    from .customaudiencestatus import CustomAudienceStatusFields
    from .lookalikespec import LookalikeSpecFields


# Field literal type
CustomAudienceField = Literal[
    "account_id",
    "approximate_count_lower_bound",
    "approximate_count_upper_bound",
    "customer_file_source",
    "data_source",
    "data_source_types",
    "datafile_custom_audience_uploading_status",
    "delete_time",
    "delivery_status",
    "description",
    "excluded_custom_audiences",
    "external_event_source",
    "household_audience",
    "id",
    "included_custom_audiences",
    "is_eligible_for_sac_campaigns",
    "is_household",
    "is_snapshot",
    "is_value_based",
    "lookalike_audience_ids",
    "lookalike_spec",
    "name",
    "operation_status",
    "opt_out_link",
    "owner_business",
    "page_deletion_marked_delete_time",
    "permission_for_actions",
    "pixel_id",
    "regulated_audience_spec",
    "retention_days",
    "rev_share_policy_id",
    "rule",
    "rule_aggregation",
    "rule_v2",
    "seed_audience",
    "sharing_status",
    "subtype",
    "time_content_updated",
    "time_created",
    "time_updated",
]


class CustomAudienceFields(BaseModel):
    """Pydantic model for CustomAudience fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    account_id: str = Field(None, alias="account_id")
    approximate_count_lower_bound: int = Field(None, alias="approximate_count_lower_bound")
    approximate_count_upper_bound: int = Field(None, alias="approximate_count_upper_bound")
    customer_file_source: str = Field(None, alias="customer_file_source")
    data_source: CustomAudienceDataSourceFields = Field(None, alias="data_source")
    data_source_types: str = Field(None, alias="data_source_types")
    datafile_custom_audience_uploading_status: str = Field(
        None, alias="datafile_custom_audience_uploading_status"
    )
    delete_time: int = Field(None, alias="delete_time")
    delivery_status: CustomAudienceStatusFields = Field(None, alias="delivery_status")
    description: str = Field(None, alias="description")
    excluded_custom_audiences: list[CustomAudienceFields] = Field(
        None, alias="excluded_custom_audiences"
    )
    external_event_source: AdsPixelFields = Field(None, alias="external_event_source")
    household_audience: int = Field(None, alias="household_audience")
    id: str = Field(None, alias="id")
    included_custom_audiences: list[CustomAudienceFields] = Field(
        None, alias="included_custom_audiences"
    )
    is_eligible_for_sac_campaigns: bool = Field(None, alias="is_eligible_for_sac_campaigns")
    is_household: bool = Field(None, alias="is_household")
    is_snapshot: bool = Field(None, alias="is_snapshot")
    is_value_based: bool = Field(None, alias="is_value_based")
    lookalike_audience_ids: list[str] = Field(None, alias="lookalike_audience_ids")
    lookalike_spec: LookalikeSpecFields = Field(None, alias="lookalike_spec")
    name: str = Field(None, alias="name")
    operation_status: CustomAudienceStatusFields = Field(None, alias="operation_status")
    opt_out_link: str = Field(None, alias="opt_out_link")
    owner_business: BusinessFields = Field(None, alias="owner_business")
    page_deletion_marked_delete_time: int = Field(None, alias="page_deletion_marked_delete_time")
    permission_for_actions: AudiencePermissionForActionsFields = Field(
        None, alias="permission_for_actions"
    )
    pixel_id: str = Field(None, alias="pixel_id")
    regulated_audience_spec: LookalikeSpecFields = Field(None, alias="regulated_audience_spec")
    retention_days: int = Field(None, alias="retention_days")
    rev_share_policy_id: int = Field(None, alias="rev_share_policy_id")
    rule: str = Field(None, alias="rule")
    rule_aggregation: str = Field(None, alias="rule_aggregation")
    rule_v2: str = Field(None, alias="rule_v2")
    seed_audience: int = Field(None, alias="seed_audience")
    sharing_status: CustomAudienceSharingStatusFields = Field(None, alias="sharing_status")
    subtype: str = Field(None, alias="subtype")
    time_content_updated: int = Field(None, alias="time_content_updated")
    time_created: int = Field(None, alias="time_created")
    time_updated: int = Field(None, alias="time_updated")


class CustomAudienceDeleteAdaccountsParams(BaseModel):
    """Parameters for CustomAudience.delete_adaccounts()."""

    model_config = ConfigDict(extra="forbid")
    adaccounts: list[str] | None = Field(None, description="adaccounts parameter")


class CustomAudienceGetAdaccountsParams(BaseModel):
    """Parameters for CustomAudience.get_adaccounts()."""

    model_config = ConfigDict(extra="forbid")
    permissions: str | None = Field(None, description="permissions parameter")


class CustomAudienceCreateAdaccountParams(BaseModel):
    """Parameters for CustomAudience.create_adaccount()."""

    model_config = ConfigDict(extra="forbid")
    adaccounts: list[str] | None = Field(None, description="adaccounts parameter")
    permissions: str | None = Field(None, description="permissions parameter")
    relationship_type: list[str] | None = Field(None, description="relationship_type parameter")
    replace: bool | None = Field(None, description="replace parameter")


class CustomAudienceGetAdsParams(BaseModel):
    """Parameters for CustomAudience.get_ads()."""

    model_config = ConfigDict(extra="forbid")
    effective_status: list[str] | None = Field(None, description="effective_status parameter")
    status: list[str] | None = Field(None, description="status parameter")


class CustomAudienceGetHealthParams(BaseModel):
    """Parameters for CustomAudience.get_health()."""

    model_config = ConfigDict(extra="forbid")
    calculated_date: str | None = Field(None, description="calculated_date parameter")
    processed_date: str | None = Field(None, description="processed_date parameter")
    value_aggregation_duration: int | None = Field(
        None, description="value_aggregation_duration parameter"
    )
    value_country: str | None = Field(None, description="value_country parameter")
    value_currency: str | None = Field(None, description="value_currency parameter")
    value_version: int | None = Field(None, description="value_version parameter")


class CustomAudienceGetSaltsParams(BaseModel):
    """Parameters for CustomAudience.get_salts()."""

    model_config = ConfigDict(extra="forbid")
    params: list[str] | None = Field(None, description="params parameter")


class CustomAudienceCreateSaltParams(BaseModel):
    """Parameters for CustomAudience.create_salt()."""

    model_config = ConfigDict(extra="forbid")
    salt: str | None = Field(None, description="salt parameter")
    valid_from: datetime | None = Field(None, description="valid_from parameter")
    valid_to: datetime | None = Field(None, description="valid_to parameter")


class CustomAudienceGetSessionsParams(BaseModel):
    """Parameters for CustomAudience.get_sessions()."""

    model_config = ConfigDict(extra="forbid")
    session_id: int | None = Field(None, description="session_id parameter")


class CustomAudienceDeleteUsersParams(BaseModel):
    """Parameters for CustomAudience.delete_users()."""

    model_config = ConfigDict(extra="forbid")
    namespace: str | None = Field(None, description="namespace parameter")
    payload: dict[str, Any] | None = Field(None, description="payload parameter")
    session: dict[str, Any] | None = Field(None, description="session parameter")


class CustomAudienceCreateUserParams(BaseModel):
    """Parameters for CustomAudience.create_user()."""

    model_config = ConfigDict(extra="forbid")
    namespace: str | None = Field(None, description="namespace parameter")
    payload: dict[str, Any] | None = Field(None, description="payload parameter")
    session: dict[str, Any] | None = Field(None, description="session parameter")


class CustomAudienceCreateUsersreplaceParams(BaseModel):
    """Parameters for CustomAudience.create_usersreplace()."""

    model_config = ConfigDict(extra="forbid")
    namespace: str | None = Field(None, description="namespace parameter")
    payload: dict[str, Any] | None = Field(None, description="payload parameter")
    session: dict[str, Any] | None = Field(None, description="session parameter")
