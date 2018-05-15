"""
fancy.py : fancier greeter classes.  This demonstrates how to build APIs that check input parameters.

* Copyright : 2017 Sampsa Riikonen
* Authors  : Sampsa Riikonen
* Date     : 2017
* Version  : 0.1

This file is part of the python skeleton example library

Skeleton example library is free software: you can redistribute it and/or modify it under the terms of the MIT License.  This code is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the MIT License for more details.
"""
__all__=["FancyHelloWorld","FancyHelloWorld2","FancyHelloWorld3","FancyHelloWorld4","FancyHelloWorld5"] # this declares what is exposed for the API user in the "from skeleton import .." namespace

import sys
from skeleton.tools import getDataFile, typeCheck, dictionaryCheck, objectCheck, parameterInitCheck, noCheck, is_py3
from skeleton.greeters.base import BaseHelloWorld # it's good to use the absolute paths here (API user could use simply "from skeleton.greeters import BaseHelloWorld")
pre_mod = "skeleton.greeters.fancy : " # a string for aux debuggin purposes


class FancyHelloWorld(BaseHelloWorld):
  """Like BaseHelloWorld, but prints a nice banner! :)
  
  Takes just a single argument (inherited from the base class)
  
  :param person: person's name: string, mandatory
  """
  def __init__(self, **kwargs):
    # if you need to call the superclass constructor:
    # super().__init__(**kwargs) # python3
    # super(FancyHelloWorld, self).__init__(**kwargs) # python2 compatible
    
    self.pre=self.__class__.__name__+" : " # auxiliary string for debugging output
    parameterInitCheck(self.parameter_defs,kwargs,self) # check kwargs agains parameter_defs, attach ok'd parameters to this object as attributes
    # print(self.pre,"__init__","leaving constructor") # auxiliary debug string
        
    
  def __str__(self):
    st ="**************\n"
    st+=super(FancyHelloWorld, self).__str__()+"\n" # python2 compatible
    st+="**************\n"
    return st



class FancyHelloWorld2(BaseHelloWorld):
  """An example of how to make an API.  Initialization done using kwargs.  Inherited from :class:`~skeleton.greeters.base.BaseHelloWorld`
  
  API checks for input types
  
  :param person: person's name : string, mandatory
  :param address: person's name : string, optional, default value = "nothing"
  :param age: person's age : integer, optional, default value = 0
  
  """
  parameter_defs={
    "person"   : str,                  # :param person: person's name : string, mandatory
    "address"  : (str,"nothing"),      # :param address: person's name : string, optional, default value = "nothing"
    "age"      : (int,0)               # :param age: person's age : integer, optional, default value = 0
    }
  
  
  def __init__(self, **kwargs):
    self.pre=self.__class__.__name__+" : " # auxiliary string for debugging output
    parameterInitCheck(self.parameter_defs,kwargs,self) # check for input parameters
    
    
  def __str__(self): # an example how to print all defined attributes
    st ="**************\n"
    for parameter in self.parameter_defs:
      st+=parameter+ ": "+str(getattr(self,parameter))+"\n"
    st+="**************\n"
    return st
  
  
  def doSomethingFancy(self,par):
    """This is simply a method that does something fancy with a parameter
    
    Parameter could be checked using parameterInitCheck, like in the constructor
    
    :param par: Parameter to do something fancy with
    
    As for documentation, everything goes here as well: here is a link to :ref:`the introduction <about>`.
    
    """
    pass


  def doSomethingFancyAsWell(self):
    """This method also does something fancy
    """
    pass



class FancyHelloWorld3(FancyHelloWorld):
  """An example of how to make an API.  Initialization done using kwargs.  Inherited from :class:`~skeleton.greeters.base.BaseHelloWorld`
  
  API checks for input types: here we have a complex object type as an input parameter
  
  :param person: person's name : string, mandatory
  :param address: person's name : string, optional, default value = "nothing"
  :param age: person's age : integer, optional, default value = 0
  :param subgreeter: an object of the type :class:`~skeleton.greeters.fancy.FancyHelloWorld`
  
  """
  parameter_defs={
    "person"     : str,             # :param person: person's name : string, mandatory
    "address"    : (str,"nothing"), # :param address: person's name : string, optional, default value = "nothing"
    "age"        : (int,0),         # :param age: person's age : integer, optional, default value = 0
    "subgreeter" : FancyHelloWorld  # :param subgreeter: an object of the type :class:`~skeleton.greeters.fancy.FancyHelloWorld`
    }
  
  
  def __init__(self, **kwargs):
    self.pre=self.__class__.__name__+" : " # auxiliary string for debugging output
    parameterInitCheck(self.parameter_defs,kwargs,self) # check for input parameters



class FancyHelloWorld4(FancyHelloWorld):
  """An example of how to make an API.  Initialization done using kwargs.  Inherited from :class:`~skeleton.greeters.base.BaseHelloWorld`
  
  API checks for input types: one of the input parameters is undefined .. we simply check that is has certain attributes.  This would be a "tedious API". .. usefull if the input class is not yet fully fixed
  
  :param person: person's name : string, mandatory
  :param address: person's name : string, optional, default value = "nothing"
  :param age: person's age : integer, optional, default value = 0
  :param vague: an object of unspecified type.  Custom checked with AttributeCheck_vague (see source code for more details)
  """
  
  def AttributeCheck_vague(obj):
    """Checks that the object has
    
    :param person: (string)
    :param age: (int)
    """
    return objectCheck(
      { # check that object has these parameters
      "person"  : str,
      "age"     : int,
      },obj)
      # we could do any sort of custom checks here.  Remember to return False or True
      
  
  parameter_defs={
    "person"     : str,                                    # :param person: person's name : string, mandatory
    "address"    : (str,"nothing"),                        # :param address: person's name : string, optional, default value = "nothing"
    "age"        : (int,0),                                # :param age: person's age : integer, optional, default value = 0
    "vague"      : AttributeCheck_vague                    # :param vague: an object of unspecified type.  Custom checked wit AttributeCheck_vague (see source code for more details)
    }
  
  
  def __init__(self, **kwargs):
    self.pre=self.__class__.__name__+" : " # auxiliary string for debugging output
    parameterInitCheck(self.parameter_defs,kwargs,self) # check for input parameters



class FancyHelloWorld5(FancyHelloWorld):
  """An example of how to make an API.  Initialization done using kwargs.  Inherited from :class:`~skeleton.greeters.base.BaseHelloWorld`
  
  API checks for input types: one of the input parameters is left completely undefined .. This is an API that has been left intentionally broken
  
  :param person: person's name : string, mandatory
  :param address: person's name : string, optional, default value = "nothing"
  :param age: person's age : integer, optional, default value = 0
  :param vague: an object of unspecified type. Congrats, your API is broken!  :)
  """
  
  parameter_defs={
    "person"     : str,                                    # :param person: person's name : string, mandatory
    "address"    : (str,"nothing"),                        # :param address: person's name : string, optional, default value = "nothing"
    "age"        : (int,0),                                # :param age: person's age : integer, optional, default value = 0
    "vague"      : noCheck                                 # :param vague: an object of unspecified type. The "checking" is done with a function that returns always True (=everything goes)
    }
  
  
  def __init__(self, **kwargs):
    self.pre=self.__class__.__name__+" : " # auxiliary string for debugging output
    parameterInitCheck(self.parameter_defs,kwargs,self) # check for input parameters



    
def test1():
  """ Test FancyHelloWorld2
  """
  pre=pre_mod+"test1 :"
  
  print(pre,"test1")
  print(pre,"Let's test FancyHelloWorlds")
  
  print(pre,"FancyHelloWorld")
  try:
    hw=FancyHelloWorld(address="Helsinki",age=40)
  except AttributeError as e:
    print(e)
  else:
    print(hw)
  try:
    hw=FancyHelloWorld(person="Sampsa",address="Helsinki",age="40")
  except AttributeError as e:
    print(e)
  else:
    print(hw)
  try:
    hw=FancyHelloWorld(person="Sampsa")
  except AttributeError as e:
    print(e)
  else:
    print(hw)
  
    
  print(pre,"FancyHelloWorld2")
  try:
    hw2=FancyHelloWorld2(address="Helsinki",age=40)
  except AttributeError as e:
    print(e)
  else:
    print(hw)
  try:
    hw2=FancyHelloWorld2(person="Sampsa",address="Helsinki",age="40")
  except AttributeError as e:
    print(e)
  else:
    print(hw)
  try:
    hw2=FancyHelloWorld2(person="Sampsa",address="Helsinki",age=40)
  except AttributeError as e:
    print(e)
  else:
    print(hw)
  
  
  print(pre,"FancyHelloWorld3")
  try:
    hw3=FancyHelloWorld3(person="Sampsa",subgreeter="x")
  except AttributeError as e:
    print(e)
  else:
    print(hw)
  try:
    hw3=FancyHelloWorld3(person="Sampsa",subgreeter=hw)
  except AttributeError as e:
    print(e)
  else:
    print(hw)
  
  
  print(pre,"FancyHelloWorld4")
  class NameSpace: # test object
    def __init__(self):
      self.person="sampsa"
      self.age   ="40" # wrong attribute
  
  try:
    hw4=FancyHelloWorld4(person="me",vague=NameSpace())
  except AttributeError as e:
    print(e)
  else:
    print(hw)
  
  class NameSpace: # test object
    def __init__(self):
      self.person="sampsa" # correct attributes
      self.age   =40
  
  try:
    hw4=FancyHelloWorld4(person="me",vague=NameSpace())
  except AttributeError as e:
    print(e)
  else:
    print(hw)
  
  print(pre,"FancyHelloWorld5")
  try:
    hw5=FancyHelloWorld5(person="me",vague=None)
  except AttributeError as e:
    print(e)
  else:
    print(hw)
  


# this rest is just broilerplate .. copy it to your new module ! :)
def test2():
  """ Test broilerplate
  """
  pre=pre_mod+"test2 :"
  print(pre,"test2")
  print(pre,"description of test 2")

    
def main():
  import sys
  pre=pre_mod+"main :"
  print(pre,"main: arguments: ",sys.argv)
  if (len(sys.argv)<2):
    print(pre,"main: needs test number")
  else:
    st="test"+str(sys.argv[1])+"()"
    exec(st)
  
  
if (__name__=="__main__"):
  main()

