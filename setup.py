from setuptools import setup, find_packages
from marqeta.version import __version__

with open("requirements.txt", "r") as requirements:
    install_requires = requirements.read()

with open("README.md") as f:
    long_description = f.read()

setup(
    name="marqeta",
    version=__version__,
    description="Marqeta Python SDK",
    author="Marqeta, Inc.",
    url="https://github.com/marqeta/marqeta-python",
    license="MIT",
    keywords=["marqeta"],
    project_urls={
        "Documentation": "https://marqeta.com/api",
        "Source Code": "https://github.com/marqeta/marqeta-python",
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    packages=find_packages(exclude=["tests", "tests.*"]),
    include_package_data=True,
    install_requires=install_requires,
    long_description=long_description,
    long_description_content_type="text/markdown",
)
