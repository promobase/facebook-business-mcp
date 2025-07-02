"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
PageCTXDefaultGreetingTextField = Literal["ctd", "ctm", "ctwa"]


class PageCTXDefaultGreetingTextFields(BaseModel):
    """Pydantic model for PageCTXDefaultGreetingText fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    ctd: str = Field(None, alias="ctd")
    ctm: str = Field(None, alias="ctm")
    ctwa: str = Field(None, alias="ctwa")
