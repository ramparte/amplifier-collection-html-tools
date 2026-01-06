---
bundle:
  name: html-tools
  version: 1.0.0
  description: "HTML generation and manipulation tools for Amplifier"
  author: "Amplifier Team"
  license: MIT
  repository: https://github.com/ramparte/amplifier-bundle-html-tools

includes:
  - bundle: git+https://github.com/microsoft/amplifier-foundation@main

tools:
  - module: tool-html-builder
    path: modules/tool-html-builder
---

# HTML Tools Bundle

Tools for generating and manipulating HTML content.

## What This Provides

- **HTML Builder Tool** - Generate structured HTML from descriptions
- **Template support** - Work with HTML templates
- **Validation** - Check HTML structure and validity

## Usage

```bash
amplifier run --bundle html-tools "Create an HTML page for..."
```
