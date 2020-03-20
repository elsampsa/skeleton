"""
base.py : Greeter base classes

* Copyright : 2017 Sampsa Riikonen
* Authors  : Sampsa Riikonen
* Date     : 2017
* Version  : 0.1

This file is part of the python skeleton example library

Skeleton example library is free software: you can redistribute it and/or modify it under the terms of the MIT License.  This code is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the MIT License for more details.
"""
import sys
from skeleton.tools import getDataFile, typeCheck, dictionaryCheck, objectCheck, parameterInitCheck, noCheck, is_py3
import logging


# If I remember correctly, in python3 all classes are automatically
# children of object
class BaseHelloWorld(object):
    """ A Greeter base class

    :param person: person's name: string, mandatory
    """

    parameter_defs = {
        "person": str  # a parameter "person" of the type string is required
    }

    def __init__(self, **kwargs):
        self.pre = self.__class__.__name__  # auxiliary string for debugging output
        # print(self.pre,"__init__ : parameter_defs : ",self.parameter_defs)
        # check kwargs agains parameter_defs, attach ok'd parameters to this
        # object as attributes
        parameterInitCheck(self.parameter_defs, kwargs, self)
        self.logger = getLogger(self.pre)  # hierarchical logger
        self.logger.debug("__init__ : hello")

    def __str__(self):
        st = "Hello from " + self.person
        return st


def test1():
    """Test BaseHelloWorld
    """
    pre = __name__ + "test1 :"
    print(pre, "test1")
    print(pre, "description of test 1")

    try:
        base = BaseHelloWorld()  # no person defined
    except AttributeError as e:
        print(e)
    else:
        print(base)
    try:
        base = BaseHelloWorld(person=1)  # wrong type for person
    except AttributeError as e:
        print(e)
    else:
        print(base)
    try:
        base = BaseHelloWorld(person="sampsa", age=10)  # unknown argument age
    except AttributeError as e:
        print(e)
    else:
        print(base)
    try:
        base = BaseHelloWorld(person="sampsa")  # success
    except AttributeError as e:
        print(e)
    else:
        print(base)


def test2():
    """Empty test
    """
    pre = pre_mod + "test2 :"
    print(pre, "test2")
    print(pre, "description of test 2")


def main():
    import sys
    pre = pre_mod + "main :"
    print(pre, "main: arguments: ", sys.argv)
    if (len(sys.argv) < 2):
        print(pre, "main: needs test number")
    else:
        st = "test" + str(sys.argv[1]) + "()"
        exec(st)


if (__name__ == "__main__"):
    main()
