import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
    
""" 

setuptools.setup(
    name="fsorter",
    author="Kadir Barut",
    version='',
    author_email="kadirrbrtt@gmail.com",
    description="This program checks the numeric values ​​at the end of the  file names in the folder and sorts the file names from the smallest number to the larger number.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kadirrbrtt/fsorter",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    python_requires='>=3.5.5',
    install_requires=[]
)
"""



setuptools.setup(
    name="fsorter",
    version="2.0",
    description="File sorting program according to the numbers in the file name.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kadirrbrtt/fsorter",
    author="Kadir Barut",
    author_email="kadirrbrtt@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
    ],
    packages=setuptools.find_packages(),
    include_package_data=True,
    
    
)