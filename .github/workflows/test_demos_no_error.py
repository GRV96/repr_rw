from os import system
from pathlib import Path


# This script is meant to run on GitHub's virtual machine ubuntu-latest in a
# CI workflow. It runs the repository's demos to ensure that no error occurs.

repo_root = Path(__file__).resolve().parents[2]
demo_dir = repo_root/"demos"

# demo_write.py must be executed first because
# it produces a file that demo_read.py needs.
system(f"python3 {demo_dir}/demo_write.py")
system(f"python3 {demo_dir}/demo_read.py")
