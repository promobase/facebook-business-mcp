"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .mcominvoicedetails import McomInvoiceDetailsFields


# Field literal type
McomInvoiceListsField = Literal["invoice_details", "invoice_ids", "page_id"]


class McomInvoiceListsFields(BaseModel):
    """Pydantic model for McomInvoiceLists fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    invoice_details: list[McomInvoiceDetailsFields] = Field(None, alias="invoice_details")
    invoice_ids: list[str] = Field(None, alias="invoice_ids")
    page_id: str = Field(None, alias="page_id")
