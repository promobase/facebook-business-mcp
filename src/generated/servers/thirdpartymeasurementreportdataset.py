"""ThirdPartyMeasurementReportDataset MCP Server with typed wrappers."""

from facebook_business.adobjects.thirdpartymeasurementreportdataset import (
    ThirdPartyMeasurementReportDataset,
)
from fastmcp import FastMCP

from src.generated.models.thirdpartymeasurementreportdataset import (
    ThirdPartyMeasurementReportDatasetField,
)
from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookThirdPartyMeasurementReportDataset"
instructions = """
ThirdPartyMeasurementReportDataset MCP Server for Facebook Business API.

Provides typed access to all ThirdPartyMeasurementReportDataset operations.
"""

thirdpartymeasurementreportdataset_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (1) ----
@thirdpartymeasurementreportdataset_server.tool
@wrapped_fn_tool
def get_thirdpartymeasurementreportdataset(
    thirdpartymeasurementreportdataset_id: str,
    fields: list[ThirdPartyMeasurementReportDatasetField] = [],
) -> str:
    """Get a ThirdPartyMeasurementReportDataset object by ID.

    Args:
        thirdpartymeasurementreportdataset_id: The ID of the ThirdPartyMeasurementReportDataset.
        fields: Fields to retrieve. Available fields: See ThirdPartyMeasurementReportDatasetField type.
    """
    obj = ThirdPartyMeasurementReportDataset(thirdpartymeasurementreportdataset_id)
    return obj.api_get(fields=fields)
