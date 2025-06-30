# Facebook Business MCP - Three-Layer Architecture

## Overview

The Facebook Business MCP server has been refactored into a three-layer architecture that balances usability, robustness, and completeness. This design reduces fragility while improving discoverability and maintainability.

## Architecture Layers

### 1. Foundation Layer (`src/servers/foundation/`)

**Universal Server** - Complete SDK access as a safety net
- `universal_server.py` - Dynamic access to ANY Facebook SDK object and method
- Provides discovery tools and fallback for edge cases
- Handles new features and undocumented operations

### 2. Resources Layer (`src/servers/resources/`)

**Streamlined Resource Servers** - Core operations that handle 80% of use cases
- `ad_account.py` - 12 core operations (reduced from 40+)
- `campaign.py` - 8 core operations (reduced from 15+)
- `adset.py` - 7 core operations
- `ad.py` - 6 core operations

Each resource server includes:
- Essential CRUD operations
- Key child resource access
- Performance metrics
- Dynamic fallback method

### 3. Workflows Layer (`src/servers/workflows/`)

**High-Level Workflow Servers** - Complex operations made simple
- `campaign_management_server.py` - Complete campaign creation and management
- `reporting_server.py` - Advanced analytics and performance reports
- `audience_server.py` - Custom and lookalike audience operations

## Benefits of This Architecture

1. **Progressive Disclosure**
   - Start with workflow tools (easiest)
   - Use resource tools for customization
   - Access universal server for edge cases

2. **Reduced Fragility**
   - Fewer specific tools to maintain
   - Dynamic fallbacks at each layer
   - Universal server covers everything

3. **Better Error Recovery**
   - Workflow fails → try resource tools
   - Resource fails → try universal server
   - Multiple paths to success

4. **Improved Discoverability**
   - Clear categorization by use case
   - Workflow tools for common tasks
   - Universal discovery tools

## Usage Examples

### Simple Campaign Creation (Workflow Layer)
```python
# One tool does everything
campaign_management.create_complete_campaign(
    account_id="act_123",
    campaign_name="Summer Sale",
    objective="CONVERSIONS",
    daily_budget=100,
    adset_name="Summer Sale AdSet",
    targeting={"geo_locations": {"countries": ["US"]}}
)
```

### Custom Campaign Setup (Resource Layer)
```python
# More control with resource tools
campaign_id = ad_account.create_campaign(...)
adset_id = ad_account.create_ad_set(...)
ad_id = ad.create_ad(...)
```

### Edge Case Handling (Foundation Layer)
```python
# Access any SDK method dynamically
universal.run_any_adobject_method(
    object_type="AdAccount",
    object_id="act_123",
    method="get_broad_targeting_categories",
    kwargs={"limit": 100}
)
```

## Migration Notes

- Old specific tools still work via dynamic fallback
- Workflow tools handle most common operations
- Universal server provides 100% SDK coverage
- Focus maintenance on high-impact workflow tools

## Tool Reduction Summary

| Server | Before | After | Reduction |
|--------|--------|-------|-----------|
| AdAccount | 40+ | 12 | 70% |
| Campaign | 15+ | 8 | 47% |
| AdSet | 20+ | 7 | 65% |
| Ad | 13+ | 6 | 54% |

Total tools reduced by ~60% while maintaining 100% functionality through dynamic fallbacks and the universal server.