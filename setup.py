from setuptools import setup, find_packages

setup(
    name="common-report-module",
    description="A Helper Module for Semester-Stats",
    author="Rushyanth S",
    author_email="42034084+Rushyanth111@users.noreply.github.com",
    python_requires=">=3.7.0",
    url="https://github.com/Rushyanth111/Common-Report-Module",
    packages=find_packages(exclude=[".venv", "tests"]),
    install_requires=["pydantic", "requests"],
    version="0.1.0",
)
