from setuptools import setup, Extension, find_packages
import sys

is_py3 = (sys.version_info >= (3,0))

# # enable the following section if you need to run a post-install script
"""
from setuptools.command.install import install

class PostInstallCommand(install):
  # ripped from:
  # https://stackoverflow.com/questions/20288711/post-install-script-with-python-setuptools
  # Post-installation for installation mode
  def run(self):
    super(PostInstallCommand,self).run()
    print("\n**running post install**\n")
    # # PUT YOUR POST-INSTALL SCRIPT HERE or CALL A FUNCTION
    # # If, at this point you are referring to your python module direction, say, with the aid of the inspect module
    # # then those directories are wrong: they are still temp directories, i.e. "/tmp/whatever"
"""

# # The short X.Y version
version = '0.1' # WARNING: modified by setver.bash

# # https://setuptools.readthedocs.io/en/latest/setuptools.html#basic-use
setup(
  name = "skeleton",
  version = version,
  install_requires = [
    'docutils>=0.3', # # List here the required packages!  List them also in "docs/snippets/requirements.txt"
    ],

  packages = find_packages(), # # includes python code from every directory that has an "__init__.py" file in it.  If no "__init__.py" is found, the directory is omitted.  Other directories / files to be included, are defined in the MANIFEST.in file
  
  include_package_data=True, # # conclusion: NEVER forget this : files get included but not installed
  # # "package_data" keyword is a practical joke: use MANIFEST.in instead
  
  
  # # enable this if you need to run a post-install script:
  #cmdclass={
  #  'install': PostInstallCommand,
  #  },
  
  # metadata for upload to PyPI
  author = "Sampsa Riikonen",
  author_email = "sampsa.riikonen@iki.fi",
  description = "A template for python projects",
  license = "MIT",
  keywords = "python sphinx packaging",
  url = "http://www.iki.fi/sampsa.riikonen"
)
