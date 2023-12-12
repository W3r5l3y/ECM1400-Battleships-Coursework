import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="battleships-pkg-w3r5l3y",
    version="0.0.1",
    author="James Worley",
    author_email="jw1412@exeter.ac.uk",
    description="A game of Battleships in Python for the ECM1400 Battleships coursework.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/W3r5l3y/ECM1400-Battleships-Coursework/",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.9.6",
)
