
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

Developers should install this package with:

::

  cd ~/python3_packages
  git clone https://[your-personal-git-repository]/your_package_name
  cd your_package_name
  ln -s $PWD/your_package_name $PYTHONPATH/
        

.. _production:
        
Production
----------

Production users should use this command to install the latest version (use either pip or pip3):

::

  pip3 install git+git://[your-personal-git-repository]/your_package_name


To install a specific version of the package, use

::

  pip3 install git+git://[your-personal-git-repository]/your_package_name@version_tag
  
  
Test the package
----------------
  
Once you've installed this package (either for development or for production), test the installation with (use either ipython or ipython3)

::

  ipython3
  from your_package_name.greeters import FancyHelloWorld
  gr=FancyHelloWorld(person="Sampsa",age=40)
  print(gr)
    

