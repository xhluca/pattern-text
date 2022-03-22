#### PATTERN #######################################################################################
from setuptools import setup, find_packages
from pattern_text import __version__, __author__

setup(
    name='pattern-text',
    version=__version__,
    author=__author__,
    url='https://github.com/xhlulu/pattern-text',
    description='A fork of pattern containing only pattern.text submodule.',
    packages=find_packages(where='pattern_text'),
    install_requires=[
        # dependencies here
        'nltk'
    ],
    extras_require={
        # For special installation, e.g. pip install simple-pip-example[dev]
        'dev': ['black']
    }
)