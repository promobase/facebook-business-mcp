"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .profile import ProfileFields


# Field literal type
CopyrightOwnershipTransferField = Literal[
    "id",
    "receiving_rights_holder",
    "sending_rights_holder",
    "status",
    "transfer_territories",
    "transfer_time",
]


class CopyrightOwnershipTransferFields(BaseModel):
    """Pydantic model for CopyrightOwnershipTransfer fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    id: str = Field(None, alias="id")
    receiving_rights_holder: ProfileFields = Field(None, alias="receiving_rights_holder")
    sending_rights_holder: ProfileFields = Field(None, alias="sending_rights_holder")
    status: str = Field(None, alias="status")
    transfer_territories: list[str] = Field(None, alias="transfer_territories")
    transfer_time: datetime = Field(None, alias="transfer_time")
