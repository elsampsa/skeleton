"""
NAME.py : Description of the file

* Copyright: 2017 [copyright holder]
* Authors  : Sampsa Riikonen
* Date     : 2017
* Version  : 0.1

This file is part of the skeleton library

[copy-paste your license here]
"""
import logging
from skeleton.parset import MyParameterSet
from skeleton.greeters import BaseHelloWorld, FancyHelloWorld

def app(my_parameter_set: MyParameterSet = None):
    assert(my_parameter_set is not None), "needs my_parameter_set"
    p = my_parameter_set # shorthand
    print("got subpar:", p.config.main_par.sub_par)
    # change it
    p.config.main_par.sub_par = 456
    print("all pars:", p.toDict())
    b = BaseHelloWorld(person="me")
    f = FancyHelloWorld(person="you")
    print(b, "\n", f)
