"""
tools.py : tool functions

* Copyright : 2017 Sampsa Riikonen
* Authors  : Sampsa Riikonen
* Date     : 2017
* Version  : 0.1

This file is part of the python skeleton example library

Skeleton example library is free software: you can redistribute it and/or modify it under the terms of the MIT License.  This code is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the MIT License for more details.
"""

import copy
import types


def objectCheck(obj, definitions):
  """ Checks that object has certain attributes, according to definitions
  
  :param obj:         Object to be checked
  :param definitions: Dictionary defining the parameters and their types
  
  An example definitions dictionary:
  
  |{
  |"age"     : int,         # must have attribute age that is an integer
  |"name"    : str,         # must have attribute name that is a string            
  | }
  """
  
  for key in definitions:
    required_type=definitions[key]
    attr=getattr(obj,key) # this raises an AttributeError of object is missing the attribute - but that is what we want
    # print("objectCheck:","got: ",attr,"of type",attr.__class__,"should be",required_type)
    if (attr.__class__ != required_type):
      raise(AttributeError("Wrong type of parameter "+key+" : should be "+required_type.__name__))
      return False # eh.. program quits anyway
    return True
    
  
def parameterInitCheck(definitions, parameters, obj):
  """ Checks that parameters are consistent with a definition
  
  :param definitions: Dictionary defining the parameters, their default values, etc.
  :param parameters:  Dictionary having the parameters to be checked
  :param obj:         Checked parameters are attached as attributes to this object
  
  An example definitions dictionary:
  
  |{
  |"age"     : (int,0),                 # parameter age defaults to 0 if not specified
  |"height"  : int,                     # parameter height **must** be defined by the user
  |"indexer" : some_module.Indexer,     # parameter indexer must of some user-defined class some_module.Indexer
  |"cleaner" : checkAttribute_cleaner,  # parameter cleaner is check by a custom function named "checkAttribute_cleaner" (that's been defined before)
  |"weird"   : None                     # parameter weird is passed without any checking - this means that your API is broken  :)
  | }
  
  """
  definitions=copy.copy(definitions)
  #print("parameterInitCheck: definitions=",definitions)
  for key in parameters:
    try:
      definition=definitions.pop(key) 
    except KeyError:
      raise AttributeError("Unknown parameter "+str(key))
      
    parameter =parameters[key]
    if (definition.__class__==tuple):   # a tuple defining (parameter_class, default value)
      #print("parameterInitCheck: tuple")
      required_type=definition[0]
      if (parameter.__class__!=required_type):
        raise(AttributeError("Wrong type of parameter "+key+" : should be "+required_type.__name__))
      else:
        setattr(obj,key,parameter)
    elif isinstance(definition, types.FunctionType):
      # object is checked by a custom function
      #print("parameterInitCheck: callable")
      ok=definition(parameter)
      if (ok):
        setattr(obj,key,parameter)
      else:
        raise(AttributeError("Checking of parameter "+key+" failed"))
    elif (definition==None):            # this is a generic object - no checking whatsoever
      #print("parameterInitCheck: None")
      setattr(obj,key,parameter)
    elif (definition.__class__==type):  # Check the type
      #print("parameterInitCheck: type")
      required_type=definition
      if (parameter.__class__!=required_type):
        raise(AttributeError("Wrong type of parameter "+key+" : should be "+required_type.__name__))
      else:
        setattr(obj,key,parameter)
    else:
      raise(AttributeError("Check your definitions syntax"))
      
  # in definitions, there might still some leftover parameters the user did not bother to give
  for key in definitions.keys():
    definition=definitions[key]
    if (definition.__class__==tuple):   # a tuple defining (parameter_class, default value)
        setattr(obj,key,definition[1])
    else:
      raise(AttributeError("Missing a mandatory parameter "+key))
    
    

def noCheck(obj):
  return True
