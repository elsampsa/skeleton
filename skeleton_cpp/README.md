# Package or a module

This directory can be installed either as a python package, having the single module ``skeleton_cpp`` in [skeleton_cpp/](skeleton_cpp/)
or as a second module ``skeleton_cpp`` for the ``skeleton`` package in the upper [level directory](../).

# A small cpp extension here

When you run ``pip3 install`` in the upper-level directory, the cpp extension is compiled automagically & placed into the correct place, 
whatever your scheme is (local install with ``-e``, creating a package, etc).

For separate debugging / testing, in this directory you can use
```
compile.bash
```
to test that the cpp build process works.  It also creates executable ``test`` that you might want to run with valgrind.

Please do read more about importing the numpy array api in [here](https://numpy.org/doc/1.16/reference/c-api.array.html#importing-the-api).

Numpy API reference [here](https://numpy.org/doc/stable/reference/c-api/index.html).

For a more ambitious / robust c++ library interfaced to python I recommend you to take a look into the main level ``skeleton_cpp_module/`` directory.  TODO

# Using the cpp extension

The python API is basically the ``.h`` header file you find in this directory.

Take a look into [../notebook/example.ipynb](../notebook/example.ipynb) on how to use it. TODO

# Numpy API Doodle

Some random notes about the numpy API.  Please look at the ``.cpp`` file in this directory for practical examples.
```
pa = (PyArrayObject*)pyobj;
// get dimensions & size of each dimension
int n_dims = PyArray_NDIM(pa);
npy_intp *dims = PyArray_DIMS(pa);
// byte buffer & it's size
npy_intp n_bytes = PyArray_NBYTES(pa); // number of bytes consumed
input_bytebuf = (uint8_t*)PyArray_BYTES(pa); // pointer to byte data
int type_num = PyArray_TYPE(pa);
std::cerr << "type_num:" << type_num << std::endl;
PyArray_Descr* dtype;
```

``PyArray_DIMS``, ``PyArray_NBYTES``, etc. macros hook up into the different members of the ``PyArrayObject`` data structure:
```
typedef struct PyArrayObject {
    PyObject_HEAD
    char *data;
    int nd;
    npy_intp *dimensions;
    npy_intp *strides;
    PyObject *base;
    PyArray_Descr *descr;
    int flags;
    PyObject *weakreflist;
    /* version dependent private members */
} PyArrayObject;
```
``PyArray_TYPE`` hooks into ``PyArray_Descr *descr;`` member (?):
```
typedef struct {
    PyObject_HEAD
    PyTypeObject *typeobj;
    char kind;
    char type;
    char byteorder;
    char flags;
    int type_num;
    int elsize;
    int alignment;
    PyArray_ArrayDescr *subarray;
    PyObject *fields;
    PyObject *names;
    PyArray_ArrFuncs *f;
    PyObject *metadata;
    NpyAuxData *c_metadata;
    npy_hash_t hash;
} PyArray_Descr;
```


```
/usr/lib/python3/dist-packages/numpy/core/include/numpy/npy_common.h:
...
typedef double npy_double;
...
#define NPY_FLOAT64 NPY_DOUBLE
...
```

```
/usr/lib/python3/dist-packages/numpy/core/include/numpy/ndarraytypes.h
...
enum NPY_TYPES {    NPY_BOOL=0,
                    NPY_BYTE, NPY_UBYTE,
                    NPY_SHORT, NPY_USHORT,
                    NPY_INT, NPY_UINT,
                    NPY_LONG, NPY_ULONG, # 7,8
                    NPY_LONGLONG, NPY_ULONGLONG,
                    NPY_FLOAT, NPY_DOUBLE, NPY_LONGDOUBLE, # 11, 12
                    NPY_CFLOAT, NPY_CDOUBLE, NPY_CLONGDOUBLE,
                    NPY_OBJECT=17,
                    NPY_STRING, NPY_UNICODE,
                    NPY_VOID,
...
```
