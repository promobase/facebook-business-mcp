from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.api import FacebookAdsApi
from fastmcp import FastMCP

my_app_id = "your-app-id"
my_app_secret = "your-appsecret"
my_access_token = "your-page-access-token"
FacebookAdsApi.init(my_app_id, my_app_secret, my_access_token)
my_account = AdAccount("act_<your-adaccount-id>")
campaigns = my_account.get_campaigns()
print(campaigns)


instructions = """
"""
# You can also add instructions for how to interact with the server
mcp = FastMCP(
    name="FacebookBusinessMCPServer",
    instructions=instructions,
    on_duplicate_prompts="error",
    on_duplicate_resources="error",
    on_duplicate_tools="error",
)


@mcp.tool
def get_campaigns() -> list:
    """
    Get all campaigns from the Facebook Ad Account.
    """
    return my_account.get_campaigns(fields=["id", "name", "status"])


if __name__ == "__main__":
    mcp.run()
