from setuptools import setup, Extension, find_packages
import sys

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

# The following line is modified by setver.bash
version = '0.0.0'

ext = Extension("_sharedmem", 
            sources             =["cpp/sharedmem.i", "cpp/sharedmem.cpp"], 
            # include_dirs        = [getstdout("pkg-config --cflags python"), "./cpp"], # -I flags for python are automatic
            include_dirs        = ["./cpp"],
            extra_compile_args  = ["-std=c++11"],
            # extra_link_args     = [getstdout("pkg-config --libs python3")], # -l flags for python are automatic
            libraries           = [],
            swig_opts           = ["-c++", "-I ./cpp"]
        )

ext_modules = [ext]

# # https://setuptools.readthedocs.io/en/latest/setuptools.html#basic-use
setup(
    name = "skeleton",
    version = version,
    install_requires = [
        "PyYAML",
        'docutils>=0.3', # # List here the required packages!  List them also in "docs/snippets/requirements.txt"
    ],

    packages = find_packages(), # # includes python code from every directory that has an "__init__.py" file in it.  If no "__init__.py" is found, the directory is omitted.  Other directories / files to be included, are defined in the MANIFEST.in file
    
    include_package_data=True, # # conclusion: NEVER forget this : files get included but not installed
    # # "package_data" keyword is a practical joke: use MANIFEST.in instead
    
    # # WARNING: If you are using namespace packages, automatic package finding does not work, so use this:
    #packages=[
    #    'skeleton.subpackage1'
    #],
    
    #scripts=[
    #    "bin/somescript"
    #],

    # # "entry points" get installed into $HOME/.local/bin
    # # https://unix.stackexchange.com/questions/316765/which-distributions-have-home-local-bin-in-path
    #entry_points={
    #    'console_scripts': [
    #        'my-command = skeleton.subpackage1.cli:main' # this would create a command "my-command" that maps to skeleton.subpackage1.cli method "main"
    #    ]
    #},
    
    # # enable this if you need to run a post-install script:
    #cmdclass={
    #  'install': PostInstallCommand,
    #  },
    
    # metadata for upload to PyPI
    author           = "Sampsa Riikonen",
    author_email     = "sampsa.riikonen@iki.fi",
    description      = "A template for python projects",
    license          = "MIT",
    keywords         = "python sphinx packaging",
    url              = "https://elsampsa.github.io/skeleton/", # project homepage
    
    long_description ="""
    A python scaffold project
    """,
    long_description_content_type='text/plain',
    # long_description_content_type='text/x-rst', # this works
    # long_description_content_type='text/markdown', # this does not work
    
    classifiers      =[  # Optional
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',
        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Operating System :: POSIX :: Linux',
        # 'Topic :: Multimedia :: Video', # set a topic
        # Pick your license as you wish
        'License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)',
        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    #project_urls={ # some additional urls
    #    'Tutorial': 'https://elsampsa.github.io/skeleton/'
    #},
    ext_modules = ext_modules # external modules
)
