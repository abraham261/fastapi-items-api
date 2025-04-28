from setuptools import setup, find_packages

setup(
    name="fastapi-items-api",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "fastapi",
        "sqlalchemy",
        "pytest",
    ],
)