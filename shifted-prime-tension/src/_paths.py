"""
Shared path configuration for the shifted-prime-tension project.

All scripts import DATA and FIGURES from here so that outputs land in
project-relative directories regardless of where the script is invoked from.
"""
from pathlib import Path

# Project root = parent of the src/ directory containing this file
ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
FIGURES = ROOT / "figures"

DATA.mkdir(exist_ok=True)
FIGURES.mkdir(exist_ok=True)
