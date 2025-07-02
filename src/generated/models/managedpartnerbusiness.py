"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .adaccount import AdAccountFields
    from .managedpartnerextendedcredit import ManagedPartnerExtendedCreditFields
    from .page import PageFields
    from .productcatalog import ProductCatalogFields


# Field literal type
ManagedPartnerBusinessField = Literal[
    "ad_account",
    "catalog_segment",
    "extended_credit",
    "page",
    "seller_business_info",
    "seller_business_status",
    "template",
]


class ManagedPartnerBusinessFields(BaseModel):
    """Pydantic model for ManagedPartnerBusiness fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    ad_account: AdAccountFields = Field(None, alias="ad_account")
    catalog_segment: ProductCatalogFields = Field(None, alias="catalog_segment")
    extended_credit: ManagedPartnerExtendedCreditFields = Field(None, alias="extended_credit")
    page: PageFields = Field(None, alias="page")
    seller_business_info: dict[str, Any] = Field(None, alias="seller_business_info")
    seller_business_status: str = Field(None, alias="seller_business_status")
    template: list[dict[str, Any]] = Field(None, alias="template")
