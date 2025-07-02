"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
AdAccountAllPaymentMethodsField = Literal[""]  # No fields defined


class AdAccountAllPaymentMethodsFields(BaseModel):
    """Pydantic model for AdAccountAllPaymentMethods fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    pass  # No fields defined
