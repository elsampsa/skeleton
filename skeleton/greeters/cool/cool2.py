# it's good to use the absolute paths here (API user could use simply
# "from my_test_package.greeters import BaseHelloWorld")
from my_test_package.greeters.base import BaseHelloWorld
from my_test_package.tools import getDataFile, typeCheck, dictionaryCheck, objectCheck, parameterInitCheck, noCheck, is_py3
import sys
"""
cool2.py : cooler greeter classes, part 2.

* Copyright : 2017 Sampsa Riikonen
* Authors  : Sampsa Riikonen
* Date     : 2017
* Version  : 0.1

This file is part of the python my_test_package example library

Skeleton example library is free software: you can redistribute it and/or modify it under the terms of the MIT License.  This code is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the MIT License for more details.
"""
__all__ = ["Cool2HelloWorld"]

pre_mod = "my_test_package.greeters.cool1 : "  # a string for aux debuggin purposes


class Cool2HelloWorld(BaseHelloWorld):
    """Like BaseHelloWorld, but prints a nice banner! :)

    Takes just a single argument (inherited from the base class)

    :param person: person's name: string, mandatory
    """

    def __init__(self, **kwargs):
        # if you need to call the superclass constructor:
        # super().__init__(**kwargs) # python3
        # super(FancyHelloWorld, self).__init__(**kwargs) # python2 compatible

        # auxiliary string for debugging output
        self.pre = self.__class__.__name__ + " : "
        # check kwargs agains parameter_defs, attach ok'd parameters to this
        # object as attributes
        parameterInitCheck(self.parameter_defs, kwargs, self) # this a bit too fancy.. avoid
        # print(self.pre,"__init__","leaving constructor") # auxiliary debug
        # string

    def __str__(self):
        st = "**************\n"
        st += super().__str__() + \
            "\n"  # python2 compatible
        st += "**************\n"
        return st


    def someMethod(self):
        print("hello from someMethod")


# this rest is just broilerplate .. copy it to your new module ! :)
def test1():
    """ Test broilerplate
    """
    pre = pre_mod + "test1 :"
    print(pre, "test1")
    print(pre, "description of test 1")


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
