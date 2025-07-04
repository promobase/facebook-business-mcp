<div align="center">
  <img src="https://raw.githubusercontent.com/promobase/facebook-business-mcp/refs/heads/dev/assets/OpenPromo.svg" alt="OpenPromo Logo" width="340" height="50" />
</div>

---

<div align="center">

[![Python](https://img.shields.io/badge/python-3.12+-blue.svg)](https://www.python.org/downloads/) [![MCP](https://img.shields.io/badge/MCP-Protocol-green)](https://modelcontextprotocol.io/) [![Facebook API](https://img.shields.io/badge/Facebook-Business_API-1877F2?logo=facebook)](https://developers.facebook.com/docs/marketing-apis) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) [![Code style: pyright](https://img.shields.io/badge/code%20style-pyright-000000.svg)](https://github.com/psf/pyright)

</div>

# Facebook Business MCP Server

Unofficial MCP server implementation for [Facebook Business API](https://developers.facebook.com/docs/business-sdk/). You can use this with any clients/LLMs to manage your ad campaigns, ads, etc.

## Features

- **Complete**: implementation is wrapped on top of api specs & python sdk, for full typesafty.
- **MCP Compliant**: Built with [FastMCP](https://gofastmcp.com/getting-started/welcome) for seamless integration with any MCP-compatible client or LLM.
- **Easy Setup**: Simple configuration with environment variables and immediate connectivity to Facebook Business API.

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
   uv run  main.py
   ```

## License

MIT
