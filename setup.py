from setuptools import setup, find_packages

VERSION = '0.0.2'
DESCRIPTION = 'A google dorking library and cli.'
LONG_DESCRIPTION = 'Use google dorking directly in python and from your terminal.'

# Setting up
setup(
    name="ventus",
    version=VERSION,
    author="aaronlyy (Aaron Levi)",
    author_email="<aaronlevican@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=["ventus"],
    install_requires=['requests', 'bs4', 'beautifulsoup4', 'click'],
    keywords=['dorking', 'google', 'scraping', 'google dorking', 'hacking', 'cracking'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)