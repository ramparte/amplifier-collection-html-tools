# CDN Libraries Reference

Quick reference for commonly useful JavaScript libraries available via CDN.

## General Utilities

### Lodash
**Purpose**: Utility functions for arrays, objects, strings
**CDN**: `https://cdn.jsdelivr.net/npm/lodash@4.17.21/lodash.min.js`
**Usage**: `_.chunk([1,2,3,4], 2)`

### Day.js
**Purpose**: Date/time manipulation (lightweight Moment.js alternative)
**CDN**: `https://cdn.jsdelivr.net/npm/dayjs@1.11.10/dayjs.min.js`
**Usage**: `dayjs().format('YYYY-MM-DD')`

### date-fns
**Purpose**: Modern date utility library
**CDN**: `https://cdn.jsdelivr.net/npm/date-fns@3.0.0/index.min.js`
**Usage**: Tree-shakeable, modular date functions

## Data Transformation

### js-yaml
**Purpose**: YAML parser and generator
**CDN**: `https://cdn.jsdelivr.net/npm/js-yaml@4.1.0/dist/js-yaml.min.js`
**Usage**: `jsyaml.dump(obj)`, `jsyaml.load(str)`

### PapaParse
**Purpose**: CSV parsing and generation
**CDN**: `https://cdn.jsdelivr.net/npm/papaparse@5.4.1/papaparse.min.js`
**Usage**: `Papa.parse(csv)`, `Papa.unparse(data)`

### xml2js (via Browserify)
**Purpose**: XML to JS object conversion
**CDN**: `https://cdn.jsdelivr.net/npm/xml2js@0.6.2/dist/xml2js.min.js`
**Usage**: XML parsing for web

## Markdown and Text

### Marked
**Purpose**: Markdown to HTML converter
**CDN**: `https://cdn.jsdelivr.net/npm/marked@11.0.0/marked.min.js`
**Usage**: `marked.parse('# Hello')`

### DOMPurify
**Purpose**: Sanitize HTML (prevent XSS)
**CDN**: `https://cdn.jsdelivr.net/npm/dompurify@3.0.8/dist/purify.min.js`
**Usage**: `DOMPurify.sanitize(html)`

### Highlight.js
**Purpose**: Syntax highlighting
**CDN**: 
- JS: `https://cdn.jsdelivr.net/gh/highlightjs/cdn-release@11.9.0/build/highlight.min.js`
- CSS: `https://cdn.jsdelivr.net/gh/highlightjs/cdn-release@11.9.0/build/styles/default.min.css`
**Usage**: `hljs.highlightAll()`

### Prism.js
**Purpose**: Lightweight syntax highlighter
**CDN**: 
- JS: `https://cdn.jsdelivr.net/npm/prismjs@1.29.0/prism.min.js`
- CSS: `https://cdn.jsdelivr.net/npm/prismjs@1.29.0/themes/prism.min.css`
**Usage**: Auto-highlights `<code>` blocks

## Visualization

### Chart.js
**Purpose**: Simple, clean charts
**CDN**: `https://cdn.jsdelivr.net/npm/chart.js@4.4.1/dist/chart.umd.min.js`
**Usage**: Canvas-based charts (bar, line, pie, etc.)

### D3.js
**Purpose**: Powerful data visualization
**CDN**: `https://cdn.jsdelivr.net/npm/d3@7.8.5/dist/d3.min.js`
**Usage**: SVG-based custom visualizations

### Plotly.js
**Purpose**: Interactive scientific charts
**CDN**: `https://cdn.plot.ly/plotly-2.27.1.min.js`
**Usage**: `Plotly.newPlot('chart', data)`

### Leaflet
**Purpose**: Interactive maps
**CDN**: 
- JS: `https://unpkg.com/leaflet@1.9.4/dist/leaflet.js`
- CSS: `https://unpkg.com/leaflet@1.9.4/dist/leaflet.css`
**Usage**: OpenStreetMap integration

## File Handling

### JSZip
**Purpose**: Create and read ZIP files
**CDN**: `https://cdn.jsdelivr.net/npm/jszip@3.10.1/dist/jszip.min.js`
**Usage**: `new JSZip().loadAsync(data)`

### FileSaver.js
**Purpose**: Save files from browser
**CDN**: `https://cdn.jsdelivr.net/npm/file-saver@2.0.5/dist/FileSaver.min.js`
**Usage**: `saveAs(blob, 'filename.txt')`

### pdf-lib
**Purpose**: Create and modify PDFs
**CDN**: `https://cdn.jsdelivr.net/npm/pdf-lib@1.17.1/dist/pdf-lib.min.js`
**Usage**: Client-side PDF generation

### PDF.js
**Purpose**: Render PDFs in browser
**CDN**: `https://cdn.jsdelivr.net/npm/pdfjs-dist@4.0.269/build/pdf.min.js`
**Usage**: Mozilla's PDF renderer

## Image Processing

### Tesseract.js
**Purpose**: OCR (Optical Character Recognition)
**CDN**: `https://cdn.jsdelivr.net/npm/tesseract.js@5.0.4/dist/tesseract.min.js`
**Usage**: Extract text from images

### Pica
**Purpose**: High-quality image resizing
**CDN**: `https://cdn.jsdelivr.net/npm/pica@9.0.1/dist/pica.min.js`
**Usage**: Better than canvas for image scaling

### fabric.js
**Purpose**: Canvas manipulation library
**CDN**: `https://cdn.jsdelivr.net/npm/fabric@5.3.0/dist/fabric.min.js`
**Usage**: Image editing, cropping, filters

## Validation and Formatting

### validator.js
**Purpose**: String validation and sanitization
**CDN**: `https://cdn.jsdelivr.net/npm/validator@13.11.0/validator.min.js`
**Usage**: Email, URL, credit card validation

### Prettier (Standalone)
**Purpose**: Code formatting
**CDN**: 
- Parser: `https://unpkg.com/prettier@3.1.1/standalone.js`
- Plugins: Various per language
**Usage**: Format JS, CSS, HTML, etc.

## HTTP and API

### Axios
**Purpose**: HTTP client (fetch alternative)
**CDN**: `https://cdn.jsdelivr.net/npm/axios@1.6.5/dist/axios.min.js`
**Usage**: `axios.get(url).then(response => ...)`

### localforage
**Purpose**: Improved localStorage (IndexedDB wrapper)
**CDN**: `https://cdn.jsdelivr.net/npm/localforage@1.10.0/dist/localforage.min.js`
**Usage**: Async storage API

## WebAssembly

### Pyodide
**Purpose**: Python in the browser
**CDN**: `https://cdn.jsdelivr.net/pyodide/v0.25.0/full/pyodide.js`
**Usage**: `loadPyodide()` then `pyodide.runPython(code)`

### sql.js
**Purpose**: SQLite compiled to JavaScript
**CDN**: `https://cdn.jsdelivr.net/npm/sql.js@1.9.0/dist/sql-wasm.js`
**Usage**: In-browser SQL database

## UI Frameworks (Minimal)

### Pico.css
**Purpose**: Minimal CSS framework (classless)
**CDN**: `https://cdn.jsdelivr.net/npm/@picocss/pico@1.5.11/css/pico.min.css`
**Usage**: Beautiful defaults without classes

### Water.css
**Purpose**: Drop-in CSS framework
**CDN**: `https://cdn.jsdelivr.net/npm/water.css@2.1.1/out/water.min.css`
**Usage**: Just add stylesheet, instant style

### Tailwind CSS (CDN - Play mode)
**Purpose**: Utility-first CSS
**CDN**: `https://cdn.tailwindcss.com`
**Usage**: Development only, not production
**Note**: No build step but limited compared to full Tailwind

## AI/ML

### TensorFlow.js
**Purpose**: Machine learning in browser
**CDN**: `https://cdn.jsdelivr.net/npm/@tensorflow/tfjs@4.15.0/dist/tf.min.js`
**Usage**: Run ML models in browser

### ONNX Runtime Web
**Purpose**: Run ONNX models in browser
**CDN**: `https://cdn.jsdelivr.net/npm/onnxruntime-web@1.16.3/dist/ort.min.js`
**Usage**: Load pre-trained models

## JSON Tools

### JSONPath Plus
**Purpose**: Query JSON with JSONPath
**CDN**: `https://cdn.jsdelivr.net/npm/jsonpath-plus@7.2.0/dist/index-browser-umd.min.js`
**Usage**: `JSONPath({path: '$.store.book[*]', json: data})`

### json-schema-validator
**Purpose**: Validate JSON against schemas
**CDN**: `https://cdn.jsdelivr.net/npm/ajv@8.12.0/dist/ajv7.min.js`
**Usage**: Schema validation

## Tips for Using CDNs

1. **Always specify version**: Prevents breaking changes
   - ✅ `lodash@4.17.21`
   - ❌ `lodash@latest`

2. **Use minified versions**: Faster loading
   - ✅ `library.min.js`
   - ❌ `library.js`

3. **Prefer jsdelivr or cdnjs**: Most reliable
   - jsdelivr.com (npm packages)
   - cdnjs.com (curated libraries)
   - unpkg.com (npm packages, good fallback)

4. **Add integrity hashes** (optional but recommended):
   ```html
   <script src="https://cdn.jsdelivr.net/npm/lodash@4.17.21/lodash.min.js"
           integrity="sha384-..."
           crossorigin="anonymous"></script>
   ```

5. **Test CORS**: Not all CDN resources support CORS
   - Check in browser console
   - Use cors-fetch debugging tool

6. **Consider bundle size**: Keep total dependencies under 500KB when possible

## Finding More Libraries

- **jsdelivr.com**: Search npm packages
- **cdnjs.com**: Browse curated libraries
- **skypack.dev**: Modern ESM CDN
- **esm.sh**: Fast ESM-only CDN

## When NOT to Use CDN

- Library needs build step (TypeScript, JSX)
- Library is too large (>1MB)
- Library is not on reliable CDN
- You need very specific version control

In these cases, consider if the tool really needs to be single-file, or if the complexity justifies a build step.
