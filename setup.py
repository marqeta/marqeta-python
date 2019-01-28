from setuptools import setup
from marqeta.version import __version__



setup(
    name='marqeta',
    version= __version__,
    description='marqeta python-SDK',
    author='Marqeta Developer',
    author_email='development@marqeta.com',
    packages=['marqeta'],
    long_description= "long_description",
    long_description_content_type="text/markdown",
    url="https://github.com/marqeta-python",
    classifiers=[
        "Programming Language :: Python :: 2 and 3",
        "License :: ",
        "Application:: ",
    ],
    install_requires=['requests']

)