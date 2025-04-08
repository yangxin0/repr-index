from setuptools import setup, find_packages

def load_requirements():
    with open("requirements.txt", "r") as f:
        return f.read().splitlines()

setup(
    name="repr-index",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=load_requirements(),
    python_requires="==3.11.*",
) 