import asyncio
import json
from typing import Any

from fastmcp import Client

config = {
    "mcpServers": {
        "facebook-business-mcp": {
            "command": "uv",
            "args": ["run", "main.py"],
        },
    }
}

client = Client(config)


async def test_tool(tool_name: str, args: dict[str, Any] = None) -> dict[str, Any]:
    """Test a single tool with given arguments."""
    if args is None:
        args = {}

    try:
        print(f"\n🧪 Testing {tool_name}...")
        result = await client.call_tool(tool_name, args)
        print(f"✅ {tool_name}: SUCCESS")
        
        # Parse the response - it's a list with TextContent objects
        parsed_result = None
        if isinstance(result, list) and len(result) > 0:
            if hasattr(result[0], 'text'):
                try:
                    parsed_result = json.loads(result[0].text)
                    if isinstance(parsed_result, dict):
                        if "data" in parsed_result:
                            if isinstance(parsed_result["data"], list):
                                print(f"   📊 Returned {len(parsed_result['data'])} items")
                            else:
                                print(f"   📊 Returned data object")
                                # Debug: print the data for campaign creation
                                if "create_campaign" in tool_name and "id" in str(parsed_result["data"]):
                                    print(f"   🆔 Created object ID: {parsed_result['data'].get('id', 'N/A')}")
                        else:
                            print(f"   📊 Returned dict object")
                except json.JSONDecodeError:
                    print(f"   ⚠️  Could not parse JSON response")
                    parsed_result = {"raw_text": result[0].text}
            else:
                print(f"   📊 Returned list with {len(result)} items")
                parsed_result = result
        else:
            print(f"   📊 Returned {type(result)} object")
            parsed_result = result
        
        return parsed_result or result
    except Exception as e:
        print(f"❌ {tool_name}: ERROR - {str(e)}")
        return {"error": str(e)}


async def test_ad_account_tools():
    """Test all Ad Account server tools."""
    print("\n" + "=" * 50)
    print("🏢 TESTING AD ACCOUNT TOOLS")
    print("=" * 50)

    # Test basic ad account info
    account_result = await test_tool("ad_account_get_ad_account")

    # Test ad account users
    await test_tool("ad_account_get_ad_account_users", {"limit": 5})

    # Test ad account activities
    await test_tool("ad_account_get_ad_account_activities", {"limit": 5})

    # Test custom audiences
    await test_tool("ad_account_get_ad_account_custom_audiences", {"limit": 5})

    # Test saved audiences
    await test_tool("ad_account_get_ad_account_saved_audiences", {"limit": 5})

    return account_result


async def test_campaign_tools():
    """Test all Campaign server tools."""
    print("\n" + "=" * 50)
    print("📈 TESTING CAMPAIGN TOOLS")
    print("=" * 50)

    # Get campaigns first
    campaigns_result = await test_tool("campaign_get_campaigns", {"limit": 5})

    campaign_id = None
    # Handle different response formats
    if isinstance(campaigns_result, dict):
        if (
            campaigns_result.get("success")
            and campaigns_result.get("data")
            and len(campaigns_result["data"]) > 0
        ):
            campaign_id = campaigns_result["data"][0].get("id")
    elif isinstance(campaigns_result, list) and len(campaigns_result) > 0:
        campaign_id = campaigns_result[0].get("id")
    
    if campaign_id:
        # Test get single campaign
        await test_tool("campaign_get_campaign", {"campaign_id": campaign_id})

    # Test campaign creation (will be paused by default for safety)
    create_result = await test_tool(
        "campaign_create_campaign",
        {
            "account_id": None,  # Use default account
            "name": "Test Campaign - MCP Test",
            "objective": "LINK_CLICKS",
            "status": "PAUSED",
            "daily_budget": 1000,  # $10.00 in cents
        },
    )

    # If campaign was created, test update and delete
    new_campaign_id = None
    if isinstance(create_result, dict):
        if create_result.get("success") and create_result.get("data"):
            new_campaign_id = create_result["data"].get("id")
    
    if new_campaign_id:
        print(f"   🎯 Testing update/delete with campaign ID: {new_campaign_id}")
        # Test update
        await test_tool(
            "campaign_update_campaign",
            {"campaign_id": new_campaign_id, "name": "Updated Test Campaign - MCP Test"},
        )

        # Test delete (cleanup)
        await test_tool("campaign_delete_campaign", {"campaign_id": new_campaign_id})

    return campaigns_result


async def test_adset_tools(campaign_id: str = None):
    """Test all AdSet server tools."""
    print("\n" + "=" * 50)
    print("🎯 TESTING ADSET TOOLS")
    print("=" * 50)

    if campaign_id:
        # Get adsets for the campaign
        adsets_result = await test_tool(
            "adset_get_campaign_adsets", {"campaign_id": campaign_id, "limit": 5}
        )

        adset_id = None
        if adsets_result:
            if isinstance(adsets_result, dict):
                if (
                    adsets_result.get("success")
                    and adsets_result.get("data")
                    and len(adsets_result["data"]) > 0
                ):
                    adset_id = adsets_result["data"][0].get("id")
            elif isinstance(adsets_result, list) and len(adsets_result) > 0:
                adset_id = adsets_result[0].get("id")
        
        if adset_id:
            # Test get single adset
            await test_tool("adset_get_adset", {"adset_id": adset_id})

        # Test adset creation (basic targeting)
        create_result = await test_tool(
            "adset_create_adset",
            {
                "campaign_id": campaign_id,
                "name": "Test AdSet - MCP Test",
                "optimization_goal": "LINK_CLICKS",
                "billing_event": "LINK_CLICKS",
                "bid_amount": 100,  # $1.00 in cents
                "targeting": {"geo_locations": {"countries": ["US"]}, "age_min": 18, "age_max": 65},
                "status": "PAUSED",
                "daily_budget": 500,  # $5.00 in cents
            },
        )

        # If adset was created, test update and delete
        if create_result.get("success") and create_result.get("data"):
            new_adset_id = create_result["data"].get("id")
            if new_adset_id:
                # Test update
                await test_tool(
                    "adset_update_adset",
                    {"adset_id": new_adset_id, "name": "Updated Test AdSet - MCP Test"},
                )

                # Test delete (cleanup)
                await test_tool("adset_delete_adset", {"adset_id": new_adset_id})

        return adsets_result
    else:
        print("⚠️  No campaign ID available, skipping adset tests")
        return None


async def test_ad_tools(adset_id: str = None):
    """Test all Ad server tools."""
    print("\n" + "=" * 50)
    print("📱 TESTING AD TOOLS")
    print("=" * 50)

    if adset_id:
        # Get ads for the adset
        ads_result = await test_tool("ad_get_adset_ads", {"adset_id": adset_id, "limit": 5})

        ad_id = None
        if ads_result:
            if isinstance(ads_result, dict):
                if ads_result.get("success") and ads_result.get("data") and len(ads_result["data"]) > 0:
                    ad_id = ads_result["data"][0].get("id")
            elif isinstance(ads_result, list) and len(ads_result) > 0:
                ad_id = ads_result[0].get("id")
        
        if ad_id:
            # Test get single ad
            await test_tool("ad_get_ad", {"ad_id": ad_id})

            # Test ad preview
            await test_tool(
                "ad_get_ad_preview", {"ad_id": ad_id, "ad_format": "DESKTOP_FEED_STANDARD"}
            )

        # Test ad creation (basic creative)
        create_result = await test_tool(
            "ad_create_ad",
            {
                "adset_id": adset_id,
                "name": "Test Ad - MCP Test",
                "creative": {
                    "object_story_spec": {
                        "page_id": "YOUR_PAGE_ID",  # This would need to be a real page ID
                        "link_data": {
                            "message": "Test ad message",
                            "link": "https://example.com",
                            "name": "Test Ad",
                        },
                    }
                },
                "status": "PAUSED",
            },
        )

        # If ad was created, test update and delete
        if create_result.get("success") and create_result.get("data"):
            new_ad_id = create_result["data"].get("id")
            if new_ad_id:
                # Test update
                await test_tool(
                    "ad_update_ad", {"ad_id": new_ad_id, "name": "Updated Test Ad - MCP Test"}
                )

                # Test delete (cleanup)
                await test_tool("ad_delete_ad", {"ad_id": new_ad_id})

        return ads_result
    else:
        print("⚠️  No adset ID available, skipping ad tests")
        return None


async def test_insights_tools(campaign_id: str = None, adset_id: str = None, ad_id: str = None):
    """Test all Insights server tools."""
    print("\n" + "=" * 50)
    print("📊 TESTING INSIGHTS TOOLS")
    print("=" * 50)

    # Test account insights
    await test_tool(
        "insights_get_account_insights",
        {"limit": 5, "time_range": {"since": "2024-01-01", "until": "2024-01-31"}},
    )

    # Test campaign insights
    if campaign_id:
        await test_tool(
            "insights_get_campaign_insights",
            {
                "campaign_id": campaign_id,
                "limit": 5,
                "time_range": {"since": "2024-01-01", "until": "2024-01-31"},
            },
        )

    # Test adset insights
    if adset_id:
        await test_tool(
            "insights_get_adset_insights",
            {
                "adset_id": adset_id,
                "limit": 5,
                "time_range": {"since": "2024-01-01", "until": "2024-01-31"},
            },
        )

    # Test ad insights
    if ad_id:
        await test_tool(
            "insights_get_ad_insights",
            {
                "ad_id": ad_id,
                "limit": 5,
                "time_range": {"since": "2024-01-01", "until": "2024-01-31"},
            },
        )

    # Test async insights
    await test_tool(
        "insights_get_insights_async",
        {
            "level": "account",
            "object_id": "act_648073588254125",  # Use the actual account ID from the logs
            "time_range": {"since": "2024-01-01", "until": "2024-01-31"},
        },
    )


async def run_comprehensive_tests():
    """Run comprehensive tests for all MCP server tools."""
    print("🚀 Starting comprehensive Facebook Business MCP tests...")
    print("⚠️  Note: Tests use PAUSED status for safety with test accounts")

    async with client:
        # List all available tools first
        tools = await client.list_tools()
        print(f"\n📋 Found {len(tools)} available tools:")
        for tool in tools:
            print(f"-{tool.name}")

        # Test Ad Account tools
        account_result = await test_ad_account_tools()

        # Test Campaign tools
        campaigns_result = await test_campaign_tools()

        # Extract IDs for dependent tests
        campaign_id = None
        if campaigns_result:
            if isinstance(campaigns_result, dict):
                if (
                    campaigns_result.get("success")
                    and campaigns_result.get("data")
                    and len(campaigns_result["data"]) > 0
                ):
                    campaign_id = campaigns_result["data"][0].get("id")
            elif isinstance(campaigns_result, list) and len(campaigns_result) > 0:
                campaign_id = campaigns_result[0].get("id")

        # Test AdSet tools
        adsets_result = await test_adset_tools(campaign_id)

        # Extract adset ID
        adset_id = None
        if adsets_result:
            if isinstance(adsets_result, dict):
                if (
                    adsets_result.get("success")
                    and adsets_result.get("data")
                    and len(adsets_result["data"]) > 0
                ):
                    adset_id = adsets_result["data"][0].get("id")
            elif isinstance(adsets_result, list) and len(adsets_result) > 0:
                adset_id = adsets_result[0].get("id")

        # Test Ad tools
        ads_result = await test_ad_tools(adset_id)

        # Extract ad ID
        ad_id = None
        if ads_result:
            if isinstance(ads_result, dict):
                if (
                    ads_result.get("success")
                    and ads_result.get("data")
                    and len(ads_result["data"]) > 0
                ):
                    ad_id = ads_result["data"][0].get("id")
            elif isinstance(ads_result, list) and len(ads_result) > 0:
                ad_id = ads_result[0].get("id")

        # Test Insights tools
        await test_insights_tools(campaign_id, adset_id, ad_id)

        print("\n" + "=" * 50)
        print("🎉 COMPREHENSIVE TESTING COMPLETED")
        print("=" * 50)
        print("✅ All available tools have been tested")
        print("📝 Check output above for individual test results")
        print("⚠️  Some tests may fail due to test account limitations or missing data")


if __name__ == "__main__":
    asyncio.run(run_comprehensive_tests())
