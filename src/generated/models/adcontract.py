"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
AdContractField = Literal[
    "account_id",
    "account_mgr_fbid",
    "account_mgr_name",
    "adops_person_name",
    "advertiser_address_fbid",
    "advertiser_fbid",
    "advertiser_name",
    "agency_discount",
    "agency_name",
    "bill_to_address_fbid",
    "bill_to_fbid",
    "campaign_name",
    "created_by",
    "created_date",
    "customer_io",
    "io_number",
    "io_terms",
    "io_type",
    "last_updated_by",
    "last_updated_date",
    "max_end_date",
    "mdc_fbid",
    "media_plan_number",
    "min_start_date",
    "msa_contract",
    "payment_terms",
    "rev_hold_flag",
    "rev_hold_released_by",
    "rev_hold_released_on",
    "salesrep_fbid",
    "salesrep_name",
    "sold_to_address_fbid",
    "sold_to_fbid",
    "status",
    "subvertical",
    "thirdparty_billed",
    "thirdparty_uid",
    "thirdparty_url",
    "vat_country",
    "version",
    "vertical",
]


class AdContractFields(BaseModel):
    """Pydantic model for AdContract fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    account_id: str = Field(None, alias="account_id")
    account_mgr_fbid: str = Field(None, alias="account_mgr_fbid")
    account_mgr_name: str = Field(None, alias="account_mgr_name")
    adops_person_name: str = Field(None, alias="adops_person_name")
    advertiser_address_fbid: str = Field(None, alias="advertiser_address_fbid")
    advertiser_fbid: str = Field(None, alias="advertiser_fbid")
    advertiser_name: str = Field(None, alias="advertiser_name")
    agency_discount: float = Field(None, alias="agency_discount")
    agency_name: str = Field(None, alias="agency_name")
    bill_to_address_fbid: str = Field(None, alias="bill_to_address_fbid")
    bill_to_fbid: str = Field(None, alias="bill_to_fbid")
    campaign_name: str = Field(None, alias="campaign_name")
    created_by: str = Field(None, alias="created_by")
    created_date: int = Field(None, alias="created_date")
    customer_io: str = Field(None, alias="customer_io")
    io_number: int = Field(None, alias="io_number")
    io_terms: str = Field(None, alias="io_terms")
    io_type: str = Field(None, alias="io_type")
    last_updated_by: str = Field(None, alias="last_updated_by")
    last_updated_date: int = Field(None, alias="last_updated_date")
    max_end_date: int = Field(None, alias="max_end_date")
    mdc_fbid: str = Field(None, alias="mdc_fbid")
    media_plan_number: str = Field(None, alias="media_plan_number")
    min_start_date: int = Field(None, alias="min_start_date")
    msa_contract: str = Field(None, alias="msa_contract")
    payment_terms: str = Field(None, alias="payment_terms")
    rev_hold_flag: bool = Field(None, alias="rev_hold_flag")
    rev_hold_released_by: int = Field(None, alias="rev_hold_released_by")
    rev_hold_released_on: int = Field(None, alias="rev_hold_released_on")
    salesrep_fbid: str = Field(None, alias="salesrep_fbid")
    salesrep_name: str = Field(None, alias="salesrep_name")
    sold_to_address_fbid: str = Field(None, alias="sold_to_address_fbid")
    sold_to_fbid: str = Field(None, alias="sold_to_fbid")
    status: str = Field(None, alias="status")
    subvertical: str = Field(None, alias="subvertical")
    thirdparty_billed: int = Field(None, alias="thirdparty_billed")
    thirdparty_uid: str = Field(None, alias="thirdparty_uid")
    thirdparty_url: str = Field(None, alias="thirdparty_url")
    vat_country: str = Field(None, alias="vat_country")
    version: int = Field(None, alias="version")
    vertical: str = Field(None, alias="vertical")
