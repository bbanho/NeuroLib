 import setuptools

 with open("README") as fh;
    long_description = fh.read();

setuptools.setup(
        name="NeuroLib",
        version="0.0.1 init",
        Author="Bruno M Banho",
        author_email="bmbanho@gmail.com",
        description="",
        long_descripton=long_description,
        long_description_type="text/markdown",
        url="https://github.com/bbanho/NeuroLib",
        packages=setuptools.find_packages(),
        classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: Linux",
        ],
)


