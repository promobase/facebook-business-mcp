"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .application import ApplicationFields
    from .currencyamount import CurrencyAmountFields
    from .user import UserFields


class paymentenginepaymentdispute_reason_enum_param(str, Enum):
    """paymentenginepaymentdispute_reason_enum_param enum values."""

    BANNED_USER = "BANNED_USER"
    DENIED_REFUND = "DENIED_REFUND"
    GRANTED_REPLACEMENT_ITEM = "GRANTED_REPLACEMENT_ITEM"


class paymentenginepaymentrefunds_reason_enum_param(str, Enum):
    """paymentenginepaymentrefunds_reason_enum_param enum values."""

    CUSTOMER_SERVICE = "CUSTOMER_SERVICE"
    FRIENDLY_FRAUD = "FRIENDLY_FRAUD"
    MALICIOUS_FRAUD = "MALICIOUS_FRAUD"


# Field literal type
PaymentEnginePaymentField = Literal[
    "actions",
    "application",
    "country",
    "created_time",
    "disputes",
    "fraud_status",
    "fulfillment_status",
    "id",
    "is_from_ad",
    "is_from_page_post",
    "items",
    "payout_foreign_exchange_rate",
    "phone_support_eligible",
    "platform",
    "refundable_amount",
    "request_id",
    "tax",
    "tax_country",
    "test",
    "user",
]


class PaymentEnginePaymentFields(BaseModel):
    """Pydantic model for PaymentEnginePayment fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    actions: list[dict[str, Any]] = Field(None, alias="actions")
    application: ApplicationFields = Field(None, alias="application")
    country: str = Field(None, alias="country")
    created_time: datetime = Field(None, alias="created_time")
    disputes: list[dict[str, Any]] = Field(None, alias="disputes")
    fraud_status: str = Field(None, alias="fraud_status")
    fulfillment_status: str = Field(None, alias="fulfillment_status")
    id: str = Field(None, alias="id")
    is_from_ad: bool = Field(None, alias="is_from_ad")
    is_from_page_post: bool = Field(None, alias="is_from_page_post")
    items: list[dict[str, Any]] = Field(None, alias="items")
    payout_foreign_exchange_rate: float = Field(None, alias="payout_foreign_exchange_rate")
    phone_support_eligible: bool = Field(None, alias="phone_support_eligible")
    platform: str = Field(None, alias="platform")
    refundable_amount: CurrencyAmountFields = Field(None, alias="refundable_amount")
    request_id: str = Field(None, alias="request_id")
    tax: str = Field(None, alias="tax")
    tax_country: str = Field(None, alias="tax_country")
    test: int = Field(None, alias="test")
    user: UserFields = Field(None, alias="user")


class PaymentEnginePaymentCreateDisputeParams(BaseModel):
    """Parameters for PaymentEnginePayment.create_dispute()."""

    model_config = ConfigDict(extra="forbid")
    reason: paymentenginepaymentdispute_reason_enum_param | None = Field(
        None, description="reason parameter"
    )


class PaymentEnginePaymentCreateRefundParams(BaseModel):
    """Parameters for PaymentEnginePayment.create_refund()."""

    model_config = ConfigDict(extra="forbid")
    amount: float | None = Field(None, description="amount parameter")
    currency: str | None = Field(None, description="currency parameter")
    reason: paymentenginepaymentrefunds_reason_enum_param | None = Field(
        None, description="reason parameter"
    )
