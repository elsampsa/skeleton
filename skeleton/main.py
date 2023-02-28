"""
NAME.py : Description of the file

* Copyright: 2017 [copyright holder]
* Authors  : Sampsa Riikonen
* Date     : 2017
* Version  : 0.1

This file is part of the skeleton library

[copy-paste your license here]
"""
import logging, time, os, sys, signal
from skeleton.parset import MyParameterSet
from skeleton.greeters import BaseHelloWorld, FancyHelloWorld
from skeleton import singleton

def handle_exit(sig, frame):
    raise(SystemExit)

def app(my_parameter_set: MyParameterSet = None):
    signal.signal(signal.SIGTERM, handle_exit)
    assert my_parameter_set is not None, "needs my_parameter_set"
    p = my_parameter_set # shorthand
    print("got subpar:", p.main_par.sub_par)
    print("got parameter from singleton:", singleton.some_global_parameter)
    print("subobject from a list", p.main_par.a_list[1].subkey1)
    # change it
    p.main_par.sub_par = 456
    print("all pars:", p.toDict())
    b = BaseHelloWorld(person="me")
    f = FancyHelloWorld(person="you")
    print(b)
    print(f)
    while True:
        t=2
        try:
            print("sleeping for %s secs" % (t))
            time.sleep(t)
        except (KeyboardInterrupt, SystemExit):
            print("you pressed CTRL-C: will exit")
            break
    print("bye!")

def app2(cfg):
    # get stuff from cfg, i.e. from the .ini file
    user=cfg["DEFAULT"]["greeter_user"]
    b = BaseHelloWorld(person=user)
    f = FancyHelloWorld(person=user)
    print(b)
    print(f)
    while True:
        t=2
        try:
            print("sleeping for %s secs" % (t))
            time.sleep(t)
        except (KeyboardInterrupt, SystemExit):
            print("you pressed CTRL-C: will exit")
            break
    print("bye!")
