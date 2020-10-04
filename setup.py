from setuptools import setup, find_packages


def readme() -> str:
    with open("README.md") as f:
        return f.read()


setup(
    name="abm",
    version="0.0.0",
    description="Agent-Based Model for Pandemic Simulations",
    long_description=readme(),
    classifiers=["Agent Based Model :: Python :: 3.6"],
    python_requires=">=3.6",
    packages=find_packages(),
    include_package_data=True,
    install_requires=["numpy", "pandas", "matplotlib",],
)
