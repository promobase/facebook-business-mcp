"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
CreditPartitionActionOptionsField = Literal["liability_type", "partition_type", "send_bill_to"]


class CreditPartitionActionOptionsFields(BaseModel):
    """Pydantic model for CreditPartitionActionOptions fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    liability_type: dict[str, Any] = Field(None, alias="liability_type")
    partition_type: dict[str, Any] = Field(None, alias="partition_type")
    send_bill_to: dict[str, Any] = Field(None, alias="send_bill_to")
