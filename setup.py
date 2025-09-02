from setuptools import setup, find_packages

# Read long description from README.md
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

AUTHOR_NAME = "Yassine"
SRC_REPO = "src"
LIST_OF_REQUIREMENTS = ["streamlit", "requests", "gdown", "pandas", "numpy"]

setup(
    name=SRC_REPO,
    version="0.0.1",
    author=AUTHOR_NAME,
    author_email="yassin.chaouachi51@gmail.com",
    description="A small example package for movie recommendation",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    python_requires=">=3.7",
    install_requires=LIST_OF_REQUIREMENTS,
)
