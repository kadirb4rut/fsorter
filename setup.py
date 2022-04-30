import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="fsorter",
    version="1.0",
    author="Kadir Barut",
    author_email="kadirrbrtt@gmail.com",
    description="filename_sorter.py programı görüntü dosyalarını dosya ismi sonundaki sayılara göre sıralama işlemi yapar.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kadirrbrtt/filename_sorter",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    python_requires='>=3.5.5',
    install_requires=[]
)