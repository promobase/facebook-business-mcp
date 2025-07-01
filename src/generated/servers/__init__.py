"""MCP servers for Facebook Business SDK resources."""

from .ad import ad_server
from .adaccount import adaccount_server
from .adcreative import adcreative_server
from .adimage import adimage_server
from .adset import adset_server
from .adspixel import adspixel_server
from .advideo import advideo_server
from .business import business_server
from .campaign import campaign_server
from .customaudience import customaudience_server
from .iguser import iguser_server
from .page import page_server
from .productcatalog import productcatalog_server
from .productfeed import productfeed_server
from .productset import productset_server

__all__ = [
    "ad_server",
    "adaccount_server",
    "adcreative_server",
    "adimage_server",
    "adset_server",
    "adspixel_server",
    "advideo_server",
    "business_server",
    "campaign_server",
    "customaudience_server",
    "iguser_server",
    "page_server",
    "productcatalog_server",
    "productfeed_server",
    "productset_server",
]
