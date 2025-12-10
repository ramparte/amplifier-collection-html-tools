# Quick Start Guide

Get started building HTML tools in 5 minutes.

## Installation

```bash
amplifier collection add git+https://github.com/microsoft/amplifier-collection-html-tools@main
```

## Your First Tool

### Option 1: Using the Agent (Recommended)

```bash
# Start Amplifier
amplifier

# In chat mode
> Use html-tool-builder to create a JSON to YAML converter
```

The agent will:
1. Assess if it's suitable (✅ yes!)
2. Generate complete HTML code
3. Provide usage instructions
4. Suggest deployment options

### Option 2: Using the CLI

```bash
# Generate and preview
html-tool "JSON to YAML converter" --preview

# Generated file opens in browser
# Try it immediately!
```

## What You Get

Every generated tool includes:

### ✅ Single File
Everything inline - just open in browser, no build step

### ✅ Working Code
Ready to use immediately:
- Input/output areas
- Clear buttons and labels
- Error handling
- Copy to clipboard buttons

### ✅ Best Practices
- Mobile-responsive design
- Accessible HTML
- Clean, readable code
- localStorage for persistence
- Proper error messages

## Next Steps

### Save Your Tool

```bash
# Copy the HTML from agent output to a file
nano my-tool.html

# Or use the CLI which auto-saves
html-tool "My tool description" --output my-tool.html
```

### Test It

```bash
# Open in browser
open my-tool.html

# Or on Linux
xdg-open my-tool.html

# Or just drag the file to your browser
```

### Deploy It

**GitHub Pages** (easiest):
1. Create a GitHub repo
2. Enable Pages in Settings
3. Commit your .html file
4. Access at `https://username.github.io/repo/tool.html`

**GitHub Gist**:
1. Create a new gist
2. Paste your HTML
3. Share the gist URL

**Local**:
- Just keep the .html file
- Open whenever needed
- Share via email/Slack

## Examples to Try

### Simple Converters
```bash
html-tool "Base64 encoder and decoder"
html-tool "Markdown to HTML converter"
html-tool "Unix timestamp converter"
```

### API Tools
```bash
html-tool "GitHub repo info viewer using GitHub API"
html-tool "Weather dashboard using Open Meteo API"
html-tool "PyPI package search"
```

### File Processors
```bash
html-tool "CSV to JSON converter with file upload"
html-tool "Image resizer"
html-tool "Text file diff viewer"
```

### Utilities
```bash
html-tool "QR code generator"
html-tool "Color picker with hex/rgb/hsl conversion"
html-tool "Password strength checker"
```

## Troubleshooting

### Agent not available?
```bash
amplifier collection list
# Should show: html-tools

# If not, reinstall
amplifier collection add git+https://github.com/microsoft/amplifier-collection-html-tools@main
```

### Tool doesn't work?
1. Open browser console (F12)
2. Check for errors
3. Ask agent to fix:
   ```bash
   amplifier
   > Fix this error in my tool: [paste error]
   ```

### Need to iterate?
```bash
amplifier
> Add dark mode to my JSON converter
> Add export to CSV feature
> Improve error messages
```

## Learning More

- **Agent knowledge**: The agent knows all patterns from Simon Willison's article
- **Context files**: See `context/` folder for patterns, APIs, libraries
- **Templates**: See `templates/` folder for starting points
- **Examples**: Visit https://tools.simonwillison.net for inspiration

## Pro Tips

### 1. Start Simple
Build basic version first, then iterate to add features.

### 2. Use Templates
```bash
# Copy a template
cp templates/basic-tool.html my-tool.html

# Customize it or ask agent to modify
```

### 3. Leverage localStorage
Auto-saves user data:
```javascript
// Agent includes this pattern automatically
localStorage.setItem('userData', JSON.stringify(data));
```

### 4. Test CORS First
Before building API tool:
```bash
# Use Simon's cors-fetch tool
# Or ask agent: "Is this API CORS-enabled?"
```

### 5. Keep It Small
If approaching 500 lines, consider:
- Simplifying scope
- Splitting into multiple tools
- Removing unused features

## What's Possible?

✅ **Can do**:
- Data transformation
- Visualizations
- File processing (client-side)
- CORS API calls
- Image manipulation
- WebAssembly (Pyodide, etc.)
- localStorage for state
- Copy/paste operations

❌ **Cannot do**:
- Server-side processing
- Non-CORS APIs
- Databases
- User authentication
- Real-time sync
- Large file uploads (>100MB)

## Getting Help

```bash
# In Amplifier chat
> How do I add syntax highlighting?
> Show me the pattern for file upload
> What CORS APIs are available for weather?

# Agent has full context access
```

## Next Steps

1. **Build your first tool** - Try one of the examples above
2. **Explore patterns** - Read `context/patterns.md` for code snippets
3. **Check APIs** - Browse `context/cors-apis.md` for integration ideas
4. **Share your work** - Deploy to GitHub Pages and share the URL!

Happy building! 🚀
