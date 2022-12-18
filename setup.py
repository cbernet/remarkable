from setuptools import setup, find_packages


setup(
    name="remarkable",
    version="1.0.1",
    packages=find_packages(exclude=("unittests",)),
    python_requires=">=3.9",
    entry_points={
        "console_scripts": [
            "rk_to_pdf=remarkable.script:main",
        ],
    },
    project_urls={
        "github": "https://github.com/cbernet/remarkable",
    },
)
