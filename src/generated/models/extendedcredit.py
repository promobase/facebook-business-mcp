"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .business import BusinessFields
    from .crmaddress import CRMAddressFields
    from .currencyamount import CurrencyAmountFields
    from .extendedcreditallocationconfig import ExtendedCreditAllocationConfigFields


class extendedcreditowning_credit_allocation_configs_partition_type_enum_param(str, Enum):
    """extendedcreditowning_credit_allocation_configs_partition_type_enum_param enum values."""

    AUTH = "AUTH"
    FIXED = "FIXED"
    FIXED_WITHOUT_PARTITION = "FIXED_WITHOUT_PARTITION"


class extendedcreditowning_credit_allocation_configs_send_bill_to_enum_param(str, Enum):
    """extendedcreditowning_credit_allocation_configs_send_bill_to_enum_param enum values."""

    VALUE_EMPTY = ""
    Advertiser = "Advertiser"
    Agency = "Agency"


class extendedcreditowning_credit_allocation_configs_liability_type_enum_param(str, Enum):
    """extendedcreditowning_credit_allocation_configs_liability_type_enum_param enum values."""

    VALUE_EMPTY = ""
    MSA = "MSA"
    Normal = "Normal"
    Sequential = "Sequential"


# Field literal type
ExtendedCreditField = Literal[
    "allocated_amount",
    "balance",
    "credit_available",
    "credit_type",
    "id",
    "is_access_revoked",
    "is_automated_experience",
    "legal_entity_name",
    "liable_address",
    "liable_biz_name",
    "max_balance",
    "online_max_balance",
    "owner_business",
    "owner_business_name",
    "partition_from",
    "receiving_credit_allocation_config",
    "send_bill_to_address",
    "send_bill_to_biz_name",
    "sold_to_address",
]


class ExtendedCreditFields(BaseModel):
    """Pydantic model for ExtendedCredit fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    allocated_amount: CurrencyAmountFields = Field(None, alias="allocated_amount")
    balance: CurrencyAmountFields = Field(None, alias="balance")
    credit_available: CurrencyAmountFields = Field(None, alias="credit_available")
    credit_type: str = Field(None, alias="credit_type")
    id: str = Field(None, alias="id")
    is_access_revoked: bool = Field(None, alias="is_access_revoked")
    is_automated_experience: bool = Field(None, alias="is_automated_experience")
    legal_entity_name: str = Field(None, alias="legal_entity_name")
    liable_address: CRMAddressFields = Field(None, alias="liable_address")
    liable_biz_name: str = Field(None, alias="liable_biz_name")
    max_balance: CurrencyAmountFields = Field(None, alias="max_balance")
    online_max_balance: CurrencyAmountFields = Field(None, alias="online_max_balance")
    owner_business: BusinessFields = Field(None, alias="owner_business")
    owner_business_name: str = Field(None, alias="owner_business_name")
    partition_from: str = Field(None, alias="partition_from")
    receiving_credit_allocation_config: ExtendedCreditAllocationConfigFields = Field(
        None, alias="receiving_credit_allocation_config"
    )
    send_bill_to_address: CRMAddressFields = Field(None, alias="send_bill_to_address")
    send_bill_to_biz_name: str = Field(None, alias="send_bill_to_biz_name")
    sold_to_address: CRMAddressFields = Field(None, alias="sold_to_address")


class ExtendedCreditCreateExtendedCreditInvoiceGroupParams(BaseModel):
    """Parameters for ExtendedCredit.create_extended_credit_invoice_group()."""

    model_config = ConfigDict(extra="forbid")
    emails: list[str] | None = Field(None, description="emails parameter")
    name: str | None = Field(None, description="name parameter")


class ExtendedCreditGetOwningCreditAllocationConfigsParams(BaseModel):
    """Parameters for ExtendedCredit.get_owning_credit_allocation_configs()."""

    model_config = ConfigDict(extra="forbid")
    receiving_business_id: str | None = Field(None, description="receiving_business_id parameter")


class ExtendedCreditCreateOwningCreditAllocationConfigParams(BaseModel):
    """Parameters for ExtendedCredit.create_owning_credit_allocation_config()."""

    model_config = ConfigDict(extra="forbid")
    amount: dict[str, Any] | None = Field(None, description="amount parameter")
    liability_type: (
        extendedcreditowning_credit_allocation_configs_liability_type_enum_param | None
    ) = Field(None, description="liability_type parameter")
    partition_type: (
        extendedcreditowning_credit_allocation_configs_partition_type_enum_param | None
    ) = Field(None, description="partition_type parameter")
    receiving_business_id: str | None = Field(None, description="receiving_business_id parameter")
    send_bill_to: extendedcreditowning_credit_allocation_configs_send_bill_to_enum_param | None = (
        Field(None, description="send_bill_to parameter")
    )


class ExtendedCreditCreateWhatsappCreditAttachParams(BaseModel):
    """Parameters for ExtendedCredit.create_whatsapp_credit_attach()."""

    model_config = ConfigDict(extra="forbid")
    waba_currency: str | None = Field(None, description="waba_currency parameter")
    waba_id: str | None = Field(None, description="waba_id parameter")


class ExtendedCreditCreateWhatsappCreditSharingParams(BaseModel):
    """Parameters for ExtendedCredit.create_whatsapp_credit_sharing()."""

    model_config = ConfigDict(extra="forbid")
    receiving_business_id: str | None = Field(None, description="receiving_business_id parameter")


class ExtendedCreditCreateWhatsappCreditSharingAndAttachParams(BaseModel):
    """Parameters for ExtendedCredit.create_whatsapp_credit_sharing_and_attach()."""

    model_config = ConfigDict(extra="forbid")
    waba_currency: str | None = Field(None, description="waba_currency parameter")
    waba_id: str | None = Field(None, description="waba_id parameter")
