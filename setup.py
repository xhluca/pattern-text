#### PATTERN #######################################################################################
from setuptools import setup, find_packages
from pattern_text import __version__, __author__

setup(
    name='pattern-text',
    version=__version__,
    author=__author__,
    url='https://github.com/xhlulu/pattern-text',
    description='A fork of pattern containing only pattern.text submodule.',
    packages=find_packages(include=['pattern_text*']),
    package_data = {
        "pattern.text.de"         : ["*.txt", "*.xml"],
        "pattern.text.en"         : ["*.txt", "*.xml", "*.slp"],
        "pattern.text.en.wordlist": ["*.txt"],
        "pattern.text.en.wordnet" : ["*.txt", "dict/*"],
        "pattern.text.ru"         : ["*.txt", "*.xml", "*.slp"],
        "pattern.text.ru.wordlist": ["*.txt"],
        "pattern.text.es"         : ["*.txt", "*.xml"],
        "pattern.text.fr"         : ["*.txt", "*.xml"],
        "pattern.text.it"         : ["*.txt", "*.xml"],
        "pattern.text.nl"         : ["*.txt", "*.xml"],
    },
    install_requires=[
        # dependencies here
        'nltk'
    ],
    extras_require={
        # For special installation, e.g. pip install simple-pip-example[dev]
        'dev': ['black']
    },
    include_package_data=True
)