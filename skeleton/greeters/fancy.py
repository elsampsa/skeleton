"""
fancy.py : fancier greeter classes

* Copyright : 2017 Sampsa Riikonen
* Authors  : Sampsa Riikonen
* Date     : 2017
* Version  : 0.1

This file is part of the python skeleton example library

Skeleton example library is free software: you can redistribute it and/or modify it under the terms of the MIT License.  This code is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the MIT License for more details.
"""

import sys
pre_mod = "skeleton.greeters.fancy : " # a string for aux debuggin purposes

from skeleton.tools import parameterCheck, parameterInit
from skeleton.greeters.base import BaseHelloWorld # it's good to use the absolute paths here (API user could use simply "from skeleton.greeters import BaseHelloWorld")



class FancyHelloWorld(BaseHelloWorld):
  """Like BaseHelloWorld, but prints a nice banner! :)
  
  :param person: String identifying the person
  """
  parameters=[
    ["person", str],  # parameter key, type
    ]
  
  
  def __init__(self, person):
    # if you need to call the superclass constructor:
    # super().__init__(person) # python3
    # super(FancyHelloWorld, self).__init__(person) # python2 compatible
    
    self.pre=self.__class__.__name__+" : " # auxiliary string for debugging output
    self.person=person
    # print(self.pre,"__init__","leaving constructor") # auxiliary debug string
    parameterCheck(self)
        
    
  def __str__(self):
    st ="**************\n"
    st+=super(FancyHelloWorld, self).__str__()+"\n" # python2 compatible
    st+="**************\n"
    return st



class UberFancyHelloWorld(BaseHelloWorld):
  """Instantiating an object with shitload of parameters.  Initialization done using kwargs.  Refer to other classes like this: inherited from :class:`~skeleton.greeters.base.BaseHelloWorld`
  
  :class:`~BaseHelloWorld`
  
  :param person:   String identifying the person
  :param address:  Address
  :param age:      Person's age
  
  """
  parameters=[
    ["person", None,      str],
    ["address","nothing", str],
    ["age",    0,         int]
    ]
  
  
  def __init__(self, **kwargs):
    self.pre=self.__class__.__name__+" : " # auxiliary string for debugging output
    parameterInit(self,kwargs)
    
    
  def __str__(self):
    st ="**************\n"
    for parameter in self.parameters:
      st+=parameter[0]+ ": "+str(getattr(self,parameter[0]))+"\n"
    st+="**************\n"
    return st
  
  
  def doSomethingFancy(self,par):
    """This is simply a method that does something fancy with a parameter
    
    :param par: Parameter to do something fancy with
    
    In fact, an empty routine.  Remember that everything goes here as well: here is a link to :ref:`the introduction <about>`.
    
    """
    pass


  def doSomethingFancyAsWell(self):
    """This method also does something fancy
    """
    pass



    
def test1():
  """ Test UberFancyHelloWorld
  """
  pre=pre_mod+"test1 :"
  print(pre,"test1")
  print(pre,"Let's test UberFancyHelloWorld")
  hw=UberFancyHelloWorld(person="Sampsa",age=40)
  print(hw)
  hw=UberFancyHelloWorld(person="Sampsa",address="Helsinki",age=40)
  print(hw)
  try:
    hw=UberFancyHelloWorld(address="Helsinki",age=40)
  except AttributeError as e:
    print(e)
  else:
    print(hw)
  try:
    hw=UberFancyHelloWorld(person="Sampsa",address="Helsinki",age="40")
  except AttributeError as e:
    print(e)
  else:
    print(hw)
    
  print(pre,"Let's test FancyHelloWorld")
  try:
    hw=FancyHelloWorld("Sampsa")
  except AttributeError as e:
    print(e)
  else:
    print(hw)
  try:
    hw=FancyHelloWorld(1)
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

