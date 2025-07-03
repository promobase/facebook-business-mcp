#!/usr/bin/env python3
"""Local development entry point."""

import sys
from pathlib import Path

# For local development, run the package as a module
if __name__ == "__main__":
    # This allows running with: python main.py or uv run main.py
    import subprocess

    subprocess.run([sys.executable, "-m", "facebook_business_mcp"], cwd=Path(__file__).parent)
