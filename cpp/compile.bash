#!/bin/bash
tmp=" $( pkg-config --cflags --libs python3 ) "
g++ -std=c++11 -fPIC sharedmem.cpp -o sharedmem.o -c
g++ -std=c++11 $tmp -fPIC -shared sharedmem_wrap.cpp sharedmem.o -o _sharedmem.so
