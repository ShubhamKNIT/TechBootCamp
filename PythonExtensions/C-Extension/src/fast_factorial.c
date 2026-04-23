#include <Python.h>
#define PY_SSIZE_T_CLEAN


static unsigned long long c_factorial(unsigned int n) {
    unsigned long long r = 1;

    for (unsigned int i = 1; i <= n; i++) {
        r *= i;
    }

    return r;
}


static PyObject* py_factorial_repeat_with_GIL(PyObject* self, PyObject* args) {
    unsigned int n;
    unsigned int reps;

    if (!PyArg_ParseTuple(args, "IK", &n, &reps)) {
        return NULL; // Return NULL if argument parsing fails
    }

    unsigned long long last = 0;

    for (unsigned long long i = 0; i < reps; i++) {
        last = c_factorial(n);
    }

    return PyLong_FromUnsignedLongLong(last);
}


static PyObject* py_factorial_repeat_without_GIL(PyObject* self, PyObject* args) {
    unsigned int n;
    unsigned int reps;

    if (!PyArg_ParseTuple(args, "IK", &n, &reps)) {
        return NULL; // Return NULL if argument parsing fails
    }

    unsigned long long last = 0;

    Py_BEGIN_ALLOW_THREADS // Releases the GIL
    for (unsigned long long i = 0; i < reps; i++) {
        last = c_factorial(n);
    }
    Py_END_ALLOW_THREADS // Reacquires the GIL

    return PyLong_FromUnsignedLongLong(last);
}

static PyMethodDef FastFactMethods[] = {
    {
        "factorial_with_GIL",
        py_factorial_repeat_with_GIL,
        METH_VARARGS,
        "Calculate factorial of n, repeated reps times, with GIL held."
    },
    {
        "factorial_without_GIL",
        py_factorial_repeat_without_GIL,
        METH_VARARGS,
        "Calculate factorial of n, repeated reps times, without holding the GIL."
    },
    {
        NULL,
        NULL,
        -1,
        NULL
    }
};

static struct PyModuleDef fastFactorialModule = {
    PyModuleDef_HEAD_INIT,
    "fast_factorial_module", // name of module
    "A module that provides fast factorial calculations with and without GIL.", // module documentation
    -1, // size of per-interpreter state of the module, or -1 if the module keeps state in global variables
    FastFactMethods // methods defined in this module
};

PyMODINIT_FUNC 
PyInit_fast_factorial_module(void) {
    return PyModule_Create(&fastFactorialModule);
}