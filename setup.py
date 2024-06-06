from setuptools import setup, find_packages

# Read the contents of the README file
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# Read the list of requirements
with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name="HairFastGAN",
    version="0.1.0",
    author="AIRI Institute",
    author_email="author@example.com",
    description="Realistic and Robust Hair Transfer with a Fast Encoder-Based Approach",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/gloompi/HairFastGAN",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=requirements,
    include_package_data=True,
)
