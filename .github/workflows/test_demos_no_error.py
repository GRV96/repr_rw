#!/bin/python3

from os import system
from pathlib import Path


_REPO_ROOT = Path(__file__).resolve().parents[2]
_DEMO_DIR = _REPO_ROOT/"demos"

# This script is meant to run on GitHub's virtual machine ubuntu-latest in a
# CI workflow. It runs the repository's demos to ensure that no error occurs.

system(f"python3 {_DEMO_DIR}/demo_write.py")
system(f"python3 {_DEMO_DIR}/demo_read.py")
