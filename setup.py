import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="search_rcsb",
    version="0.1.1",
    author="Cong Wang",
    author_email="wangimagine@gmail.com",
    description="This package talks to RCSB server using its RESTful API.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/carbonscott/search_rcsb",
    keywords = ['pdb', 'rcsb'],
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
