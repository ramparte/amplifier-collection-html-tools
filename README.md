# HTML Tools Collection for Amplifier

Build single-file HTML tools using Simon Willison's proven patterns for browser-based utilities - no build steps, no React, just simple HTML+CSS+JS that works by opening in a browser.

## What This Collection Provides

### 🤖 The `html-tool-builder` Agent

An expert AI agent that creates complete, working HTML tools following best practices:
- Single-file HTML (inline CSS/JS)
- No build steps required
- CDN-loaded dependencies
- CORS-friendly API integration
- LocalStorage for secrets
- Copy/paste/file operations
- Small and maintainable (<500 lines)

### 📚 Knowledge Base

Context files loaded automatically by the agent:
- **simon-willison-article.md** - Complete patterns and philosophy
- **cdn-libraries.md** - Curated list of useful CDN libraries
- **cors-apis.md** - Known CORS-enabled APIs with examples
- **patterns.md** - Ready-to-use code snippets

### 🛠️ CLI Tool

`html-tool` command for quick generation:
```bash
html-tool "JSON to YAML converter" --output converter.html --preview
```

## Installation

```bash
# Install the collection
amplifier collection add git+https://github.com/microsoft/amplifier-collection-html-tools@main

# Verify installation
amplifier collection list
amplifier collection show html-tools

# The html-tool CLI is automatically available
html-tool --help
```

## Quick Start

### Using the Agent Directly

```bash
# Start Amplifier
amplifier

# In chat mode, delegate to the agent
> Use html-tool-builder to create a markdown to HTML converter

# Or via command line
amplifier run --agent html-tool-builder "Build a CSV to JSON converter"
```

### Using the CLI Tool

```bash
# Generate a tool
html-tool "JSON to YAML converter"

# Generate and preview in browser
html-tool "Image resizer" --preview

# Specify output filename
html-tool "Color picker" --output my-picker.html
```

### What You Get

The agent provides:
1. **Assessment** - Is this suitable for a single-file HTML tool?
2. **Complete HTML** - Ready to save and use
3. **Usage instructions** - How to use the tool
4. **Deployment options** - GitHub Pages, Gist, etc.
5. **Testing checklist** - What to verify

## Example Interactions

### Example 1: Data Converter

```bash
amplifier run --agent html-tool-builder "Create a JSON to YAML converter with copy button"
```

**You get:**
- Complete HTML file
- Paste/type JSON input
- Convert button
- Copy to clipboard button
- Error handling
- localStorage auto-save

### Example 2: API Consumer

```bash
amplifier run --agent html-tool-builder "Build a GitHub repo search tool using the GitHub API"
```

**You get:**
- Search input field
- CORS-friendly GitHub API calls
- Results display
- Rate limiting awareness
- Error handling

### Example 3: File Processor

```bash
amplifier run --agent html-tool-builder "Create a CSV viewer with sorting and filtering"
```

**You get:**
- File upload support
- Drag-and-drop
- Client-side CSV parsing
- Interactive table
- Export functionality

## What Can You Build?

### ✅ Perfect Candidates

- **Data transformation**: JSON ↔ YAML, CSV processing, format converters
- **Visualization**: Charts, graphs, maps, data display
- **Utilities**: Calculators, converters, formatters, generators
- **API consumers**: Tools using CORS-enabled public APIs
- **File processors**: Client-side file reading, manipulation, export
- **Debugging tools**: Inspectors, validators, testers
- **Content tools**: Markdown renderers, syntax highlighters, diff viewers
- **Image tools**: Crop, resize, format conversion (client-side)

### ❌ Not Suitable

- Requires backend/database
- Needs non-CORS APIs
- Complex authentication systems
- Real-time multi-user collaboration
- Very large file processing (>100MB)

## Core Principles

The agent follows these principles:

1. **Single file**: Everything inline - HTML, CSS, JavaScript
2. **No build step**: Works by opening in browser
3. **No React**: Vanilla JS or lightweight CDN libraries only
4. **Small scope**: Target under 500 lines total
5. **CORS-friendly**: Only use accessible APIs
6. **Secure**: API keys in localStorage, never in source
7. **Accessible**: Clear UI, keyboard support, error messages

## Deployment Options

Generated tools can be deployed anywhere:

### GitHub Pages (Recommended)
```bash
# 1. Create/use a GitHub repository
# 2. Enable Pages (Settings → Pages → Deploy from main)
# 3. Commit your .html file
# 4. Access at https://username.github.io/repo/tool.html
```

### GitHub Gist
```bash
# Create a secret gist with your HTML file
# Share the gist URL
```

### Local Use
```bash
# Just open the HTML file in any browser
open my-tool.html
```

### Any Static Host
- Netlify Drop
- Vercel
- Cloudflare Pages
- Your own web server

## Advanced Usage

### Iterating on Tools

```bash
# Generate initial version
amplifier run --agent html-tool-builder "Create a color picker"

# Save to file, then enhance
amplifier run --agent html-tool-builder \
  "Add these features to my color picker: hex/rgb/hsl conversion, copy to clipboard"
```

### Accessing Context Files

In chat mode, you can reference the knowledge base:

```bash
amplifier

> What CORS APIs are available for weather data?
# Agent can access @context/cors-apis.md

> Show me the pattern for file upload with drag-and-drop
# Agent can access @context/patterns.md
```

### Learning from Examples

The agent learns from Simon Willison's collection:
- Over 150 real-world examples
- Proven patterns and techniques
- Best practices baked in

## Knowledge Base Contents

### CDN Libraries (`cdn-libraries.md`)

Curated libraries available via CDN:
- **Data**: js-yaml, PapaParse, xml2js
- **Markdown**: Marked, DOMPurify, Highlight.js
- **Visualization**: Chart.js, D3.js, Plotly, Leaflet
- **Files**: JSZip, FileSaver, pdf-lib, PDF.js
- **Images**: Tesseract.js (OCR), Pica, fabric.js
- **WebAssembly**: Pyodide, sql.js
- **UI**: Pico.css, Water.css, Tailwind (play mode)

### CORS APIs (`cors-apis.md`)

Known working APIs:
- **Package registries**: PyPI, npm
- **GitHub**: Raw content, API, Gists
- **Nature**: iNaturalist observations
- **Weather**: Open Meteo
- **Social**: Bluesky, Mastodon
- **AI**: OpenAI, Anthropic, Gemini (require API keys)
- **Geographic**: OpenStreetMap

### Patterns (`patterns.md`)

Ready-to-use code snippets:
- State management (URL, localStorage)
- Copy and paste handling
- File upload/download
- CORS API calls
- Error handling
- UI feedback (loading, notifications)
- Data transformation
- Keyboard shortcuts

## Tips & Best Practices

### Start Simple
```bash
# Begin with basic version
html-tool "JSON formatter"

# Iterate to add features
html-tool "Add syntax highlighting and error messages to my JSON formatter"
```

### Test Immediately
Generated tools should work immediately:
1. Save to .html file
2. Open in browser
3. Test core functionality
4. Report issues back to agent for fixes

### Use localStorage for Secrets
```javascript
// Agent automatically includes this pattern for API keys
const apiKey = localStorage.getItem('api_key');
if (!apiKey) {
    const key = prompt('Enter your API key:');
    localStorage.setItem('api_key', key);
}
```

### Share Easily
Single-file tools are perfect for sharing:
- Email attachment
- Copy/paste code
- GitHub Gist
- GitHub Pages

## Troubleshooting

### "Agent not found"
```bash
# Verify collection is installed
amplifier collection list

# Should show: html-tools

# Reinstall if needed
amplifier collection add git+https://github.com/microsoft/amplifier-collection-html-tools@main
```

### "Tool doesn't work"
1. Check browser console (F12) for errors
2. Verify CDN libraries loaded
3. Test CORS APIs in isolation
4. Ask agent to fix specific issues

### "CLI not working"
```bash
# Verify collection is installed properly
which html-tool

# Reinstall collection
amplifier collection add git+https://github.com/microsoft/amplifier-collection-html-tools@main --force
```

## Examples Gallery

### Data Converters
- JSON ↔ YAML
- CSV ↔ JSON
- Markdown → HTML
- Base64 encoder/decoder

### Visualizations
- Chart generator
- Data table viewer
- Map plotter
- Graph visualizer

### Utilities
- QR code generator
- Color picker
- Unit converter
- Hash calculator

### API Tools
- GitHub repo explorer
- Weather dashboard
- Package search (PyPI/npm)
- Species observer (iNaturalist)

### File Tools
- Image resizer
- PDF viewer
- CSV editor
- ZIP extractor

## Philosophy

This collection embodies Simon Willison's philosophy:

> "The best code is often the simplest. A few hundred lines of HTML, CSS, and JavaScript that just works when you open it in a browser - no installation, no build step, no dependencies to manage. That's the sweet spot for rapid tool development with AI."

**Core beliefs:**
- Single-file constraint = maximum portability
- No build steps = immediate usability
- LLM-native = designed for AI generation
- Remix culture = every tool is a starting point
- Progressive capability = start simple, add complexity only when needed

## Contributing

Found a useful pattern? Discovered a great CORS API? Improvements welcome!

1. Fork the repository
2. Add to context files (`context/*.md`)
3. Submit pull request
4. Share your generated tools!

## Resources

- **Simon Willison's collection**: https://tools.simonwillison.net
- **Original article**: https://simonwillison.net/2025/Dec/10/html-tools/
- **Amplifier**: https://github.com/microsoft/amplifier
- **CDN resources**: 
  - https://www.jsdelivr.com
  - https://cdnjs.com
  - https://unpkg.com

## License

MIT License - see LICENSE file

## Version

1.0.0 - Initial release

---

**Built with ❤️ using Amplifier**
