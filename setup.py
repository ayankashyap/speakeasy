import pathlib
from setuptools import find_packages, setup

HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text()

setup(
    name='speakeasy',
    packages=find_packages(include=['speakeasy']),
    version='0.1.0',
    description='Convert spoken english to written english!',
    long_description=README,
    long_description_content_type="text/markdown",
    author='Ayan Kashyap',
    license='MIT',
    install_requires=['snowballstemmer']
)
