# CORS-Enabled APIs

APIs that can be called directly from browser-based HTML tools (no proxy needed).

## What is CORS?

**CORS** (Cross-Origin Resource Sharing) allows JavaScript running on one domain to access APIs on another domain. APIs must explicitly enable CORS headers for browser access.

**Why it matters**: HTML tools need CORS-enabled APIs since they run in the browser without a backend proxy.

## Testing for CORS

```javascript
async function testCORS(url) {
    try {
        const response = await fetch(url);
        const corsHeader = response.headers.get('Access-Control-Allow-Origin');
        return corsHeader === '*' || corsHeader === window.location.origin;
    } catch (error) {
        return false;
    }
}
```

Or use Simon Willison's **cors-fetch** debugging tool.

## Known CORS-Enabled APIs

### Package Registries

#### PyPI (Python Package Index)
- **Endpoint**: `https://pypi.org/pypi/{package}/json`
- **CORS**: ✅ Fully open
- **Rate Limit**: None documented
- **Auth**: Not required
- **Example**:
  ```javascript
  const response = await fetch('https://pypi.org/pypi/requests/json');
  const data = await response.json();
  console.log(data.info.version);
  ```
- **Use cases**: Package info, version history, download stats

#### npm Registry
- **Endpoint**: `https://registry.npmjs.org/{package}`
- **CORS**: ✅ Open
- **Rate Limit**: None documented
- **Auth**: Not required
- **Example**:
  ```javascript
  const response = await fetch('https://registry.npmjs.org/lodash');
  const data = await response.json();
  ```
- **Use cases**: Package metadata, versions, dependencies

### GitHub

#### Raw Content (raw.githubusercontent.com)
- **Endpoint**: `https://raw.githubusercontent.com/{user}/{repo}/{branch}/{path}`
- **CORS**: ✅ Fully open
- **CDN**: Yes (cached)
- **Auth**: Not required for public repos
- **Example**:
  ```javascript
  const response = await fetch(
    'https://raw.githubusercontent.com/microsoft/amplifier/main/README.md'
  );
  const content = await response.text();
  ```
- **Use cases**: Fetch files from public repos, load configs, read documentation

#### API (api.github.com)
- **Endpoint**: `https://api.github.com/*`
- **CORS**: ✅ Partial (some endpoints)
- **Rate Limit**: 60 requests/hour (unauthenticated), 5000/hour (authenticated)
- **Auth**: Optional (token via Authorization header)
- **Example**:
  ```javascript
  const response = await fetch('https://api.github.com/repos/microsoft/amplifier');
  const data = await response.json();
  ```
- **Use cases**: Repo info, issues, releases, user data

#### Gists
- **Endpoint**: `https://api.github.com/gists/{id}`
- **CORS**: ✅ Yes
- **Auth**: Token required for creation/updates
- **Use cases**: Store/retrieve user data, share snippets

### Nature and Science

#### iNaturalist
- **Endpoint**: `https://api.inaturalist.org/v1/*`
- **CORS**: ✅ Fully open
- **Rate Limit**: ~60 requests/minute
- **Auth**: Not required for observations
- **Example**:
  ```javascript
  const response = await fetch(
    'https://api.inaturalist.org/v1/observations?taxon_name=Puma+concolor'
  );
  const data = await response.json();
  ```
- **Use cases**: Species observations, photos, geographic data, taxonomy

#### Open Meteo (Weather)
- **Endpoint**: `https://api.open-meteo.com/v1/*`
- **CORS**: ✅ Fully open
- **Rate Limit**: 10,000 requests/day (free)
- **Auth**: Not required
- **Example**:
  ```javascript
  const response = await fetch(
    'https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&current_weather=true'
  );
  const data = await response.json();
  ```
- **Use cases**: Weather forecasts, historical weather data

### Social Networks

#### Bluesky
- **Endpoint**: `https://public.api.bsky.app/xrpc/*`
- **CORS**: ✅ Fully open for public endpoints
- **Rate Limit**: Varies by endpoint
- **Auth**: Not required for public data
- **Example**:
  ```javascript
  const response = await fetch(
    'https://public.api.bsky.app/xrpc/app.bsky.feed.getPostThread?uri=at://...'
  );
  const data = await response.json();
  ```
- **Use cases**: Read posts, threads, profiles, follows

#### Mastodon Instances
- **Endpoint**: `https://{instance}/api/v1/*`
- **CORS**: ✅ Generally open (instance-dependent)
- **Rate Limit**: Varies by instance
- **Auth**: Token for private data
- **Example**:
  ```javascript
  const response = await fetch('https://mastodon.social/api/v1/timelines/public?limit=10');
  const data = await response.json();
  ```
- **Use cases**: Public timelines, profiles, posts

### AI/LLM APIs

#### OpenAI
- **Endpoint**: `https://api.openai.com/v1/*`
- **CORS**: ✅ Yes
- **Rate Limit**: Varies by tier
- **Auth**: ⚠️ **Required** (API key)
- **Security**: Store key in localStorage, never in HTML
- **Example**:
  ```javascript
  const response = await fetch('https://api.openai.com/v1/chat/completions', {
    method: 'POST',
    headers: {
      'Authorization': `Bearer ${localStorage.getItem('openai_key')}`,
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      model: 'gpt-4',
      messages: [{role: 'user', content: 'Hello!'}]
    })
  });
  ```
- **Use cases**: Chat, completions, embeddings, audio, vision

#### Anthropic (Claude)
- **Endpoint**: `https://api.anthropic.com/v1/*`
- **CORS**: ✅ Yes
- **Rate Limit**: Varies by tier
- **Auth**: ⚠️ **Required** (API key + version header)
- **Security**: Store key in localStorage
- **Example**:
  ```javascript
  const response = await fetch('https://api.anthropic.com/v1/messages', {
    method: 'POST',
    headers: {
      'x-api-key': localStorage.getItem('anthropic_key'),
      'anthropic-version': '2023-06-01',
      'content-type': 'application/json'
    },
    body: JSON.stringify({
      model: 'claude-3-5-sonnet-20241022',
      max_tokens: 1024,
      messages: [{role: 'user', content: 'Hello!'}]
    })
  });
  ```
- **Use cases**: Chat, analysis, vision

#### Google Gemini
- **Endpoint**: `https://generativelanguage.googleapis.com/v1beta/*`
- **CORS**: ✅ Yes
- **Rate Limit**: Varies by tier
- **Auth**: ⚠️ **Required** (API key as query param)
- **Example**:
  ```javascript
  const apiKey = localStorage.getItem('gemini_key');
  const response = await fetch(
    `https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key=${apiKey}`,
    {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({
        contents: [{parts: [{text: 'Hello!'}]}]
      })
    }
  );
  ```
- **Use cases**: Text generation, vision, embeddings

### Geographic Data

#### OpenStreetMap
- **Endpoint**: `https://nominatim.openstreetmap.org/*`
- **CORS**: ✅ Yes
- **Rate Limit**: 1 request/second
- **Auth**: Not required
- **User-Agent**: ⚠️ Required in headers
- **Example**:
  ```javascript
  const response = await fetch(
    'https://nominatim.openstreetmap.org/search?q=London&format=json',
    {headers: {'User-Agent': 'MyHTMLTool/1.0'}}
  );
  ```
- **Use cases**: Geocoding, reverse geocoding, address search

### Miscellaneous

#### JSONPlaceholder
- **Endpoint**: `https://jsonplaceholder.typicode.com/*`
- **CORS**: ✅ Fully open
- **Rate Limit**: None
- **Auth**: Not required
- **Purpose**: Fake REST API for testing
- **Example**:
  ```javascript
  const response = await fetch('https://jsonplaceholder.typicode.com/posts/1');
  const data = await response.json();
  ```

#### httpbin
- **Endpoint**: `https://httpbin.org/*`
- **CORS**: ✅ Fully open
- **Rate Limit**: None
- **Auth**: Not required
- **Purpose**: HTTP request/response testing
- **Example**:
  ```javascript
  const response = await fetch('https://httpbin.org/get');
  const data = await response.json();
  ```

#### Random User Generator
- **Endpoint**: `https://randomuser.me/api/*`
- **CORS**: ✅ Fully open
- **Rate Limit**: None
- **Auth**: Not required
- **Example**:
  ```javascript
  const response = await fetch('https://randomuser.me/api/?results=10');
  const data = await response.json();
  ```
- **Use cases**: Generate fake user data for demos

## Handling API Keys Safely

### ⚠️ NEVER put API keys in:
- HTML source code
- JavaScript variables visible in source
- URL parameters
- Git repositories
- Comments

### ✅ DO store API keys in:
```javascript
// Prompt user for key on first use
function getAPIKey(service) {
    let key = localStorage.getItem(`${service}_api_key`);
    
    if (!key) {
        key = prompt(`Enter your ${service} API key:`);
        if (key) {
            localStorage.setItem(`${service}_api_key`, key);
        }
    }
    
    return key;
}

// Use in requests
const apiKey = getAPIKey('openai');
if (!apiKey) {
    alert('API key required');
    return;
}

// Include in request
headers: {
    'Authorization': `Bearer ${apiKey}`
}
```

### Key Management UI Pattern

```html
<details>
    <summary>⚙️ API Settings</summary>
    <div>
        <label>
            OpenAI API Key:
            <input type="password" id="apiKey" value="">
        </label>
        <button onclick="saveKey()">Save</button>
        <button onclick="clearKey()">Clear</button>
        <p><small>Stored locally in your browser. <a href="https://platform.openai.com/api-keys" target="_blank">Get a key</a></small></p>
    </div>
</details>

<script>
function saveKey() {
    const key = document.getElementById('apiKey').value;
    localStorage.setItem('openai_key', key);
    alert('Key saved!');
}

function clearKey() {
    localStorage.removeItem('openai_key');
    document.getElementById('apiKey').value = '';
    alert('Key cleared!');
}

// Load on page load
document.getElementById('apiKey').value = localStorage.getItem('openai_key') || '';
</script>
```

## Testing for CORS Support

Before building a tool around an API, test CORS support:

```javascript
async function testAPICORS(url) {
    try {
        const response = await fetch(url, {mode: 'cors'});
        const corsHeader = response.headers.get('Access-Control-Allow-Origin');
        
        console.log('✅ CORS Enabled:', corsHeader);
        console.log('Status:', response.status);
        return true;
    } catch (error) {
        console.error('❌ CORS Error:', error.message);
        return false;
    }
}

// Test an endpoint
testAPICORS('https://api.github.com/repos/microsoft/amplifier');
```

## When CORS Isn't Available

If an API doesn't support CORS:

1. **Use a CORS proxy** (not recommended for production):
   - `https://corsproxy.io/?${url}`
   - `https://api.allorigins.win/get?url=${encodeURIComponent(url)}`

2. **Build a backend proxy**: Not suitable for single-file HTML tools

3. **Find an alternative API**: Many services have CORS-enabled alternatives

4. **Ask the API provider**: Request CORS support

## Rate Limiting Best Practices

```javascript
// Simple rate limiter
class RateLimiter {
    constructor(maxRequests, windowMs) {
        this.maxRequests = maxRequests;
        this.windowMs = windowMs;
        this.requests = [];
    }
    
    async limit() {
        const now = Date.now();
        this.requests = this.requests.filter(time => now - time < this.windowMs);
        
        if (this.requests.length >= this.maxRequests) {
            const oldestRequest = this.requests[0];
            const waitTime = this.windowMs - (now - oldestRequest);
            await new Promise(resolve => setTimeout(resolve, waitTime));
        }
        
        this.requests.push(now);
    }
}

// Usage: GitHub API (60 requests/hour)
const limiter = new RateLimiter(60, 60 * 60 * 1000);

async function fetchFromGitHub(url) {
    await limiter.limit();
    return fetch(url);
}
```

## Contributing

Found a CORS-enabled API? Add it to this list following the template:

```markdown
#### API Name
- **Endpoint**: Base URL
- **CORS**: ✅/❌/⚠️ (with conditions)
- **Rate Limit**: Details
- **Auth**: Required/Not required
- **Example**: Code snippet
- **Use cases**: What it's good for
```
