from setuptools import setup, Extension, find_packages
import sys, os

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

separate_cpp_module = False
if '--separate-cpp-module' in sys.argv:
    index = sys.argv.index('--separate-cpp-module')
    sys.argv.pop(index)  # Removes the '--separate_cpp_module'
    # value = sys.argv.pop(index)  # Returns the element after the '--foo'
    #if separate_cpp_module not in ["true", "false"]:
    #    print("please use --separate_cpp_module true / --separate_cpp_module false")
    separate_cpp_module = True

# The following line is modified by setver.bash
version = '0.0.0'

ext_modules = []
"""You can choose to "bundle" the cpp extension module into the main package,
or create a separate module for it.  In the latter case, please comment out
the cpp extension module section here.  Please see also the discussion in 
skeleton_cpp/README.md
"""

if separate_cpp_module:
    print("NOT compiling/bundling the CPP module")
else: # cpp module is bundled to the main package as an extension
    #"""example cpp extension starts>
    try:
        import numpy
    except ModuleNotFoundError:
        print("Before installing this package, you need to install numpy 'manually'")
        sys.exit(2)

    ext = Extension("_skeleton_cpp_module", 
        sources             =["skeleton_cpp/skeleton_cpp/skeleton_cpp_module.i", "skeleton_cpp/skeleton_cpp/skeleton_cpp_module.cpp"], 
        # include_dirs        = [getstdout("pkg-config --cflags python"), "./cpp"], # -I flags for python are automatic
        include_dirs        = ["./skeleton_cpp/skeleton_cpp", numpy.get_include()],
        extra_compile_args  = ["-std=c++11"],
        # extra_link_args     = [getstdout("pkg-config --libs python3")], # -l flags for python are automatic
        libraries           = [],
        # swig_opts           = ["-c++", "-outdir something", "-I./cpp"]# this will never work, swig insists in "Unrecognized option -outdir somedir""
        swig_opts           = ["-c++", "-I./skeleton_cpp/skeleton_cpp", "-I"+numpy.get_include()],
        # optional = True     # install even if the build fails
        optional = False
    )
    ext_modules = [ext]
    #"""<example cpp extensions stops

this_folder = os.path.dirname(os.path.realpath(__file__))
path = this_folder + '/requirements.txt'
install_requires = [] # Here we'll get: ["gunicorn", "docutils>=0.3", "lxml==0.5a7"]
if os.path.isfile(path):
    with open(path) as f:
        install_requires = f.read().splitlines()

# # https://setuptools.readthedocs.io/en/latest/setuptools.html#basic-use
setup(
    name = "skeleton",
    version = version,
    #install_requires = [
    #    "PyYAML",
    #    'docutils>=0.3', # # List here the required packages
    #],

    install_requires = install_requires, # instead, read from a file (see above)

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
    entry_points={
        'console_scripts': [
            'skeleton-command = skeleton.cli:main' # this would create a command "skeleton-command" that maps to skeleton/cli.py, method "main"
        ]
    },
    
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
        # https://autopilot-docs.readthedocs.io/en/latest/license_list.html
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
