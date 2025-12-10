# Useful patterns for building HTML tools

**Source**: https://simonwillison.net/2025/Dec/10/html-tools/  
**Author**: Simon Willison  
**Date**: December 10, 2025

## Overview

HTML tools are HTML applications that combine HTML, JavaScript, and CSS in a single file and use them to provide useful functionality. This approach has proven effective for building over 150 tools in the past year, almost all written by LLMs.

## Key Examples

- **svg-render**: Renders SVG code to downloadable JPEGs or PNGs
- **pypi-changelog**: Generates diffs between different PyPI package releases
- **bluesky-thread**: Provides a nested view of Bluesky discussion threads

Collection: https://tools.simonwillison.net

## The Anatomy of an HTML Tool

### Core Characteristics

1. **Single file**: Inline JavaScript and CSS means minimal hosting/distribution hassle
2. **Avoid React or anything with a build step**: JSX requires compilation, which reduces convenience
3. **Load dependencies from CDN**: jsdelivr, cdnjs, or similar
4. **Keep them small**: A few hundred lines means easy LLM comprehension and quick rewrites
5. **Copy-paste friendly**: Can be cleanly copied into GitHub repositories

### Prototype with Artifacts or Canvas

- **Claude**: "Artifacts" feature (enabled by default)
- **ChatGPT/Gemini**: "Canvas" feature (may need to toggle in tools menu)

**Key tip**: Always add "No React" to prompts to avoid build-step complexity

### Switch to Coding Agents

For complex projects, use coding agents like:
- Claude Code
- Codex CLI

Benefits:
- Can test code themselves using Playwright
- Can create Pull Requests directly
- Handle asynchronous development workflows

## Core Patterns

### 1. Load Dependencies from CDNs

LLM platforms support specific CDNs in their Artifacts/Canvas features. Common sources:
- **cdnjs**: https://cdnjs.com
- **jsdelivr**: https://www.jsdelivr.com

Include package version for reliability.

### 2. Self-Host Elsewhere

Don't rely on LLM platform hosting:
- Tight sandboxes with restrictions
- Can't load external URLs or images
- Warning messages for new users
- Less reliable than static hosting
- May show platform promotions

**Preferred**: GitHub Pages
- Paste HTML into file on github.com
- Hosted on permanent URL in seconds
- No build step makes this trivial

### 3. Copy and Paste

Most useful input/output mechanism:
- Accept pasted content
- Transform it
- Let user copy back to clipboard

**Copy to clipboard buttons**: Essential for mobile (fiddly selection)

**Rich clipboard data**: Operating system clipboards carry multiple formats
- Word processor: Preserves formatting
- Text editor: Strips formatting
- JavaScript paste events can access all formats

Examples:
- **hacker-news-thread-export**: Paste URL, get condensed thread for LLM
- **paste-rich-text**: Copy from page, paste to get HTML (useful on mobile)
- **alt-text-extractor**: Paste images, copy their alt text

### 4. Build Debugging Tools

Essential for understanding what's possible.

**clipboard-viewer**: Most useful debugging tool
- Paste anything (text, rich text, images, files)
- Shows every type of paste data available
- Reveals invisible data for bootstrapping other tools

Other examples:
- **keyboard-debug**: Shows keys/KeyCode values being held
- **cors-fetch**: Reveals if URL can be accessed via CORS
- **exif**: Displays EXIF data for photos

### 5. Persist State in URL

HTML tools lack server-side databases but can store state in URLs:
- Easy to bookmark
- Easy to share
- Good for tools users want to reference later

Example: **icon-editor** - 24x24 icon editor that persists design in URL

### 6. Use localStorage for Secrets or Larger State

localStorage API stores data persistently on user's device without exposing to server:

**Use for**:
- Larger state that doesn't fit in URL
- Secrets like API keys (never in server logs)

Examples:
- **word-counter**: Saves as you type, survives tab close
- **render-markdown**: Saves blog post drafts
- **haiku**: Stores Claude API key for LLM demos

### 7. Collect CORS-Enabled APIs

APIs with open CORS headers are goldmines for HTML tools.

**Valuable CORS APIs**:
- **iNaturalist**: Animal sightings with photos
- **PyPI**: Python package details
- **GitHub**: Public repo content via raw.githubusercontent.com (cached CDN)
- **Bluesky**: All sorts of operations
- **Mastodon**: Generous CORS policies
- **GitHub Gists**: Can persist state to permanent Gist via cross-origin call

Examples:
- **species-observation-map**: iNaturalist sightings on map
- **zip-wheel-explorer**: Fetches .whl from PyPI, unzips in browser
- **github-issue-to-markdown**: Fetches issues/comments, converts to Markdown
- **terminal-to-html**: Optionally saves to Gist

### 8. LLMs Can Be Called Directly via CORS

OpenAI, Anthropic, and Gemini offer CORS-accessible JSON APIs.

**Challenge**: API keys
- Baking keys into HTML = anyone can steal and rack up charges
- Solution: localStorage pattern (ask user to create/paste API key)
- UX friction but works

Examples:
- **haiku**: Claude API writes haiku about webcam image
- **openai-audio-output**: GPT-4o audio speech generation
- **gemini-bbox**: Gemini 2.5 image segmentation

### 9. Don't Be Afraid of Opening Files

`<input type="file">` doesn't need server upload - JavaScript can access content directly.

Examples:
- **ocr**: Opens PDF/image, converts to images, runs OCR (PDF.js + Tesseract.js)
- **social-media-cropper**: Open/paste image, crop to social media dimensions
- **ffmpeg-crop**: Open video, drag crop box, copy ffmpeg command

### 10. Offer Downloadable Files

HTML tools can generate downloads without server help.

JavaScript library ecosystem has packages for generating all file formats.

Examples:
- **svg-render**: Download PNG/JPEG from SVG
- **social-media-cropper**: Download cropped images
- **open-sauce-2025**: Downloadable ICS calendar file

### 11. Pyodide Can Run Python in Browser

Pyodide is Python compiled to WebAssembly for browsers:
- Engineering marvel
- Loads from CDN
- Includes micropip for loading pure-Python packages from PyPI via CORS

Examples:
- **pyodide-bar-chart**: Pyodide + Pandas + matplotlib for charts
- **numpy-pyodide-lab**: Interactive Numpy tutorial
- **apsw-query**: APSW SQLite library showing EXPLAIN QUERY plans

### 12. WebAssembly Opens More Possibilities

WebAssembly enables software from other languages in browsers.

**Squoosh.app**: Convinced of WebAssembly power - best-in-class image compression in browser

Examples:
- **ocr**: Tesseract.js WebAssembly port
- **sloccount**: David Wheeler's Perl/C SLOCCount ported via WebAssembly
- **micropython**: MicroPython WebAssembly for smaller download than Pyodide

### 13. Remix Your Previous Tools

Biggest advantage of 100+ public tools: Easy for LLMs to recombine.

**Approach**:
- Copy/paste previous tool into context
- OR tell coding agent to search for examples
- Source code doubles as documentation

Example: **pypi-changelog** built by:
1. "Look at the pypi package explorer tool"
2. Agent reads zip-wheel-explorer source
3. "Build pypi-changelog.html that uses PyPI API..."

### 14. Record the Prompt and Transcript

Keep records of LLM interactions to grow skills:

**For chat platforms**: Use "share" feature
**For coding agents**: Copy/paste transcript to terminal-to-html, share via Gist

Include transcript links in commit messages when saving tools.

## Go Forth and Build

Getting started:
1. Create free GitHub repository
2. Enable GitHub Pages (Settings → Pages → Source → Deploy from branch → main)
3. Start copying in .html pages generated however you like

All you need is a repository with Pages enabled.

## Philosophy

- **Single-file constraint**: Maximum portability and shareability
- **No build steps**: Immediate usability and deployment
- **LLM-native**: Tools designed to be generated and regenerated by AI
- **Remix culture**: Every tool is a starting point for new tools
- **Progressive capability**: Start simple, add complexity only when needed

## Key Learnings

1. **Simplicity scales**: Keeping tools small makes them more maintainable
2. **CDNs are reliable**: Version-pinned CDN links are trustworthy
3. **Browser capabilities are vast**: Modern browsers can do almost everything
4. **AI excels at this pattern**: LLMs are great at generating single-file apps
5. **Documentation through code**: Working examples are the best documentation
