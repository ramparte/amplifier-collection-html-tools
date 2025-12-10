# Common Patterns and Code Snippets

Ready-to-use code patterns for HTML tools.

## State Management

### URL-Based State (Shareable)

```javascript
// Save state to URL
function saveStateToURL(data) {
    const encoded = btoa(JSON.stringify(data));
    const params = new URLSearchParams(window.location.search);
    params.set('state', encoded);
    const newURL = window.location.pathname + '?' + params.toString();
    window.history.replaceState({}, '', newURL);
}

// Load state from URL
function loadStateFromURL() {
    const params = new URLSearchParams(window.location.search);
    const encoded = params.get('state');
    if (encoded) {
        try {
            return JSON.parse(atob(encoded));
        } catch (e) {
            console.error('Failed to parse state from URL:', e);
            return null;
        }
    }
    return null;
}

// Initialize on page load
window.addEventListener('DOMContentLoaded', () => {
    const state = loadStateFromURL();
    if (state) {
        // Restore state
        document.getElementById('input').value = state.input || '';
        // ... restore other fields
    }
});
```

### localStorage (Secrets and Persistence)

```javascript
// Save/load simple values
function saveToStorage(key, value) {
    localStorage.setItem(key, value);
}

function loadFromStorage(key, defaultValue = null) {
    return localStorage.getItem(key) || defaultValue;
}

// Save/load objects
function saveObjectToStorage(key, obj) {
    localStorage.setItem(key, JSON.stringify(obj));
}

function loadObjectFromStorage(key, defaultValue = null) {
    const item = localStorage.getItem(key);
    if (item) {
        try {
            return JSON.parse(item);
        } catch (e) {
            console.error('Failed to parse from localStorage:', e);
        }
    }
    return defaultValue;
}

// Auto-save input as user types
function enableAutoSave(elementId, storageKey) {
    const element = document.getElementById(elementId);
    
    // Load saved value
    const saved = loadFromStorage(storageKey);
    if (saved) {
        element.value = saved;
    }
    
    // Save on input
    element.addEventListener('input', () => {
        saveToStorage(storageKey, element.value);
    });
}
```

## Copy and Paste

### Copy to Clipboard

```javascript
async function copyToClipboard(text) {
    try {
        // Modern API
        await navigator.clipboard.writeText(text);
        return true;
    } catch (err) {
        // Fallback for older browsers
        const textarea = document.createElement('textarea');
        textarea.value = text;
        textarea.style.position = 'fixed';
        textarea.style.opacity = '0';
        document.body.appendChild(textarea);
        textarea.select();
        const success = document.execCommand('copy');
        document.body.removeChild(textarea);
        return success;
    }
}

// Usage with button feedback
async function handleCopy(text, buttonId) {
    const button = document.getElementById(buttonId);
    const originalText = button.textContent;
    
    const success = await copyToClipboard(text);
    
    if (success) {
        button.textContent = '✓ Copied!';
        button.classList.add('success');
    } else {
        button.textContent = '✗ Failed';
        button.classList.add('error');
    }
    
    setTimeout(() => {
        button.textContent = originalText;
        button.classList.remove('success', 'error');
    }, 2000);
}
```

### Paste Handling (Including Rich Content)

```javascript
// Handle paste events with multiple formats
document.addEventListener('paste', async (e) => {
    e.preventDefault();
    
    const items = Array.from(e.clipboardData.items);
    
    for (const item of items) {
        // Handle images
        if (item.type.startsWith('image/')) {
            const file = item.getAsFile();
            const reader = new FileReader();
            reader.onload = (event) => {
                const img = document.createElement('img');
                img.src = event.target.result;
                document.getElementById('output').appendChild(img);
            };
            reader.readAsDataURL(file);
        }
        
        // Handle HTML (rich text)
        else if (item.type === 'text/html') {
            const html = await new Promise(resolve => {
                item.getAsString(resolve);
            });
            document.getElementById('output').innerHTML = html;
        }
        
        // Handle plain text
        else if (item.type === 'text/plain') {
            const text = e.clipboardData.getData('text/plain');
            document.getElementById('input').value = text;
        }
    }
});
```

## File Operations

### File Upload

```javascript
// Handle file selection
function setupFileUpload(inputId, callback) {
    const input = document.getElementById(inputId);
    
    input.addEventListener('change', async (e) => {
        const file = e.target.files[0];
        if (!file) return;
        
        // Read as text
        if (file.type.startsWith('text/')) {
            const text = await file.text();
            callback(text, file);
        }
        // Read as data URL (for images)
        else if (file.type.startsWith('image/')) {
            const reader = new FileReader();
            reader.onload = (event) => {
                callback(event.target.result, file);
            };
            reader.readAsDataURL(file);
        }
        // Read as array buffer (for binary)
        else {
            const buffer = await file.arrayBuffer();
            callback(buffer, file);
        }
    });
}

// Drag and drop support
function setupDragDrop(elementId, callback) {
    const element = document.getElementById(elementId);
    
    element.addEventListener('dragover', (e) => {
        e.preventDefault();
        element.classList.add('drag-over');
    });
    
    element.addEventListener('dragleave', () => {
        element.classList.remove('drag-over');
    });
    
    element.addEventListener('drop', async (e) => {
        e.preventDefault();
        element.classList.remove('drag-over');
        
        const file = e.dataTransfer.files[0];
        if (file) {
            const text = await file.text();
            callback(text, file);
        }
    });
}
```

### File Download

```javascript
function downloadFile(content, filename, mimeType = 'text/plain') {
    const blob = new Blob([content], { type: mimeType });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = filename;
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    URL.revokeObjectURL(url);
}

// Common download helpers
function downloadText(text, filename) {
    downloadFile(text, filename, 'text/plain');
}

function downloadJSON(obj, filename) {
    const json = JSON.stringify(obj, null, 2);
    downloadFile(json, filename, 'application/json');
}

function downloadHTML(html, filename) {
    downloadFile(html, filename, 'text/html');
}

function downloadCSV(csv, filename) {
    downloadFile(csv, filename, 'text/csv');
}
```

## API Calls

### CORS API Wrapper

```javascript
async function fetchAPI(url, options = {}) {
    const defaultOptions = {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
        },
        ...options
    };
    
    try {
        const response = await fetch(url, defaultOptions);
        
        if (!response.ok) {
            throw new Error(`HTTP ${response.status}: ${response.statusText}`);
        }
        
        const contentType = response.headers.get('content-type');
        if (contentType && contentType.includes('application/json')) {
            return await response.json();
        } else {
            return await response.text();
        }
    } catch (error) {
        console.error('API Error:', error);
        showError(`API request failed: ${error.message}`);
        throw error;
    }
}

// API with retry
async function fetchWithRetry(url, options = {}, maxRetries = 3) {
    for (let i = 0; i < maxRetries; i++) {
        try {
            return await fetchAPI(url, options);
        } catch (error) {
            if (i === maxRetries - 1) throw error;
            await new Promise(resolve => setTimeout(resolve, 1000 * (i + 1)));
        }
    }
}
```

### API Key Management

```javascript
function getAPIKey(serviceName, promptMessage) {
    let key = localStorage.getItem(`${serviceName}_api_key`);
    
    if (!key) {
        key = prompt(promptMessage || `Enter your ${serviceName} API key:`);
        if (key) {
            localStorage.setItem(`${serviceName}_api_key`, key);
        }
    }
    
    return key;
}

function clearAPIKey(serviceName) {
    localStorage.removeItem(`${serviceName}_api_key`);
}

// API settings UI
function createAPISettings(serviceName, urlForKey) {
    return `
        <details class="api-settings">
            <summary>⚙️ API Settings</summary>
            <div class="settings-content">
                <label>
                    ${serviceName} API Key:
                    <input type="password" id="${serviceName}_key" 
                           value="${localStorage.getItem(serviceName + '_api_key') || ''}">
                </label>
                <button onclick="saveKey_${serviceName}()">Save</button>
                <button onclick="clearKey_${serviceName}()">Clear</button>
                <p><small>Stored locally in your browser. 
                <a href="${urlForKey}" target="_blank">Get a key</a></small></p>
            </div>
        </details>
    `;
}
```

## UI Feedback

### Loading States

```javascript
function setLoading(elementId, isLoading, loadingText = 'Loading...') {
    const element = document.getElementById(elementId);
    
    if (isLoading) {
        element.disabled = true;
        element.dataset.originalText = element.textContent;
        element.textContent = loadingText;
        element.classList.add('loading');
    } else {
        element.disabled = false;
        element.textContent = element.dataset.originalText;
        element.classList.remove('loading');
    }
}

// Progress bar
function updateProgress(current, total) {
    const percent = Math.round((current / total) * 100);
    const progressBar = document.getElementById('progress');
    progressBar.style.width = `${percent}%`;
    progressBar.textContent = `${percent}%`;
}
```

### Notifications

```javascript
function showNotification(message, type = 'info', duration = 3000) {
    const notification = document.createElement('div');
    notification.className = `notification notification-${type}`;
    notification.textContent = message;
    notification.style.cssText = `
        position: fixed;
        top: 20px;
        right: 20px;
        padding: 1rem 1.5rem;
        background: ${type === 'error' ? '#ef4444' : type === 'success' ? '#10b981' : '#3b82f6'};
        color: white;
        border-radius: 8px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        z-index: 1000;
        animation: slideIn 0.3s ease;
    `;
    
    document.body.appendChild(notification);
    
    setTimeout(() => {
        notification.style.animation = 'slideOut 0.3s ease';
        setTimeout(() => notification.remove(), 300);
    }, duration);
}

function showError(message) {
    showNotification(message, 'error', 5000);
}

function showSuccess(message) {
    showNotification(message, 'success', 3000);
}
```

## Error Handling

### Try-Catch Wrapper

```javascript
async function tryCatch(fn, errorMessage) {
    try {
        return await fn();
    } catch (error) {
        console.error(errorMessage, error);
        showError(`${errorMessage}: ${error.message}`);
        return null;
    }
}

// Usage
const data = await tryCatch(
    () => fetchAPI('https://api.example.com/data'),
    'Failed to fetch data'
);
```

### Form Validation

```javascript
function validateForm(formId) {
    const form = document.getElementById(formId);
    const inputs = form.querySelectorAll('[required]');
    let isValid = true;
    
    inputs.forEach(input => {
        if (!input.value.trim()) {
            input.classList.add('error');
            isValid = false;
        } else {
            input.classList.remove('error');
        }
    });
    
    return isValid;
}

// Email validation
function isValidEmail(email) {
    return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);
}

// URL validation
function isValidURL(url) {
    try {
        new URL(url);
        return true;
    } catch {
        return false;
    }
}
```

## Data Transformation

### JSON ↔ Other Formats

```javascript
// JSON to YAML (requires js-yaml from CDN)
function jsonToYAML(jsonString) {
    const obj = JSON.parse(jsonString);
    return jsyaml.dump(obj);
}

// YAML to JSON (requires js-yaml from CDN)
function yamlToJSON(yamlString) {
    const obj = jsyaml.load(yamlString);
    return JSON.stringify(obj, null, 2);
}

// JSON to CSV
function jsonToCSV(jsonArray) {
    if (!jsonArray.length) return '';
    
    const headers = Object.keys(jsonArray[0]);
    const csvRows = [
        headers.join(','),
        ...jsonArray.map(row => 
            headers.map(header => 
                JSON.stringify(row[header] || '')
            ).join(',')
        )
    ];
    
    return csvRows.join('\n');
}

// CSV to JSON (requires PapaParse from CDN)
function csvToJSON(csvString) {
    const result = Papa.parse(csvString, { header: true });
    return result.data;
}
```

## Debouncing and Throttling

```javascript
// Debounce - wait until user stops typing
function debounce(func, delay = 300) {
    let timeoutId;
    return function (...args) {
        clearTimeout(timeoutId);
        timeoutId = setTimeout(() => func.apply(this, args), delay);
    };
}

// Usage
const input = document.getElementById('search');
input.addEventListener('input', debounce((e) => {
    performSearch(e.target.value);
}, 500));

// Throttle - limit function calls
function throttle(func, limit = 100) {
    let inThrottle;
    return function(...args) {
        if (!inThrottle) {
            func.apply(this, args);
            inThrottle = true;
            setTimeout(() => inThrottle = false, limit);
        }
    };
}
```

## LocalStorage Utilities

```javascript
// Storage with expiry
function setWithExpiry(key, value, ttl) {
    const item = {
        value: value,
        expiry: Date.now() + ttl
    };
    localStorage.setItem(key, JSON.stringify(item));
}

function getWithExpiry(key) {
    const itemStr = localStorage.getItem(key);
    if (!itemStr) return null;
    
    const item = JSON.parse(itemStr);
    if (Date.now() > item.expiry) {
        localStorage.removeItem(key);
        return null;
    }
    
    return item.value;
}

// Clear all localStorage for this tool
function clearAllStorage() {
    if (confirm('Clear all saved data?')) {
        localStorage.clear();
        location.reload();
    }
}
```

## Keyboard Shortcuts

```javascript
function setupKeyboardShortcuts(shortcuts) {
    document.addEventListener('keydown', (e) => {
        const key = e.key.toLowerCase();
        const ctrl = e.ctrlKey || e.metaKey;
        const shift = e.shiftKey;
        
        for (const [combo, handler] of Object.entries(shortcuts)) {
            const [modifiers, targetKey] = combo.split('+');
            const needsCtrl = modifiers.includes('ctrl');
            const needsShift = modifiers.includes('shift');
            
            if (key === targetKey && 
                ctrl === needsCtrl && 
                shift === needsShift) {
                e.preventDefault();
                handler(e);
            }
        }
    });
}

// Usage
setupKeyboardShortcuts({
    'ctrl+enter': convertData,
    'ctrl+c': () => copyToClipboard(output.value),
    'ctrl+shift+c': clearForm
});
```

## Animation Helpers

```javascript
// Smooth scroll to element
function scrollToElement(elementId) {
    document.getElementById(elementId).scrollIntoView({ 
        behavior: 'smooth' 
    });
}

// Fade in
function fadeIn(element, duration = 300) {
    element.style.opacity = 0;
    element.style.display = 'block';
    
    let start = null;
    function animate(timestamp) {
        if (!start) start = timestamp;
        const progress = timestamp - start;
        element.style.opacity = Math.min(progress / duration, 1);
        
        if (progress < duration) {
            requestAnimationFrame(animate);
        }
    }
    
    requestAnimationFrame(animate);
}

// Fade out
function fadeOut(element, duration = 300) {
    let start = null;
    function animate(timestamp) {
        if (!start) start = timestamp;
        const progress = timestamp - start;
        element.style.opacity = Math.max(1 - progress / duration, 0);
        
        if (progress < duration) {
            requestAnimationFrame(animate);
        } else {
            element.style.display = 'none';
        }
    }
    
    requestAnimationFrame(animate);
}
```

## Browser Detection

```javascript
function getBrowserInfo() {
    const ua = navigator.userAgent;
    let browser = 'Unknown';
    
    if (ua.includes('Firefox')) browser = 'Firefox';
    else if (ua.includes('Chrome')) browser = 'Chrome';
    else if (ua.includes('Safari')) browser = 'Safari';
    else if (ua.includes('Edge')) browser = 'Edge';
    
    const isMobile = /iPhone|iPad|iPod|Android/i.test(ua);
    
    return { browser, isMobile };
}

// Feature detection (better than browser detection)
function hasFeature(feature) {
    const features = {
        clipboard: () => navigator.clipboard !== undefined,
        fileAPI: () => window.File !== undefined,
        localStorage: () => {
            try {
                localStorage.setItem('test', 'test');
                localStorage.removeItem('test');
                return true;
            } catch {
                return false;
            }
        },
        webAssembly: () => typeof WebAssembly === 'object'
    };
    
    return features[feature] ? features[feature]() : false;
}
```

These patterns cover most common scenarios for HTML tools. Mix and match as needed!
