"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .application import ApplicationFields
    from .paymentenginepayment import PaymentEnginePaymentFields
    from .user import UserFields


# Field literal type
PaymentSubscriptionField = Literal[
    "amount",
    "app_param_data",
    "application",
    "billing_period",
    "canceled_reason",
    "created_time",
    "currency",
    "id",
    "last_payment",
    "next_bill_time",
    "next_period_amount",
    "next_period_currency",
    "next_period_product",
    "payment_status",
    "pending_cancel",
    "period_start_time",
    "product",
    "status",
    "test",
    "trial_amount",
    "trial_currency",
    "trial_expiry_time",
    "updated_time",
    "user",
]


class PaymentSubscriptionFields(BaseModel):
    """Pydantic model for PaymentSubscription fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    amount: str = Field(None, alias="amount")
    app_param_data: str = Field(None, alias="app_param_data")
    application: ApplicationFields = Field(None, alias="application")
    billing_period: str = Field(None, alias="billing_period")
    canceled_reason: str = Field(None, alias="canceled_reason")
    created_time: datetime = Field(None, alias="created_time")
    currency: str = Field(None, alias="currency")
    id: str = Field(None, alias="id")
    last_payment: PaymentEnginePaymentFields = Field(None, alias="last_payment")
    next_bill_time: datetime = Field(None, alias="next_bill_time")
    next_period_amount: str = Field(None, alias="next_period_amount")
    next_period_currency: str = Field(None, alias="next_period_currency")
    next_period_product: str = Field(None, alias="next_period_product")
    payment_status: str = Field(None, alias="payment_status")
    pending_cancel: bool = Field(None, alias="pending_cancel")
    period_start_time: datetime = Field(None, alias="period_start_time")
    product: str = Field(None, alias="product")
    status: str = Field(None, alias="status")
    test: int = Field(None, alias="test")
    trial_amount: str = Field(None, alias="trial_amount")
    trial_currency: str = Field(None, alias="trial_currency")
    trial_expiry_time: datetime = Field(None, alias="trial_expiry_time")
    updated_time: datetime = Field(None, alias="updated_time")
    user: UserFields = Field(None, alias="user")
