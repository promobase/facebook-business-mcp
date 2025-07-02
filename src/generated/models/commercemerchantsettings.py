"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .profile import ProfileFields


class commercemerchantsettingscommerce_orders_filters_enum_param(str, Enum):
    """commercemerchantsettingscommerce_orders_filters_enum_param enum values."""

    HAS_CANCELLATIONS = "HAS_CANCELLATIONS"
    HAS_FULFILLMENTS = "HAS_FULFILLMENTS"
    HAS_REFUNDS = "HAS_REFUNDS"
    NO_CANCELLATIONS = "NO_CANCELLATIONS"
    NO_REFUNDS = "NO_REFUNDS"
    NO_SHIPMENTS = "NO_SHIPMENTS"


class commercemerchantsettingscommerce_orders_state_enum_param(str, Enum):
    """commercemerchantsettingscommerce_orders_state_enum_param enum values."""

    COMPLETED = "COMPLETED"
    CREATED = "CREATED"
    FB_PROCESSING = "FB_PROCESSING"
    IN_PROGRESS = "IN_PROGRESS"


class commercemerchantsettingsreturns_statuses_enum_param(str, Enum):
    """commercemerchantsettingsreturns_statuses_enum_param enum values."""

    APPROVED = "APPROVED"
    DISAPPROVED = "DISAPPROVED"
    MERCHANT_MARKED_COMPLETED = "MERCHANT_MARKED_COMPLETED"
    REFUNDED = "REFUNDED"
    REQUESTED = "REQUESTED"


# Field literal type
CommerceMerchantSettingsField = Literal[
    "checkout_config",
    "checkout_message",
    "contact_email",
    "cta",
    "display_name",
    "facebook_channel",
    "id",
    "instagram_channel",
    "korea_ftc_listing",
    "merchant_page",
    "merchant_status",
    "onsite_commerce_merchant",
    "payment_provider",
    "privacy_policy_localized",
    "return_policy_localized",
    "review_rejection_messages",
    "review_rejection_reasons",
    "terms",
]


class CommerceMerchantSettingsFields(BaseModel):
    """Pydantic model for CommerceMerchantSettings fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    checkout_config: str = Field(None, alias="checkout_config")
    checkout_message: str = Field(None, alias="checkout_message")
    contact_email: str = Field(None, alias="contact_email")
    cta: str = Field(None, alias="cta")
    display_name: str = Field(None, alias="display_name")
    facebook_channel: dict[str, Any] = Field(None, alias="facebook_channel")
    id: str = Field(None, alias="id")
    instagram_channel: dict[str, Any] = Field(None, alias="instagram_channel")
    korea_ftc_listing: str = Field(None, alias="korea_ftc_listing")
    merchant_page: ProfileFields = Field(None, alias="merchant_page")
    merchant_status: str = Field(None, alias="merchant_status")
    onsite_commerce_merchant: dict[str, Any] = Field(None, alias="onsite_commerce_merchant")
    payment_provider: str = Field(None, alias="payment_provider")
    privacy_policy_localized: str = Field(None, alias="privacy_policy_localized")
    return_policy_localized: str = Field(None, alias="return_policy_localized")
    review_rejection_messages: list[str] = Field(None, alias="review_rejection_messages")
    review_rejection_reasons: list[str] = Field(None, alias="review_rejection_reasons")
    terms: str = Field(None, alias="terms")


class CommerceMerchantSettingsCreateAcknowledgeOrderParams(BaseModel):
    """Parameters for CommerceMerchantSettings.create_acknowledge_order()."""

    model_config = ConfigDict(extra="forbid")
    idempotency_key: str | None = Field(None, description="idempotency_key parameter")
    orders: list[dict[str, Any]] | None = Field(None, description="orders parameter")


class CommerceMerchantSettingsGetCommerceOrdersParams(BaseModel):
    """Parameters for CommerceMerchantSettings.get_commerce_orders()."""

    model_config = ConfigDict(extra="forbid")
    filters: list[commercemerchantsettingscommerce_orders_filters_enum_param] | None = Field(
        None, description="filters parameter"
    )
    state: list[commercemerchantsettingscommerce_orders_state_enum_param] | None = Field(
        None, description="state parameter"
    )
    updated_after: datetime | None = Field(None, description="updated_after parameter")
    updated_before: datetime | None = Field(None, description="updated_before parameter")


class CommerceMerchantSettingsGetCommercePayoutsParams(BaseModel):
    """Parameters for CommerceMerchantSettings.get_commerce_payouts()."""

    model_config = ConfigDict(extra="forbid")
    end_time: datetime | None = Field(None, description="end_time parameter")
    start_time: datetime | None = Field(None, description="start_time parameter")


class CommerceMerchantSettingsGetCommerceTransactionsParams(BaseModel):
    """Parameters for CommerceMerchantSettings.get_commerce_transactions()."""

    model_config = ConfigDict(extra="forbid")
    end_time: datetime | None = Field(None, description="end_time parameter")
    payout_reference_id: str | None = Field(None, description="payout_reference_id parameter")
    start_time: datetime | None = Field(None, description="start_time parameter")


class CommerceMerchantSettingsGetReturnsParams(BaseModel):
    """Parameters for CommerceMerchantSettings.get_returns()."""

    model_config = ConfigDict(extra="forbid")
    end_time_created: datetime | None = Field(None, description="end_time_created parameter")
    merchant_return_id: str | None = Field(None, description="merchant_return_id parameter")
    start_time_created: datetime | None = Field(None, description="start_time_created parameter")
    statuses: list[commercemerchantsettingsreturns_statuses_enum_param] | None = Field(
        None, description="statuses parameter"
    )


class CommerceMerchantSettingsGetShippingProfilesParams(BaseModel):
    """Parameters for CommerceMerchantSettings.get_shipping_profiles()."""

    model_config = ConfigDict(extra="forbid")
    reference_id: str | None = Field(None, description="reference_id parameter")


class CommerceMerchantSettingsCreateShippingProfileParams(BaseModel):
    """Parameters for CommerceMerchantSettings.create_shipping_profile()."""

    model_config = ConfigDict(extra="forbid")
    handling_time: dict[str, Any] | None = Field(None, description="handling_time parameter")
    is_default: bool | None = Field(None, description="is_default parameter")
    is_default_shipping_profile: bool | None = Field(
        None, description="is_default_shipping_profile parameter"
    )
    name: str | None = Field(None, description="name parameter")
    reference_id: str | None = Field(None, description="reference_id parameter")
    shipping_destinations: list[dict[str, Any]] | None = Field(
        None, description="shipping_destinations parameter"
    )
