import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
        name='helper',
        version='1.0.0',
        author="Shadhini Jayatilake",
        author_email="shadhini.jayatilake@gmail.com",
        license='MIT',
        description="Helper functions useful for weather data integration.",
        long_description=long_description,
        long_description_content_type="text/markdown",
        url="https://github.com/shadhini/curw_helpers",
        packages=setuptools.find_packages(),
        classifiers=[
                "Programming Language :: Python :: 3",
                "License :: OSI Approved :: MIT License",
                "Operating System :: OS Independent",
                ],
        install_requires=['pymysql',
                          'netCDF4',
                          'pandas',
                          'numpy',
                          'PyYAML',
                          'git+https://github.com/shadhini/curw_db_adapter.git'],
        zip_safe=False
        )
