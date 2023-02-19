import setuptools

# include additional packages as well - requests , tabulate , json

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="sqliteencrypt", # Replace with your own username
    version="0.22",
    author="Dave Kosik",
    author_email="dave@draegyn.com",
    description="Light weight, easy to use sqlite wrapper with built in encryption. AN extension to Harsh Native version.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/KosDav/pysqlitecipher",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],

    install_requires=[
   'cryptography',
   'onetimepad',
    ],

    python_requires='>=3.6',
)
