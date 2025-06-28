This is repo for `facebook-business-mcp`, server implementation of Model Context Protocol(MCP) wrapping the facebook business API. Implemneted using `FastMCP`. You can use tools to fetch the docs for reference.

# Architecture

we installed `facebook_business` python sdk, the goal is to create MCP server for each resource group. e.g. Ad Account. Campaign, etc. Then, in the `main,py` we have a root MCP server, mounting the sub servers into it. We try to provide 100% type safety. you can look up the types params from the docs on Facebook marketing apis, and then call it using the python sdk.

# Docs

1. [Meta Business API docs](https://developers.facebook.com/docs/marketing-apis)
2. [FastMCP docs](https://gofastmcp.com/llms.txt) This contains all the site map for how to use fastmcp & composing, etc.
