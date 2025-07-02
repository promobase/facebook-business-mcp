"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .adaccount import AdAccountFields
    from .user import UserFields


# Field literal type
AdColumnSizesField = Literal[
    "admarket_account", "app_id", "columns", "id", "owner", "page", "report", "tab", "view"
]


class AdColumnSizesFields(BaseModel):
    """Pydantic model for AdColumnSizes fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    admarket_account: AdAccountFields = Field(None, alias="admarket_account")
    app_id: str = Field(None, alias="app_id")
    columns: list[dict[str, str]] = Field(None, alias="columns")
    id: str = Field(None, alias="id")
    owner: UserFields = Field(None, alias="owner")
    page: str = Field(None, alias="page")
    report: str = Field(None, alias="report")
    tab: str = Field(None, alias="tab")
    view: str = Field(None, alias="view")
