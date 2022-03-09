"""singleton.py : Global variables for the whole python program/library!

* Copyright: 2017 [copyright holder]
* Authors  : Sampsa Riikonen
* Date     : 2017
* Version  : 0.1

This file is part of the skeleton library

[copy-paste your license here]
"""

"""This parameter is None until some part of the program sets it
you'd do this typically at cli.py
"""
some_global_parameter = None

"""Don't abuse program-wide global parameters!  Set them only once at only once place (say, cli.py).
They're good for parameter sets / configs
"""

"""Better to use setters:
"""
def setSomeGlobalParameter(par):
    global some_global_parameter
    some_global_parameter = par
