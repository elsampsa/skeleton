"""base.py : A Greeter base class

* Copyright : 2017 Sampsa Riikonen
* Authors  : Sampsa Riikonen
* Date     : 2017
* Version  : 0.1

This file is part of the python skeleton example library

Skeleton example library is free software: you can redistribute it and/or modify it under the terms of the MIT License.  This code is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the MIT License for more details.
"""
import sys
import logging


class BaseHelloWorld:
    """ A Greeter base class

    :param person: person's name: string, mandatory
    """
    def __init__(self, person):
        self.logger = logging.getLogger(self.__class__.__name__)
        self.person = person
        self.logger.info("info level msg from __init__")
        self.logger.debug("debug level msg from __init__")

    def __str__(self):
        st = "Hello from " + self.person
        return st


def test1():
    """Test BaseHelloWorld
    """
    print(__name__, "test1")
    # when running normally the program, the loglevels are set through a yaml file
    logger = logging.getLogger("BaseHelloWorld")
    logger.setLevel(logging.DEBUG)
    base = BaseHelloWorld(person="me")
    print(base)


def main():
    import sys
    if (len(sys.argv) < 2):
        print("main: needs test number")
    else:
        st = "test" + str(sys.argv[1]) + "()"
        exec(st)


if (__name__ == "__main__"):
    main()

