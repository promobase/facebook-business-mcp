"""Local development entry point."""

import sys
from pathlib import Path

if __name__ == "__main__":
    import subprocess

    subprocess.run([sys.executable, "-m", "facebook_business_mcp"], cwd=Path(__file__).parent)
