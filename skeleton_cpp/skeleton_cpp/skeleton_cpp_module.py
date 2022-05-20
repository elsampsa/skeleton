# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.1
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

import _skeleton_cpp_module

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)


def _swig_setattr_nondynamic_instance_variable(set):
    def set_instance_attr(self, name, value):
        if name == "thisown":
            self.this.own(value)
        elif name == "this":
            set(self, name, value)
        elif hasattr(self, name) and isinstance(getattr(type(self), name), property):
            set(self, name, value)
        else:
            raise AttributeError("You cannot add instance attributes to %s" % self)
    return set_instance_attr


def _swig_setattr_nondynamic_class_variable(set):
    def set_class_attr(cls, name, value):
        if hasattr(cls, name) and not isinstance(getattr(cls, name), property):
            set(cls, name, value)
        else:
            raise AttributeError("You cannot add class attributes to %s" % cls)
    return set_class_attr


def _swig_add_metaclass(metaclass):
    """Class decorator for adding a metaclass to a SWIG wrapped class - a slimmed down version of six.add_metaclass"""
    def wrapper(cls):
        return metaclass(cls.__name__, cls.__bases__, cls.__dict__.copy())
    return wrapper


class _SwigNonDynamicMeta(type):
    """Meta class to enforce nondynamic attributes (no new attributes) for a class"""
    __setattr__ = _swig_setattr_nondynamic_class_variable(type.__setattr__)


class Test(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self):
        _skeleton_cpp_module.Test_swiginit(self, _skeleton_cpp_module.new_Test())
    __swig_destroy__ = _skeleton_cpp_module.delete_Test

    def callme(self):
        return _skeleton_cpp_module.Test_callme(self)

# Register Test in _skeleton_cpp_module:
_skeleton_cpp_module.Test_swigregister(Test)

class TestNumpy(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self):
        _skeleton_cpp_module.TestNumpy_swiginit(self, _skeleton_cpp_module.new_TestNumpy())
    __swig_destroy__ = _skeleton_cpp_module.delete_TestNumpy

    def setZero(self, pyobj):
        return _skeleton_cpp_module.TestNumpy_setZero(self, pyobj)

    def doodle2D(self, pyobj):
        return _skeleton_cpp_module.TestNumpy_doodle2D(self, pyobj)

# Register TestNumpy in _skeleton_cpp_module:
_skeleton_cpp_module.TestNumpy_swigregister(TestNumpy)

class TestThread(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, thread_index=-1):
        _skeleton_cpp_module.TestThread_swiginit(self, _skeleton_cpp_module.new_TestThread(thread_index))
    __swig_destroy__ = _skeleton_cpp_module.delete_TestThread

    def getFd(self):
        return _skeleton_cpp_module.TestThread_getFd(self)

    def put(self, po):
        return _skeleton_cpp_module.TestThread_put(self, po)

    def load(self):
        return _skeleton_cpp_module.TestThread_load(self)

    def waitLoad(self):
        return _skeleton_cpp_module.TestThread_waitLoad(self)

# Register TestThread in _skeleton_cpp_module:
_skeleton_cpp_module.TestThread_swigregister(TestThread)



