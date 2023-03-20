from setuptools import setup, find_packages
from typing import List
import os
from pathlib import Path
 
def get_current_version() -> str:
    latest_version = "v0.0.0"
    buffer_file = os.path.join(".dev_logs","buffer.txt")
    if Path(buffer_file).exists():
        os.system(f"git tag > {buffer_file}")
        
        with open(buffer_file) as read_file:
            versions = read_file.readlines()

        for version in versions:
            latest_version = version

    return latest_version.replace("\n", "")

__version__ = get_current_version()

def filter_requirements(requirements: List[str]):
    return list(
        filter(
            lambda line: not line.startswith("certifi")
            and line not in requirements_dev
            and not line.startswith("-e")
            and not line.startswith("wincertstore"),
            requirements,
        )
    )


with open("README.md", "r", encoding="utf-8") as readme_file, open(
    "requirements.txt", "r"
) as requirements_file, open("requirements_dev.txt", "r") as requirements_dev_file:
    long_description = readme_file.read()
    requirements_dev = [line.replace("\n", "")
                        for line in requirements_dev_file.readlines()]
    # filter the odd line containing the ceritifi dependency, and the jaguarelopment dependencies
    requirements = filter_requirements(
        [line.replace("\n", "") for line in requirements_file.readlines()]
    )
    
if __name__ == "__main__":
    setup(
        name="draw_uml_backend",
        version=__version__,
        description="A python application for generating python applications",
        long_description_content_type="text/markdown",
        long_description=long_description,
        package_dir={"": "src"},
        author="Kesler Isoko",
        author_email="uchekesla@gmail.com",
        packages=find_packages(where="src", exclude=(
            "tests*")),
        install_requires=requirements,
        classifiers=[
            "Programming Language :: Python :: 3",
            "Operating System :: OS Independent",
        ],
        extras_require={
            "draw_uml_backend": requirements_dev,
        },
    )