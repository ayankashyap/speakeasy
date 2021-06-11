from setuptools import find_packages, setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='speakeasy',
    packages=find_packages(where="speakeasy"),
    include_package_data=True,
    version='0.0.1',
    description='Convert spoken english to written english!',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ayankashyap/speakeasy",
    author='Ayan Kashyap',
    license='MIT',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=['snowballstemmer'],
)
