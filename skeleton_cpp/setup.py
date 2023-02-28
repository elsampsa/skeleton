"""
"""

from setuptools import setup, Extension, find_packages
import sys

# The following line is modified by setver.bash
version = '0.0.0'
ext_modules = []

try:
    import numpy
except ModuleNotFoundError:
    print("Before installing this package, you need to install numpy 'manually'")
    sys.exit(2)

"""Logic here is:

An extension with the name "_skeleton_cpp_module" is installed to the system.
But we don't use that directly as that's simply an .so file..

..we still need the "skeleton_cpp" package, i.e. 

::

    skeleton_cpp/__init__.py
    skeleton_cpp/skeleton_cpp_module.py 

That file ``skeleton_cpp_module.py`` is written by swig & has the nice
interface to python.
"""
ext = Extension("_skeleton_cpp_module", 
    sources             =["skeleton_cpp/skeleton_cpp_module.i", "skeleton_cpp/skeleton_cpp_module.cpp"], 
    # include_dirs        = [getstdout("pkg-config --cflags python"), "./cpp"], # -I flags for python are automatic
    include_dirs        = ["./skeleton_cpp", numpy.get_include()],
    extra_compile_args  = ["-std=c++11"], # , "-O0"],
    # extra_link_args     = [getstdout("pkg-config --libs python3")], # -l flags for python are automatic
    libraries           = [],
    swig_opts           = ["-c++", "-I./skeleton_cpp", "-I"+numpy.get_include()],
    optional = True     # install even if the build fails
)
ext_modules = [ext]
# use like this:
# from skeleton_cpp import skeleton_cpp_module

# # https://setuptools.readthedocs.io/en/latest/setuptools.html#basic-use
setup(
    name = "skeleton_cpp",
    version = version,
    install_requires = [
        "numpy",
    ],
    packages = [
        "skeleton_cpp"
    ],
    # metadata for upload to PyPI
    author           = "Sampsa Riikonen",
    author_email     = "sampsa.riikonen@iki.fi",
    description      = "A template for python projects: cpp extension",
    license          = "MIT",
    keywords         = "python packaging swig numpy cpp",
    long_description ="""
    A template for python projects: cpp extension
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
        # 'License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)',
        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    ext_modules = ext_modules # external modules
)
