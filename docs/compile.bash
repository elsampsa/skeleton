#!/bin/bash
# sphinx-apidoc -f -e -o . ..
sphinx-autogen *.rst
#./fix_rst.py
#cd generated
#sphinx-autogen *.rst
#cd ..
make html
