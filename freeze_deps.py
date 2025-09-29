#!/usr/bin/env python3
import os
import tomllib  # Python 3.11+
from pathlib import Path
import subprocess
import sys


def pip_lock(requirements_file: str) -> None:
    cmd = [sys.executable, "-m", "pip", "lock", "-r", requirements_file]
    try:
        result = subprocess.run(cmd, check=True, text=True, capture_output=True)
    except Exception:
        print(f"failed. is pip lock available in your python environment? {sys.executable=}", file=sys.stderr)
        sys.exit(1)
    if result.stdout:
        print(result.stdout, end="")
    elif result.stderr:
        print(result.stderr, end="", file=sys.stderr)


def generate_requirements(lock_file: str, output_file: str):
    # Load the TOML lock file
    with open(lock_file, "rb") as f:
        data = tomllib.load(f)

    lines = []

    # Iterate over all packages
    for package in data.get("packages", []):
        name = package["name"]
        version = package["version"]

        # Start requirement line
        line = f"{name}=={version}"

        # Collect hashes if present
        wheels = package.get("wheels", [])
        hashes = []
        for wheel in wheels:
            wheel_hashes = wheel.get("hashes", {})
            if "sha256" in wheel_hashes:
                hashes.append(wheel_hashes["sha256"])

        # Append hashes in pip format
        if hashes:
            hash_parts = [f"--hash=sha256:{h}" for h in hashes]
            line += " \\\n    " + " \\\n    ".join(hash_parts)

        lines.append(line)

    # Write requirements.txt
    Path(output_file).write_text("\n".join(lines))


if __name__ == "__main__":
    pip_lock('requirements-docs.txt')
    generate_requirements("pylock.toml", "requirements-docs-frozen.txt")
    os.remove('pylock.toml')
    print(f"wrote frozen packages to requirements-docs-frozen.txt")