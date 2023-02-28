#!/bin/bash
rm -r -f venv
# virtualenv --no-site-packages -p python3 venv
virtualenv -p python3 venv
echo
echo "> Do this"
echo "source venv/bin/activate"
echo "export PYTHONPATH="
echo "> To test the package, use"
echo "pip3 install skeleton/dist/skeleton-0.1.0.tar.gz"
echo "> To exit, type"
echo "deactivate"
echo
