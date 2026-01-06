#!/usr/bin/env python3
"""
HTML Tool Generator CLI - Quick builder for single-file HTML tools.
Uses the html-tool-builder agent under the hood.
"""

import sys
import webbrowser
from pathlib import Path
import subprocess
import re


def extract_html_from_output(output: str) -> str:
    """Extract HTML code from agent output."""
    # Look for code blocks with html, or just code blocks
    patterns = [
        r'```html\n(.*?)\n```',
        r'```\n(<!DOCTYPE html>.*?)\n```',
        r'(<!DOCTYPE html>.*?</html>)'
    ]
    
    for pattern in patterns:
        match = re.search(pattern, output, re.DOTALL | re.IGNORECASE)
        if match:
            return match.group(1).strip()
    
    # If no code block found, check if the whole output is HTML
    if '<!DOCTYPE html>' in output:
        start = output.find('<!DOCTYPE html>')
        end = output.rfind('</html>') + 7
        if start != -1 and end > start:
            return output[start:end].strip()
    
    return None


def generate_filename(description: str) -> str:
    """Generate a filename from description."""
    # Take first few words, clean them up
    words = description.lower().split()[:4]
    name = '-'.join(word.strip('.,!?;:') for word in words if word.isalnum() or '-' in word)
    return f"{name}.html"


def invoke_agent(description: str) -> str:
    """Invoke the html-tool-builder agent via amplifier."""
    try:
        # Call amplifier with the agent
        result = subprocess.run(
            ['amplifier', 'run', '--agent', 'html-tool-builder', description],
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"❌ Error calling amplifier agent: {e.stderr}", file=sys.stderr)
        sys.exit(1)
    except FileNotFoundError:
        print("❌ Amplifier not found. Please install it first:", file=sys.stderr)
        print("   uv tool install git+https://github.com/microsoft/amplifier", file=sys.stderr)
        sys.exit(1)


def main():
    """Main entry point for html-tool CLI."""
    import argparse
    
    parser = argparse.ArgumentParser(
        description='Generate single-file HTML tools using AI',
        epilog='Example: html-tool "JSON to YAML converter" --output converter.html --preview'
    )
    parser.add_argument(
        'description',
        nargs='+',
        help='Description of the tool to build'
    )
    parser.add_argument(
        '--output', '-o',
        help='Output filename (default: auto-generated from description)'
    )
    parser.add_argument(
        '--preview', '-p',
        action='store_true',
        help='Open the generated tool in browser'
    )
    parser.add_argument(
        '--verbose', '-v',
        action='store_true',
        help='Show full agent output'
    )
    
    args = parser.parse_args()
    
    # Join description if multiple words
    description = ' '.join(args.description)
    
    print(f"🤖 Building HTML tool: {description}")
    print()
    
    # Invoke agent
    print("⏳ Calling html-tool-builder agent...")
    output = invoke_agent(description)
    
    if args.verbose:
        print("\n--- Full Agent Output ---")
        print(output)
        print("--- End Output ---\n")
    
    # Extract HTML
    html = extract_html_from_output(output)
    
    if not html:
        print("❌ Failed to extract HTML from agent output.", file=sys.stderr)
        print("Run with --verbose to see full output.", file=sys.stderr)
        sys.exit(1)
    
    # Determine output filename
    output_file = args.output or generate_filename(description)
    output_path = Path(output_file)
    
    # Save to file
    try:
        output_path.write_text(html, encoding='utf-8')
        print(f"✅ Generated: {output_path.absolute()}")
        print(f"   Size: {len(html)} bytes")
    except Exception as e:
        print(f"❌ Failed to save file: {e}", file=sys.stderr)
        sys.exit(1)
    
    # Preview if requested
    if args.preview:
        print(f"\n🌐 Opening in browser...")
        file_url = f"file://{output_path.absolute()}"
        webbrowser.open(file_url)
    
    # Show next steps
    print("\n📋 Next steps:")
    print(f"   • Open: {output_path}")
    print(f"   • Test: open {output_path}")
    if not args.preview:
        print(f"   • Preview: html-tool \"{description}\" --preview")
    print(f"   • Deploy: Commit to GitHub repo with Pages enabled")
    print()


if __name__ == '__main__':
    main()
