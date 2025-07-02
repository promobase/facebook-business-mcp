"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .adaccount import AdAccountFields
    from .business import BusinessFields
    from .page import PageFields
    from .user import UserFields


# Field literal type
FranchiseProgramMemberField = Literal[
    "business",
    "end_date",
    "id",
    "join_date",
    "member_ad_account",
    "member_user",
    "membership_status",
    "page",
]


class FranchiseProgramMemberFields(BaseModel):
    """Pydantic model for FranchiseProgramMember fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    business: BusinessFields = Field(None, alias="business")
    end_date: datetime = Field(None, alias="end_date")
    id: str = Field(None, alias="id")
    join_date: datetime = Field(None, alias="join_date")
    member_ad_account: AdAccountFields = Field(None, alias="member_ad_account")
    member_user: UserFields = Field(None, alias="member_user")
    membership_status: str = Field(None, alias="membership_status")
    page: PageFields = Field(None, alias="page")
