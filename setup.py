from setuptools import setup, find_packages

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="databuilder",
    version="0.0.1",
    description="make fake data quick",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dbusteed/databuilder",
    author="Davis Busteed",
    author_email="busteed.davis@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
    ],
    packages=find_packages(),
    install_requires=[
        "pandas~=1.0.5",
        "numpy~=1.19.1",
        "names~=0.3.0",
        "brule~=0.2.0"
    ],
)