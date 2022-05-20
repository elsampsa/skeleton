#include "skeleton_cpp_module.h"
#include <vector>

#define NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION
#include "numpy/ndarraytypes.h"
#include "numpy/arrayobject.h"


using namespace std::this_thread;
using namespace std::chrono;


/*for pure-cpp debugging it's a good idea to run valgrind:

sudo apt-get install valgrind
valgrind ./test

*/
int main(int argc, char **argcv) {
    /* // if you need to
    Py_Initialize();
    import_array();
    */

    Test t;
    t.callme();

    TestNumpy tn;
    tn.setZero(NULL);
}
