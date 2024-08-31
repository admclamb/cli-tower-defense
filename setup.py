from setuptools import setup

with open("README.md", 'r') as f:
    long_description = f.read()

setup(
    name="cli-tower-defense",
    version="0.1.0",
    description="CLI Tower Defense Game",
    license="MIT",
    long_description=long_description,
    author="Anthony Mclamb",
    author_email="adylanmclamb@gmail.com",
    packages=["game"],
    extras_require={
        'dev': [
            'pytest==8.3.2',
            'mypy==1.11.2',
        ],
    },
    entry_points={
        'console_scripts': [
            'tower-defense=game.main:main',
        ],
    },
)