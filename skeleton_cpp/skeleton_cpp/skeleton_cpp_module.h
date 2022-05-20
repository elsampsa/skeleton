#ifndef skeleton_cpp_module_HEADER_GUARD
#define skeleton_cpp_module_HEADER_GUARD

#include <iostream>

// for multithreading
#include <mutex>
#include <thread>
#include <condition_variable>
#include <sys/eventfd.h>
#include <poll.h>
#include <sys/ioctl.h>

#define PY_ARRAY_UNIQUE_SYMBOL skeleton_cpp_module
#define NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION
#include "numpy/ndarraytypes.h"
#include "numpy/arrayobject.h"

// for Python C API
#include <Python.h>


/**
 * @brief Just call some c++ **it from python
 * 
 */
class Test {

public:
    Test();
    virtual ~Test();

public:
    void callme();
};


/**
 * @brief Examples of passing numpy array to C++ side
 * 
 */
class TestNumpy {

public:
    TestNumpy();
    virtual ~TestNumpy();

public:
    void setZero(PyObject* pyobj); ///< simply set a numpy array to zero
    PyObject* doodle2D(PyObject* pyobj); ///< take in 2D array, access its elements, return 1D array
};

/**
 * @brief Do some **it with a separate thread at the c++ side, 
 * give notice when **it is ready to be read at python side.
 * The thread is running continuously in the background during the
 * object's lifetime
 * WARNING: this is work-in-progress, not ready yet
 */
class TestThread {

public:
    TestThread(int thread_index=-1);
    virtual ~TestThread();

private:
    int event_fd;
    int thread_index;
    pthread_attr_t thread_attr; ///< Thread attributes, pthread_* way
    cpu_set_t cpuset;
    pthread_t internal_thread;

private:
    static void *thread_func_(void *p);
    void thread_func();

private: // mutex-protected vars
    std::mutex m;
    std::condition_variable cond;
    bool go_read;
    bool go_exit;

protected:
    PyObject* pyobj;
    uint8_t* buf;
    std::size_t bufsize;

public:
    int getFd(); ///< Get the notifying eventfd
    void put(PyObject* po); ///< Give some **it (numpy array) for manipulation
    PyObject* load(); ///< returns the manipulated numpy array
    PyObject* waitLoad(); ///< like load, but waits first for the event_fd to fire
};

#endif

