from setuptools import setup, Extension, find_packages

# https://setuptools.readthedocs.io/en/latest/setuptools.html#basic-use
setup(
  name = "skeleton",
  version = "0.1",
  install_requires = ['docutils>=0.3'],

  packages = find_packages(),  
  
  include_package_data=True, # conclusion: NEVER forget this : files get included but not installed
  # "package_data" keyword is a practical joke: use MANIFEST.in instead
  
  # metadata for upload to PyPI
  author = "Sampsa Riikonen",
  author_email = "sampsa.riikonen@iki.fi",
  description = "A template for python projects",
  license = "MIT",
  keywords = "python sphinx packaging",
  url = "http://www.iki.fi/sampsa.riikonen"
)
