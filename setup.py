import setuptools
import thyme


with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="thyme",
    version=thyme.__version__,
    author="Apostolos Georgiadis",
    author_email="apostolos.georgiadis@nfiniity.com",
    description="Timing utilities for developers",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/apgeorg/thyme.git",
    packages=setuptools.find_packages(),
    classifiers=[
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules'
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
