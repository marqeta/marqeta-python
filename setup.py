from setuptools import setup



setup(
    name='marqeta',
    version='1.0.0',
    description='marqeta python-SDK',
    author='Maqeta Developer',
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