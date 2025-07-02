"""BusinessAssetGroup MCP Server with typed wrappers."""

from facebook_business.adobjects.businessassetgroup import BusinessAssetGroup
from fastmcp import FastMCP

from src.generated.models.abstractcrudobject import AbstractCrudObjectField
from src.generated.models.assigneduser import AssignedUserField
from src.generated.models.businessassetgroup import (
    BusinessAssetGroupCreateAssignedUserParams,
    BusinessAssetGroupCreateContainedAdAccountParams,
    BusinessAssetGroupCreateContainedApplicationParams,
    BusinessAssetGroupCreateContainedCustomConversionParams,
    BusinessAssetGroupCreateContainedInstagramAccountParams,
    BusinessAssetGroupCreateContainedPageParams,
    BusinessAssetGroupCreateContainedPixelParams,
    BusinessAssetGroupCreateContainedProductCatalogParams,
    BusinessAssetGroupDeleteAssignedUsersParams,
    BusinessAssetGroupDeleteContainedAdAccountsParams,
    BusinessAssetGroupDeleteContainedApplicationsParams,
    BusinessAssetGroupDeleteContainedCustomConversionsParams,
    BusinessAssetGroupDeleteContainedInstagramAccountsParams,
    BusinessAssetGroupDeleteContainedPagesParams,
    BusinessAssetGroupDeleteContainedPixelsParams,
    BusinessAssetGroupDeleteContainedProductCatalogsParams,
    BusinessAssetGroupField,
    BusinessAssetGroupGetAssignedUsersParams,
    BusinessAssetGroupUpdateParams,
)
from src.utils import wrapped_fn_tool

# Server setup
server_name = "FacebookBusinessAssetGroup"
instructions = """
BusinessAssetGroup MCP Server for Facebook Business API.

Provides typed access to all BusinessAssetGroup operations.
"""

businessassetgroup_server = FastMCP(
    name=server_name,
    instructions=instructions,
)


# ---- CRUD Operations (2) ----
@businessassetgroup_server.tool
@wrapped_fn_tool
def get_businessassetgroup(
    businessassetgroup_id: str,
    fields: list[BusinessAssetGroupField] = [],
) -> str:
    """Get a BusinessAssetGroup object by ID.

    Args:
        businessassetgroup_id: The ID of the BusinessAssetGroup.
        fields: Fields to retrieve. Available fields: See BusinessAssetGroupField type.
    """
    obj = BusinessAssetGroup(businessassetgroup_id)
    return obj.api_get(fields=fields)


@businessassetgroup_server.tool
@wrapped_fn_tool
def update_businessassetgroup(
    businessassetgroup_id: str,
    fields: list[BusinessAssetGroupField] = [],
    params: BusinessAssetGroupUpdateParams | dict = {},
) -> str:
    """Update a BusinessAssetGroup object.

    Args:
        businessassetgroup_id: The ID of the BusinessAssetGroup.
        fields: Fields to return after update. Available fields: See BusinessAssetGroupField type.
        params: Parameters to update. Available params: See BusinessAssetGroupUpdateParams type.
    """
    return BusinessAssetGroup(businessassetgroup_id).api_update(fields=fields, params=params)


# ---- Edge Methods (17) ----
@businessassetgroup_server.tool
@wrapped_fn_tool
def delete_assigned_users(
    businessassetgroup_id: str,
    params: BusinessAssetGroupDeleteAssignedUsersParams | dict = {},
):
    """Delete Assigned Users for this BusinessAssetGroup.

    Args:
        businessassetgroup_id: The ID of the BusinessAssetGroup.
        params: Query parameters. Available params: See BusinessAssetGroupDeleteAssignedUsersParams type.
    """
    return BusinessAssetGroup(businessassetgroup_id).delete_assigned_users(params=params)


@businessassetgroup_server.tool
@wrapped_fn_tool
def get_assigned_users(
    businessassetgroup_id: str,
    fields: list[AssignedUserField] = [],
    params: BusinessAssetGroupGetAssignedUsersParams | dict = {},
):
    """Get Assigned Users for this BusinessAssetGroup.

    Args:
        businessassetgroup_id: The ID of the BusinessAssetGroup.
        fields: Fields to retrieve. Available fields: See AssignedUserField type.
        params: Query parameters. Available params: See BusinessAssetGroupGetAssignedUsersParams type.
    """
    return BusinessAssetGroup(businessassetgroup_id).get_assigned_users(
        fields=fields, params=params
    )


@businessassetgroup_server.tool
@wrapped_fn_tool
def create_assigned_user(
    businessassetgroup_id: str,
    fields: list[str] = [],
    params: BusinessAssetGroupCreateAssignedUserParams | dict = {},
):
    """Create Assigned User for this BusinessAssetGroup.

    Args:
        businessassetgroup_id: The ID of the BusinessAssetGroup.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See BusinessAssetGroupCreateAssignedUserParams type.
    """
    return BusinessAssetGroup(businessassetgroup_id).create_assigned_user(
        fields=fields, params=params
    )


@businessassetgroup_server.tool
@wrapped_fn_tool
def delete_contained_ad_accounts(
    businessassetgroup_id: str,
    params: BusinessAssetGroupDeleteContainedAdAccountsParams | dict = {},
):
    """Delete Contained Ad Accounts for this BusinessAssetGroup.

    Args:
        businessassetgroup_id: The ID of the BusinessAssetGroup.
        params: Query parameters. Available params: See BusinessAssetGroupDeleteContainedAdAccountsParams type.
    """
    return BusinessAssetGroup(businessassetgroup_id).delete_contained_ad_accounts(params=params)


@businessassetgroup_server.tool
@wrapped_fn_tool
def create_contained_ad_account(
    businessassetgroup_id: str,
    fields: list[str] = [],
    params: BusinessAssetGroupCreateContainedAdAccountParams | dict = {},
):
    """Create Contained Ad Account for this BusinessAssetGroup.

    Args:
        businessassetgroup_id: The ID of the BusinessAssetGroup.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See BusinessAssetGroupCreateContainedAdAccountParams type.
    """
    return BusinessAssetGroup(businessassetgroup_id).create_contained_ad_account(
        fields=fields, params=params
    )


@businessassetgroup_server.tool
@wrapped_fn_tool
def delete_contained_applications(
    businessassetgroup_id: str,
    params: BusinessAssetGroupDeleteContainedApplicationsParams | dict = {},
):
    """Delete Contained Applications for this BusinessAssetGroup.

    Args:
        businessassetgroup_id: The ID of the BusinessAssetGroup.
        params: Query parameters. Available params: See BusinessAssetGroupDeleteContainedApplicationsParams type.
    """
    return BusinessAssetGroup(businessassetgroup_id).delete_contained_applications(params=params)


@businessassetgroup_server.tool
@wrapped_fn_tool
def create_contained_application(
    businessassetgroup_id: str,
    fields: list[str] = [],
    params: BusinessAssetGroupCreateContainedApplicationParams | dict = {},
):
    """Create Contained Application for this BusinessAssetGroup.

    Args:
        businessassetgroup_id: The ID of the BusinessAssetGroup.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See BusinessAssetGroupCreateContainedApplicationParams type.
    """
    return BusinessAssetGroup(businessassetgroup_id).create_contained_application(
        fields=fields, params=params
    )


@businessassetgroup_server.tool
@wrapped_fn_tool
def delete_contained_custom_conversions(
    businessassetgroup_id: str,
    params: BusinessAssetGroupDeleteContainedCustomConversionsParams | dict = {},
):
    """Delete Contained Custom Conversions for this BusinessAssetGroup.

    Args:
        businessassetgroup_id: The ID of the BusinessAssetGroup.
        params: Query parameters. Available params: See BusinessAssetGroupDeleteContainedCustomConversionsParams type.
    """
    return BusinessAssetGroup(businessassetgroup_id).delete_contained_custom_conversions(
        params=params
    )


@businessassetgroup_server.tool
@wrapped_fn_tool
def create_contained_custom_conversion(
    businessassetgroup_id: str,
    fields: list[str] = [],
    params: BusinessAssetGroupCreateContainedCustomConversionParams | dict = {},
):
    """Create Contained Custom Conversion for this BusinessAssetGroup.

    Args:
        businessassetgroup_id: The ID of the BusinessAssetGroup.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See BusinessAssetGroupCreateContainedCustomConversionParams type.
    """
    return BusinessAssetGroup(businessassetgroup_id).create_contained_custom_conversion(
        fields=fields, params=params
    )


@businessassetgroup_server.tool
@wrapped_fn_tool
def delete_contained_instagram_accounts(
    businessassetgroup_id: str,
    params: BusinessAssetGroupDeleteContainedInstagramAccountsParams | dict = {},
):
    """Delete Contained Instagram Accounts for this BusinessAssetGroup.

    Args:
        businessassetgroup_id: The ID of the BusinessAssetGroup.
        params: Query parameters. Available params: See BusinessAssetGroupDeleteContainedInstagramAccountsParams type.
    """
    return BusinessAssetGroup(businessassetgroup_id).delete_contained_instagram_accounts(
        params=params
    )


@businessassetgroup_server.tool
@wrapped_fn_tool
def create_contained_instagram_account(
    businessassetgroup_id: str,
    fields: list[str] = [],
    params: BusinessAssetGroupCreateContainedInstagramAccountParams | dict = {},
):
    """Create Contained Instagram Account for this BusinessAssetGroup.

    Args:
        businessassetgroup_id: The ID of the BusinessAssetGroup.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See BusinessAssetGroupCreateContainedInstagramAccountParams type.
    """
    return BusinessAssetGroup(businessassetgroup_id).create_contained_instagram_account(
        fields=fields, params=params
    )


@businessassetgroup_server.tool
@wrapped_fn_tool
def delete_contained_pages(
    businessassetgroup_id: str,
    params: BusinessAssetGroupDeleteContainedPagesParams | dict = {},
):
    """Delete Contained Pages for this BusinessAssetGroup.

    Args:
        businessassetgroup_id: The ID of the BusinessAssetGroup.
        params: Query parameters. Available params: See BusinessAssetGroupDeleteContainedPagesParams type.
    """
    return BusinessAssetGroup(businessassetgroup_id).delete_contained_pages(params=params)


@businessassetgroup_server.tool
@wrapped_fn_tool
def create_contained_page(
    businessassetgroup_id: str,
    fields: list[str] = [],
    params: BusinessAssetGroupCreateContainedPageParams | dict = {},
):
    """Create Contained Page for this BusinessAssetGroup.

    Args:
        businessassetgroup_id: The ID of the BusinessAssetGroup.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See BusinessAssetGroupCreateContainedPageParams type.
    """
    return BusinessAssetGroup(businessassetgroup_id).create_contained_page(
        fields=fields, params=params
    )


@businessassetgroup_server.tool
@wrapped_fn_tool
def delete_contained_pixels(
    businessassetgroup_id: str,
    params: BusinessAssetGroupDeleteContainedPixelsParams | dict = {},
):
    """Delete Contained Pixels for this BusinessAssetGroup.

    Args:
        businessassetgroup_id: The ID of the BusinessAssetGroup.
        params: Query parameters. Available params: See BusinessAssetGroupDeleteContainedPixelsParams type.
    """
    return BusinessAssetGroup(businessassetgroup_id).delete_contained_pixels(params=params)


@businessassetgroup_server.tool
@wrapped_fn_tool
def create_contained_pixel(
    businessassetgroup_id: str,
    fields: list[str] = [],
    params: BusinessAssetGroupCreateContainedPixelParams | dict = {},
):
    """Create Contained Pixel for this BusinessAssetGroup.

    Args:
        businessassetgroup_id: The ID of the BusinessAssetGroup.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See BusinessAssetGroupCreateContainedPixelParams type.
    """
    return BusinessAssetGroup(businessassetgroup_id).create_contained_pixel(
        fields=fields, params=params
    )


@businessassetgroup_server.tool
@wrapped_fn_tool
def delete_contained_product_catalogs(
    businessassetgroup_id: str,
    params: BusinessAssetGroupDeleteContainedProductCatalogsParams | dict = {},
):
    """Delete Contained Product Catalogs for this BusinessAssetGroup.

    Args:
        businessassetgroup_id: The ID of the BusinessAssetGroup.
        params: Query parameters. Available params: See BusinessAssetGroupDeleteContainedProductCatalogsParams type.
    """
    return BusinessAssetGroup(businessassetgroup_id).delete_contained_product_catalogs(
        params=params
    )


@businessassetgroup_server.tool
@wrapped_fn_tool
def create_contained_product_catalog(
    businessassetgroup_id: str,
    fields: list[str] = [],
    params: BusinessAssetGroupCreateContainedProductCatalogParams | dict = {},
):
    """Create Contained Product Catalog for this BusinessAssetGroup.

    Args:
        businessassetgroup_id: The ID of the BusinessAssetGroup.
        fields: Fields to retrieve.
        params: Query parameters. Available params: See BusinessAssetGroupCreateContainedProductCatalogParams type.
    """
    return BusinessAssetGroup(businessassetgroup_id).create_contained_product_catalog(
        fields=fields, params=params
    )
