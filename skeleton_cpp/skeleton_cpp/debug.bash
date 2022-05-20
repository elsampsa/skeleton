#!/bin/bash
## https://www.podoliaka.org/2016/04/10/debugging-cpython-gdb/
## remember to:
# sudo apt-get install gdb python3-dbg
##
gdb --args python3 pytest.py
