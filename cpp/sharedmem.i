%module sharedmem
%include <std_string.i>
%{ // this is prepended in the wapper-generated c(pp) file

#define SWIG_FILE_WITH_INIT
#include <Python.h>
#include "sharedmem.h"

#define NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION
//#define PY_ARRAY_UNIQUE_SYMBOL shmem_array_api
#include "numpy/ndarraytypes.h"
#include "numpy/arrayobject.h"

%}

%init %{

import_array(); // numpy initialization that should be run only once

%}

%inline %{

%}

// next, expose what is necessary
// autogenerate from this point on
%include "sharedmem.h"
