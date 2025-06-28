# Facebook Business MCP Server

Unofficial MCP server implementation for Facebook Business API.

## Overview

This server provides access to Facebook Business API through the Model Context Protocol (MCP), allowing LLMs to interact with Facebook advertising data and operations.

## Features

- **Ad Account Management**: Get account information and insights
- **Campaign Operations**: Retrieve campaign data and details
- **Health Checks**: Verify API connectivity and configuration

## Setup

1. Install dependencies:
   ```bash
   uv sync
   ```

2. Set environment variables:
   ```bash
   export FACEBOOK_APP_ID="your-app-id"
   export FACEBOOK_APP_SECRET="your-app-secret"
   export FACEBOOK_ACCESS_TOKEN="your-access-token"
   export FACEBOOK_AD_ACCOUNT_ID="your-ad-account-id"  # optional
   ```

3. Run the server:
   ```bash
   uv run python main.py
   ```

## Available Tools

- `get_ad_account(account_id?)` - Get ad account information
- `get_campaigns(account_id?, limit?)` - List campaigns for an account
- `get_campaign(campaign_id)` - Get specific campaign details
- `health_check()` - Check API connectivity

## Configuration

The server uses environment variables for configuration:

- `FACEBOOK_APP_ID` - Your Facebook App ID (required)
- `FACEBOOK_APP_SECRET` - Your Facebook App Secret (required)
- `FACEBOOK_ACCESS_TOKEN` - Your Facebook Access Token (required)
- `FACEBOOK_AD_ACCOUNT_ID` - Default Ad Account ID (optional)
- `FACEBOOK_API_VERSION` - API version to use (default: v21.0)

## License

MIT
