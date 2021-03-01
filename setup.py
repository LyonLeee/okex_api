from setuptools import setup, find_packages
from okex_api import __version__

setup(
    name='okex_api',
    version=__version__,
    packeges=find_packages,
    requires=[
        'websockets(>=6.0)'
    ],
)