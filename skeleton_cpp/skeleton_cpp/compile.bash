#!/bin/bash
numpy_cflags="-I"$(python3 -c "import numpy; print(numpy.get_include(), end='')")
name="skeleton_cpp_module"
cname=$name".cpp"
hname=$name".h"
oname=$name".o"
pyname=$name".py"
libname="_"$name".so"
wrapname=$name"_wrap.cpp"
intname=$name".i"
#
rm -f $wrapname $pyname $libname *.o
swig -python -c++ -o $wrapname $intname
cflags=$(python3-config --cflags)
lflags=$(python3-config --embed --ldflags)
# objects
echo
echo "COMPILING OBJECTS"
echo
set -x
g++ -std=c++11 $cflags $numpy_cflags -fPIC $cname -o $oname -c
g++ -std=c++11 $cflags $numpy_cflags -fPIC main.cpp -o main.o -c
set +x
# shared lib for python
echo
echo "SHARED LIBRARY LINK"
echo
set -x
g++ -std=c++11 $cflags $numpy_cflags $lflags -fPIC -shared $wrapname $oname -o $libname
set +x
# test executable
echo
echo "TEST EXECUTABLE LINK"
echo
set -x
g++ -std=c++11 $cflags $numpy_cflags $oname main.o $lflags -o test
set +x
