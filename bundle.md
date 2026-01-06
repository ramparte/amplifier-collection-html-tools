---
bundle:
  name: html-tools
  version: 1.0.0
  description: "Build single-file HTML tools using Simon Willison's proven patterns"
  author: "Amplifier Contributors"
  license: MIT
  repository: https://github.com/ramparte/amplifier-bundle-html-tools

includes:
  - foundation:dev

agents:
  include:
    - html-tools:html-tool-builder

modules:
  - path: modules/tool-html-builder
    description: "CLI tool for generating HTML tools via the html-tool-builder agent"
---

# HTML Tools Bundle

Build single-file HTML applications following Simon Willison's proven patterns for creating browser-based tools without build steps.

## What This Provides

- **html-tool-builder agent**: Expert at building single-file HTML tools
- **html-tool CLI**: Command-line tool for quick HTML tool generation
- **Context files**: CDN libraries, CORS APIs, patterns reference

## Philosophy

Create complete, working HTML tools that:
- Are self-contained in a single .html file
- Work by simply opening in a browser
- Require no build step, no npm, no bundlers
- Are small enough to copy/paste and share easily
- Follow web standards and best practices

## Usage

### Via Agent

Ask Amplifier to build an HTML tool:

```
Build a JSON to YAML converter tool
```

The html-tool-builder agent will:
1. Assess if this is suitable for a single-file tool
2. Build a complete working HTML file
3. Provide usage instructions and testing checklist

### Via CLI (if module installed)

```bash
# Generate a tool
html-tool "JSON to YAML converter" --output converter.html

# Generate and preview
html-tool "Markdown previewer" --preview
```

## Good Candidates for HTML Tools

- Data transformation (JSON/YAML/CSV conversion)
- Visualization (charts, graphs)
- Utilities (calculators, converters, formatters)
- API consumers (CORS-enabled public APIs)
- File processors (client-side)
- Debugging tools (inspectors, validators)
- Content tools (markdown, syntax highlighting)

## Context Files Available

- `context/cdn-libraries.md` - Curated CDN library list
- `context/cors-apis.md` - Known CORS-enabled APIs
- `context/patterns.md` - Code snippets for common patterns
- `context/simon-willison-article.md` - Full reference article
