
.. _started:

Getting started
===============

Explain here, what you need to do in order to get the module up and running

.. let's do cross-referencing

Let's refer to :ref:`the introduction <intro>`.


Required packages
-----------------

Install the following packages on a debian-based distribution:

::

    sudo apt-get install some-package


Start also the following system service
      
::

    sudo service some-service start


Developers
----------

For developing this package using git, install it with these commands:

::

  cd ~/python3_packages
  git clone https://[your-personal-git-repository]/your_package_name
  cd your_package_name
  ln -s $PWD/your_package_name $PYTHONPATH/
        

Production
----------

Production users should use this command to install (use either pip or pip3):

::

  pip3 install git+https://[your-personal-git-repository]/your_package_name


Test the package
----------------
  
Once you've installed this package (either for development or for production), test the installation with (use either ipython or ipython3)

::

  ipython3
  from your_package_name.greeters import UberFancyHelloWorld
  gr=UberFancyHelloWorld(person="Sampsa",age=40)
  print(gr)
    
