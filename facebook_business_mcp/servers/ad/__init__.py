"""Ad server module."""

from .crud import (
    ad_api_create,
    ad_api_create_from_adaccount,
    ad_api_create_from_campaign,
    ad_api_delete,
    ad_api_get,
    ad_api_update,
)
from .operations import (
    CommonAdFields,
    ad_add_labels,
    ad_archive,
    ad_create_copy,
    ad_get_adcreatives,
    ad_get_copies,
    ad_get_insights,
    ad_get_leads,
    ad_get_previews,
    ad_get_targetingsentencelines,
    ad_pause,
    ad_resume,
)
from .server import server

__all__ = [
    # Server
    "server",
    # CRUD
    "ad_api_get",
    "ad_api_create",
    "ad_api_create_from_adaccount",
    "ad_api_create_from_campaign",
    "ad_api_update",
    "ad_api_delete",
    # Operations
    "ad_get_adcreatives",
    "ad_get_insights",
    "ad_get_targetingsentencelines",
    "ad_get_previews",
    "ad_get_leads",
    "ad_pause",
    "ad_resume",
    "ad_archive",
    "ad_add_labels",
    "ad_create_copy",
    "ad_get_copies",
    # Fields
    "CommonAdFields",
]
