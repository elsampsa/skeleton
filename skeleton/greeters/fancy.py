"""fancy.py : A fancier greeter class

* Copyright : 2017 Sampsa Riikonen
* Authors  : Sampsa Riikonen
* Date     : 2017
* Version  : 0.1

This file is part of the python skeleton example library

Skeleton example library is free software: you can redistribute it and/or modify it under the terms of the MIT License.  This code is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the MIT License for more details.
"""
import logging
# inside the module please use absolute paths:
from skeleton.greeters.base import BaseHelloWorld
import sys


class FancyHelloWorld(BaseHelloWorld):
    """Like BaseHelloWorld, but prints a nice banner! :)

    Takes just a single argument (inherited from the base class)

    :param person: person's name: string, mandatory
    """
    def __str__(self):
        st = "**************\n"
        st += super().__str__() + "\n"
        st += "**************\n"
        return st


def test1():
    """Test FancyHelloWorld
    """
    print(__name__, "test1")
    # when running normally the program, the loglevels are set through a yaml file
    logger = logging.getLogger("FancyHelloWorld")
    logger.setLevel(logging.DEBUG)
    fancy = FancyHelloWorld(person="me")
    print(fancy)


def main():
    import sys
    if (len(sys.argv) < 2):
        print("main: needs test number")
    else:
        st = "test" + str(sys.argv[1]) + "()"
        exec(st)


if (__name__ == "__main__"):
    main()

