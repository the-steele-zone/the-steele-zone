# Supabase Query Webhook - N8N Workflow

## Overview
This workflow creates a flexible API endpoint that accepts dynamic Supabase queries via POST requests. It allows you to query any table with custom filters without creating multiple workflows.

## Endpoint
```
POST https://thesteelezone.app.n8n.cloud/webhook/query_supabase
```

## Workflow Architecture

### Nodes Required:
├── **Webhook (POST)** ✅
│   └── Listen for incoming POST requests
│
├── **Code Node** (Parse request body)
│   └── Extract `body.table` and `body.filters`
│   └── Validate input parameters
│
├── **Supabase Node** (Get many rows)
│   └── Query table with parsed parameters
│   └── Apply filters dynamically
│
└── **Respond to Webhook**
    └── Return JSON response with results

## Request Format

### Basic Request
```json
{
  "table": "your_table_name",
  "filters": {
    "column_name": "value_to_match"
  }
}
```

### Advanced Request with Multiple Filters
```json
{
  "table": "content_posts",
  "filters": {
    "status": "published",
    "platform": "tiktok",
    "created_at": ">2024-01-01"
  },
  "limit": 50,
  "order_by": "created_at.desc"
}
```

## Example Use Cases

### 1. Query Social Media Posts
```bash
curl -X POST https://thesteelezone.app.n8n.cloud/webhook/query_supabase \
  -H "Content-Type: application/json" \
  -d '{
    "table": "social_posts",
    "filters": {
      "platform": "tiktok",
      "status": "published"
    }
  }'
```

### 2. Query User Analytics
```bash
curl -X POST https://thesteelezone.app.n8n.cloud/webhook/query_supabase \
  -H "Content-Type: application/json" \
  -d '{
    "table": "user_analytics",
    "filters": {
      "user_id": "your_user_id",
      "date": ">2024-12-01"
    }
  }'
```

### 3. Query Product Inventory
```bash
curl -X POST https://thesteelezone.app.n8n.cloud/webhook/query_supabase \
  -H "Content-Type: application/json" \
  -d '{
    "table": "products",
    "filters": {
      "in_stock": true,
      "category": "digital"
    },
    "limit": 100
  }'
```

## Code Node Implementation

### Parse and Validate Input
```javascript
// Get the webhook body
const body = $input.item.json.body;

// Validate required fields
if (!body.table) {
  throw new Error('Missing required field: table');
}

// Extract parameters
const tableName = body.table;
const filters = body.filters || {};
const limit = body.limit || 100;
const orderBy = body.order_by || 'created_at.desc';

// Build filter query string for Supabase
const filterEntries = Object.entries(filters);
const filterString = filterEntries
  .map(([key, value]) => {
    if (typeof value === 'string' && value.startsWith('>')) {
      return `${key}.gt.${value.substring(1)}`;
    } else if (typeof value === 'string' && value.startsWith('<')) {
      return `${key}.lt.${value.substring(1)}`;
    } else {
      return `${key}.eq.${value}`;
    }
  })
  .join('&');

// Return parsed data for next nodes
return {
  json: {
    table: tableName,
    filters: filters,
    filterString: filterString,
    limit: limit,
    orderBy: orderBy
  }
};
```

## Supabase Node Configuration

### Settings:
- **Operation**: Get Many
- **Table**: `{{ $json.table }}`
- **Return All**: False
- **Limit**: `{{ $json.limit }}`
- **Additional Fields**:
  - Filter: `{{ $json.filterString }}`
  - Order: `{{ $json.orderBy }}`

## Response Format

### Success Response
```json
{
  "success": true,
  "data": [
    {
      "id": 1,
      "column1": "value1",
      "column2": "value2"
    }
  ],
  "count": 1,
  "table": "your_table_name"
}
```

### Error Response
```json
{
  "success": false,
  "error": "Error message here",
  "code": "ERROR_CODE"
}
```

## Security Considerations

⚠️ **IMPORTANT**: This endpoint should be secured!

### Recommended Security Measures:
1. **Add Authentication Header**
   - Require API key in request headers
   - Validate in Code node before processing

2. **Table Whitelist**
   - Only allow queries to approved tables
   - Reject requests for sensitive tables

3. **Rate Limiting**
   - Implement rate limiting in n8n or via proxy
   - Prevent abuse and excessive API calls

4. **Input Validation**
   - Sanitize all inputs
   - Prevent SQL injection attempts

### Example Security Code
```javascript
// Whitelist of allowed tables
const ALLOWED_TABLES = [
  'social_posts',
  'user_analytics', 
  'products',
  'content_automation'
];

// Check API key
const apiKey = $input.item.headers.authorization;
if (apiKey !== process.env.WEBHOOK_API_KEY) {
  throw new Error('Unauthorized: Invalid API key');
}

// Validate table access
if (!ALLOWED_TABLES.includes(body.table)) {
  throw new Error(`Forbidden: Access to table '${body.table}' is not allowed`);
}
```

## Integration with Other Tools

### Use with Bardeen
```javascript
// Bardeen playbook code
const response = await fetch('https://thesteelezone.app.n8n.cloud/webhook/query_supabase', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer YOUR_API_KEY'
  },
  body: JSON.stringify({
    table: 'social_posts',
    filters: { platform: 'tiktok' }
  })
});

const data = await response.json();
```

### Use with Frontend Application
```javascript
// JavaScript/React frontend
const querySupabase = async (table, filters) => {
  try {
    const response = await fetch('https://thesteelezone.app.n8n.cloud/webhook/query_supabase', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ table, filters })
    });
    
    return await response.json();
  } catch (error) {
    console.error('Query failed:', error);
    throw error;
  }
};

// Usage
const posts = await querySupabase('social_posts', { 
  status: 'published',
  platform: 'tiktok' 
});
```

### Use with Python
```python
import requests

def query_supabase(table, filters=None, limit=100):
    url = 'https://thesteelezone.app.n8n.cloud/webhook/query_supabase'
    
    payload = {
        'table': table,
        'filters': filters or {},
        'limit': limit
    }
    
    response = requests.post(url, json=payload)
    return response.json()

# Usage
results = query_supabase(
    table='social_posts',
    filters={'platform': 'tiktok', 'status': 'published'},
    limit=50
)
```

## Testing

### Test with curl
```bash
# Test basic query
curl -X POST https://thesteelezone.app.n8n.cloud/webhook/query_supabase \
  -H "Content-Type: application/json" \
  -d '{"table":"test_table","filters":{}}'

# Test with filters
curl -X POST https://thesteelezone.app.n8n.cloud/webhook/query_supabase \
  -H "Content-Type: application/json" \
  -d '{"table":"social_posts","filters":{"status":"draft"}}'
```

### Test with Postman
1. Create new POST request
2. Set URL: `https://thesteelezone.app.n8n.cloud/webhook/query_supabase`
3. Set Headers: `Content-Type: application/json`
4. Set Body (raw JSON):
```json
{
  "table": "your_table",
  "filters": {
    "column": "value"
  }
}
```

## Environment Variables

Make sure these are set in your n8n instance:

```env
SUPABASE_URL=https://your-project.supabase.co
SUPABASE_KEY=your_supabase_anon_key
WEBHOOK_API_KEY=your_webhook_security_key
```

## Troubleshooting

### Common Errors

#### 1. "Missing required field: table"
- Ensure your request body includes `table` field
- Check JSON formatting

#### 2. "Forbidden: Access to table not allowed"
- Table name not in whitelist
- Add table to ALLOWED_TABLES array

#### 3. "Unauthorized: Invalid API key"
- Check Authorization header
- Verify API key matches environment variable

#### 4. No results returned
- Verify table name is correct
- Check if filters match existing data
- Try query without filters first

## Performance Optimization

### Tips:
1. **Use Pagination**: Always set reasonable limits
2. **Index Columns**: Ensure filtered columns are indexed in Supabase
3. **Cache Results**: Implement caching for frequently queried data
4. **Batch Requests**: Combine multiple queries when possible

## Future Enhancements

- [ ] Add support for JOIN operations
- [ ] Implement SELECT specific columns
- [ ] Add INSERT/UPDATE/DELETE operations
- [ ] Create audit logging for all queries
- [ ] Add webhook signature verification
- [ ] Implement response caching layer
- [ ] Add GraphQL support
- [ ] Create automatic API documentation

## Related Documentation

- [Helius Endpoints](../helius_endpoints.md) - Solana RPC endpoints
- [N8N Configuration](../n8n-config/.env.n8n) - N8N environment setup
- [Supabase Documentation](https://supabase.io/docs)
- [N8N Webhook Documentation](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.webhook/)

## Changelog

### 2024-12-23
- Created initial workflow documentation
- Added security considerations
- Added integration examples
- Added testing instructions

---

**Status**: 🟡 In Development
**Owner**: @thesteelezone
**Last Updated**: December 23, 2024
