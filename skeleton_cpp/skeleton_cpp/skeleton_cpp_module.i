// %module skeleton_cpp_module
// http://swig.org/Doc4.0/Python.html#Python_nn72
// https://github.com/swig/swig/issues/1831
%module(moduleimport="import _skeleton_cpp_module") skeleton_cpp_module
%include <std_string.i>
%{ // this is prepended in the wapper-generated c(pp) file

#define SWIG_FILE_WITH_INIT
#include <Python.h>
#include "skeleton_cpp_module.h"

#define NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION
#include "numpy/ndarraytypes.h"
#include "numpy/arrayobject.h"

%}

%init %{

import_array(); // numpy initialization that should be run only once

%}

%inline %{

%}

// next, expose what is necessary
%include "skeleton_cpp_module.h" // autogenerate
