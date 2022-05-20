#define NO_IMPORT_ARRAY // before all that stuff in skeleton_cpp_module.h
#include "skeleton_cpp_module.h"

using namespace std::this_thread;
using namespace std::chrono;

// generic error handling
#define handle_error(msg) \
    do { perror(msg); exit(EXIT_FAILURE); } while (0)

Test::Test() {
}

Test::~Test() {
}

void Test::callme() {
    std::cout << "hello from cpp" << std::endl;
}



TestNumpy::TestNumpy() {
}

TestNumpy::~TestNumpy() {
}

void TestNumpy::setZero(PyObject* pyobj) {
    // by default, the GIL is reserved while we're executing this method
    if (!pyobj) {
        std::cout << "NULL python object - testing from cpp maybe?" << std::endl;
        return;
    }
    Py_INCREF(pyobj);
    PyArrayObject* pa = (PyArrayObject*)pyobj;
    // get dimensions & size of each dimension
    int n_dims = PyArray_NDIM(pa);
    npy_intp *dims = PyArray_DIMS(pa);
    // byte buffer & it's size
    npy_intp n_bytes = PyArray_NBYTES(pa); // number of bytes consumed
    uint8_t* buf = (uint8_t*)PyArray_BYTES(pa); // pointer to byte data
    Py_BEGIN_ALLOW_THREADS; // use or not
    // danger zone: GIL is now released & you may 
    // manipulate the data area of the numpy array
    // while other python code is running
    // this might be a good idea or not (depending on your case)
    memset(buf, 0, n_bytes);
    Py_END_ALLOW_THREADS; // use or not
    Py_DECREF(pyobj);
}

PyObject* TestNumpy::doodle2D(PyObject* pyobj) {
    Py_INCREF(pyobj);
    // should check if numpy array, well..
    PyArrayObject* pa = (PyArrayObject*)pyobj;
    // check type
    int type_num = PyArray_TYPE(pa);
    if (type_num != NPY_DOUBLE) {
        std::cerr << "requires NPY_DOUBLE" << std::endl;
        Py_DECREF(pyobj);
        Py_RETURN_NONE;
    }
    // get dimensions & size of each dimension
    int n_dims = PyArray_NDIM(pa);
    if (n_dims != 2) {
        std::cerr << "dims must be exactly 2, you have " << n_dims << std::endl;
        Py_DECREF(pyobj);
        Py_RETURN_NONE;
    }
    npy_intp *dims = PyArray_DIMS(pa);
    int idim=dims[0];
    int jdim=dims[1];
    void* input_bytebuf = (void*)PyArray_BYTES(pa); // pointer to byte data
    
    // let's create the output 1D array
    npy_intp dims_[1];
    dims_[0]=dims[1]; // copy dim length from input x length
    /* // some numpy C-api functions are deprecated & removed, calling
    them can result in mysterious segfaults.  This is a fine example:
    int dims_[1];
    dims_[0]=int(dims[1]);
    out = (PyArrayObject*)PyArray_FromDims(1, dims_, NPY_DOUBLE);
    */
    PyArrayObject* out = (PyArrayObject*)PyArray_SimpleNew(1, &(dims_[0]), NPY_DOUBLE);
    void *output_bytebuf = (void*)PyArray_BYTES(out); // pointer to output byte data

    // create nice [i][j] indexing for the input & output arrays
    double* arr=(double*)(input_bytebuf);
    double* img[idim];
    double* line=(double*)(output_bytebuf);
    int i,j;
    for(i=0;i<idim;i++) {
        img[i]=&(arr[i*jdim]);
    }
    // now we can access img[i][j]
    Py_BEGIN_ALLOW_THREADS; // use or not
    for(i=0;i<idim;i++) {
        line[i]=0.;
        for(j=0;j<jdim;j++) {
            // std::cout << img[i][j] << std::endl;
            line[i]+=img[i][j];
        }
    }
    Py_END_ALLOW_THREADS; // use or not
    Py_DECREF(pyobj);
    return (PyObject*)out;
}



TestThread::TestThread(int thread_index) : thread_index(thread_index), 
    go_read(false), go_exit(false), pyobj(NULL), buf(NULL), bufsize(0) {
    // a non-blocking event file descriptor for interprocess communication:
    this->event_fd = eventfd(0, EFD_NONBLOCK); // https://linux.die.net/man/2/eventfd
    if (this->event_fd == -1) {
        handle_error("could not get eventfd");
    }
    int i=pthread_attr_init(&(this->thread_attr));
    if (i!=0) {handle_error("could not init thread attrs");}
    i=pthread_create(&(this->internal_thread), 
        &(this->thread_attr), 
        this->thread_func_, this);
    if (i!=0) {handle_error("could not create thread");}
}

TestThread::~TestThread() {
    {
        std::lock_guard<std::mutex> lk{m};
        go_read = true;
        go_exit = true;
        cond.notify_all();
    }
    void *res;
    int i=pthread_join(this->internal_thread, &res);
    if (i!=0) {handle_error("could not join thread");}
    free(res);
    i=pthread_attr_destroy(&(this->thread_attr));
    if (i!=0) {handle_error("could not remove thread attrs");}
    close(this->event_fd);
}


void* TestThread::thread_func_(void *p) {
    ((TestThread*)p)->thread_func();
    return NULL;
}


void TestThread::thread_func() { // TODO
    while(true) { // LOOP
    } // LOOP
}


int TestThread::getFd() {
    return this->event_fd;
}

void TestThread::put(PyObject* po) { // TODO
    Py_INCREF(po); // set as a member
    pyobj = po; // assume that this never goes off scope in the main python program
    // let the cpp thread read socket & hack directly the memspace of the numpy array
    {
        std::lock_guard<std::mutex> lk{m};
        go_read = true;
        cond.notify_all();
    }
}

PyObject* TestThread::load() { // TODO
    return NULL;
}

PyObject* TestThread::waitLoad() { // TODO
    return NULL;
}







