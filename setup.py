from setuptools import setup, find_packages
from OkexApi import __version__

setup(
    name='OkexApi',
    version=__version__,
    packeges=find_packages,
    requires=[
        'websockets(>=6.0)'
    ],
)