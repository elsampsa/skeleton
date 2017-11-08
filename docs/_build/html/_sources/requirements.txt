
Getting started
===============


.. let's do cross-referencing

So, you have red :ref:`the introduction <about>`.


Required packages
-----------------

Install the following packages on a debian-based distribution:

::

    sudo apt-get install some-package

Start also the following system service
      
::

    sudo service some-service start

        
Once you've installed this package, test the code with (use either ipython or ipython3)

::

    ipython3
    from skeleton.greeters import UberFancyHelloWorld
    gr=UberFancyHelloWorld(person="Sampsa",age=40)
    print(gr)
    

Code Organization
-----------------

So, let's get back to this tutorial.  This is a module that has a single submodule called "greeters" that is organized as follows:

.. remember: "|" forces line-breaks

greeters
  | __init__.py
  | base.py
  | fancy.py
  
The idea is that "base.py" has some base class definitions that are used bu "fancy.py" to create derived classes.  __init__.py has been tweaked so that user can import with

::

  from skeleton.greeters import UberFancyHelloWorld
  
instead of the cumbersome

::

  from skeleton.fancy.greeters import UberFancyHelloWorld
  
(also, the api user should not be bothered with the internal inheritance, etc.)

So, I suggest you open in your editor all files of the "greeters" submodule and study them a bit.


Quick testing
-------------

Each module file under "greeters" works also as a stand-alone test.  Go to the "greeters" directory and try (either ipython or ipython3):

::
  
    ipython3
    %run fancy.py
    
Or just (either python or python3):

::

    python3 fancy.py


This is not proper testing, though.  It's quick'n'dirty testing during development.  Separate testing programs for systematic testing are a good idea to include in your module package.


Packaging
---------
  
After we have made the correct "scaffolded" directory structure (:ref:`see here <about>`), everything works like magic.  At the main "skeleton" directory, do (either python or python3)

::

  python3 setup.py sdist

  
Your distributable python package is now in "dist/skeleton-0.1.tar.gz".  You can install it with pip(3).

The setup.py script automatically finds and includes python packages to the distribution package.  In "MANIFEST.in" we also tell it to include the complete "docs/" directory an auxiliary file from the "greeters" submodule



Miscellaneous
-------------

Some other points:
  * Check out in the source code, how I init and check a large number of parameters in the constructor
  * It is also a good idea to add "exceptions.py" under "greeters".  This way you can quickly see what custom exceptions must be handled.


