"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
CTWAWhatsAppNumbersInfoField = Literal[
    "can_manage_wa_flows",
    "formatted_whatsapp_number",
    "is_business_number",
    "is_calling_enabled",
    "number_country_prefix",
    "page_whatsapp_number_id",
    "waba_id",
    "whatsapp_number",
    "whatsapp_smb_device",
]


class CTWAWhatsAppNumbersInfoFields(BaseModel):
    """Pydantic model for CTWAWhatsAppNumbersInfo fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    can_manage_wa_flows: bool = Field(None, alias="can_manage_wa_flows")
    formatted_whatsapp_number: str = Field(None, alias="formatted_whatsapp_number")
    is_business_number: bool = Field(None, alias="is_business_number")
    is_calling_enabled: bool = Field(None, alias="is_calling_enabled")
    number_country_prefix: str = Field(None, alias="number_country_prefix")
    page_whatsapp_number_id: str = Field(None, alias="page_whatsapp_number_id")
    waba_id: str = Field(None, alias="waba_id")
    whatsapp_number: str = Field(None, alias="whatsapp_number")
    whatsapp_smb_device: str = Field(None, alias="whatsapp_smb_device")
