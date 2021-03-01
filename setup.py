from setuptools import setup, find_packages
from OKexApi import __version__

setup(
    name='OKexApi',
    version=__version__,
    packeges=find_packages,
    requires=[
        'websockets(>=6.0)'
    ],
)