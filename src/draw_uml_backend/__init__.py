import os
from pathlib import Path


def get_current_version() -> str:
    latest_version = "v0.0.0"
    buffer_file = os.path.join(".dev_logs", "buffer.txt")
    if Path(buffer_file).exists():
        os.system(f"git tag > {buffer_file}")

        with open(buffer_file) as read_file:
            versions = read_file.readlines()

        for version in versions:
            latest_version = version

    return latest_version.replace("\n", "")


__version__ = get_current_version()
