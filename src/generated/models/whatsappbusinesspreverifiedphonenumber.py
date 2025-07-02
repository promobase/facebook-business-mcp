"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .business import BusinessFields


class WhatsAppBusinessPreVerifiedPhoneNumber_code_verification_status(str, Enum):
    """WhatsAppBusinessPreVerifiedPhoneNumber_code_verification_status enum values."""

    EXPIRED = "EXPIRED"
    NOT_VERIFIED = "NOT_VERIFIED"
    VERIFIED = "VERIFIED"


class whatsappbusinesspreverifiedphonenumberrequest_code_code_method_enum_param(str, Enum):
    """whatsappbusinesspreverifiedphonenumberrequest_code_code_method_enum_param enum values."""

    SMS = "SMS"
    VOICE = "VOICE"


# Field literal type
WhatsAppBusinessPreVerifiedPhoneNumberField = Literal[
    "code_verification_status",
    "code_verification_time",
    "id",
    "owner_business",
    "phone_number",
    "verification_expiry_time",
]


class WhatsAppBusinessPreVerifiedPhoneNumberFields(BaseModel):
    """Pydantic model for WhatsAppBusinessPreVerifiedPhoneNumber fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    code_verification_status: dict[str, Any] = Field(None, alias="code_verification_status")
    code_verification_time: datetime = Field(None, alias="code_verification_time")
    id: str = Field(None, alias="id")
    owner_business: BusinessFields = Field(None, alias="owner_business")
    phone_number: str = Field(None, alias="phone_number")
    verification_expiry_time: datetime = Field(None, alias="verification_expiry_time")


class WhatsAppBusinessPreVerifiedPhoneNumberCreateRequestCodeParams(BaseModel):
    """Parameters for WhatsAppBusinessPreVerifiedPhoneNumber.create_request_code()."""

    model_config = ConfigDict(extra="forbid")
    code_method: (
        whatsappbusinesspreverifiedphonenumberrequest_code_code_method_enum_param | None
    ) = Field(None, description="code_method parameter")
    language: str | None = Field(None, description="language parameter")


class WhatsAppBusinessPreVerifiedPhoneNumberCreateVerifyCodeParams(BaseModel):
    """Parameters for WhatsAppBusinessPreVerifiedPhoneNumber.create_verify_code()."""

    model_config = ConfigDict(extra="forbid")
    code: str | None = Field(None, description="code parameter")
