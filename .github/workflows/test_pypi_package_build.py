from os import system
from pathlib import Path


# This script is meant to run on GitHub's virtual machine ubuntu-latest in a CI
# workflow. It builds the PyPI package and installs it to ensure the
# installation works. However, the script does not upload the package to PyPI.

repo_root = Path(__file__).resolve().parents[2]

system(f"python3 {repo_root}/setup.py sdist")

latest_dist = list((repo_root/"dist").glob("repr_rw-*.tar.gz"))[-1]

system(f"pip3 install --no-cache-dir {latest_dist}")
