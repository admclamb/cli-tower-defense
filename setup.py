from setuptools import find_packages, setup

setup(
    name="cli-tower-defense",
    version="0.1.0",
    packages=find_packages(),
    install_requires=["pytest"],
    entry_points={"console_scripts": [
        "tower-defense=game.main:main"
    ]}
)