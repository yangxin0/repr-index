from setuptools import setup, find_packages

setup(
    name="repr-index",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        # Add your project dependencies here
    ],
    python_requires="==3.11.*",
) 