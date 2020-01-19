import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="utilities", # Replace with your own username
    version="0.0.1",
    author="fr0zty",
    author_email="darshn0108@gmail.com",
    description="Misc Utilities Package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/fR0zTy/utilities.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)