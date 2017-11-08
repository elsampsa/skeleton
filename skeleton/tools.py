"""
tools.py : tool functions

* Copyright : 2017 Sampsa Riikonen
* Authors  : Sampsa Riikonen
* Date     : 2017
* Version  : 0.1

This file is part of the python skeleton example library

Skeleton example library is free software: you can redistribute it and/or modify it under the terms of the MIT License.  This code is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the MIT License for more details.
"""


def parameterCheck(obj):
  """ Parameter checker for a class that has the following members:
  
  parameters : list of pairs, e.g. [ ["parameter_name",parameter_type], ["parameter_name",parameter_type], .. ]
  pre        : a string
  
  """
  for parameter in obj.parameters:
    par=getattr(obj,parameter[0])
    if (par.__class__!=parameter[1]):
      print(obj.pre,"FATAL: wrong parameter type for",parameter[0],":",par.__class__.__name__," - should be of type",parameter[1].__name__)
      raise AttributeError
  
  
def parameterInit(obj, kwargs):
  """ Parameter checker/initiator
  
  :param kwargs: dictionary object of input parameters for the class
  
  obj class must have the following members:
  
  parameters : list of lists, e.g. [ ["person", None,      str], ["address","nothing", str], ["age",    0,         int] ].  None indicates that a value must be in kwargs
  pre        : a string
  
  """
  for parameter in obj.parameters:
    par=kwargs.pop(parameter[0],parameter[1]) # take value of key parameter[0] (i.e. "person", "address", ..), if no such key, default to parameter[1], i.e. the default value
    if (par==None): 
      print(obj.pre,"FATAL: needs parameter",parameter[0])
      raise AttributeError
    elif (par.__class__!=parameter[2]):
      print(obj.pre,"FATAL: wrong parameter type for",parameter[0],":",par.__class__.__name__," - should be of type",parameter[2].__name__)
      raise AttributeError
    else:
      setattr(obj,parameter[0],par) # now the parameter is accessible with instance_name.parameter_name


 
