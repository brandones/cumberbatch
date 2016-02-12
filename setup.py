# setup.py
#

import os

from setuptools import setup

def read(*paths):
    """Build a file path from *paths* and return the contents."""
    with open(os.path.join(*paths), 'r') as f:
        return f.read()

setup(
  name = 'cumberbatch',
  packages = ['cumberbatch'],
  version = '0.5',
  license = 'Apache License 2.0',
  description = 'Generate names similar to Benedict Cumberbatch.',
  long_description=(read('README.rst')),
  author = 'Brandon Istenes',
  author_email = 'brandonesbox@gmail.com',
  url = 'https://github.com/brandones/cumberbatch',
  download_url = 'https://github.com/brandones/cumberbatch/tarball/0.5',
  keywords = ['names', 'testing', 'fixtures', 'generation', 'generator', 'benedict', 'cumberbatch'],
  classifiers = ['Development Status :: 4 - Beta',
                 'License :: OSI Approved :: Apache Software License']
)
