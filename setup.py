import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="metafun",
    version="0.0.0",
    author="Mingli Yuan",
    author_email="mingli.yuan@gmail.com",
    description="functional meta-programming for python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mountain/metafun",
    project_urls={
        'Documentation': 'https://packaging.python.org/tutorials/distributing-packages/',
        'Source': 'https://github.com/mountain/metafun',
        'Tracker': 'https://github.com/mountain/metafun/issues',
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(),
    python_requires='>=3.9',
    install_requires=[
        'arghandler',
    ],
    test_suite='nose.collector',
    tests_require=['nose'],
    entry_points={
        'console_scripts': [
            'mft = metafun.toolkit:main',
        ]
    }
)

