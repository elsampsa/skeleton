"""
base.py : Greeter base classes

* Copyright : 2017 Sampsa Riikonen
* Authors  : Sampsa Riikonen
* Date     : 2017
* Version  : 0.1

This file is part of the python skeleton example library

Skeleton example library is free software: you can redistribute it and/or modify it under the terms of the MIT License.  This code is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the MIT License for more details.
"""
import sys
pre_mod = "skeleton.greeters.base : " # a string for aux debugging



# If I remember correctly, in python3 all classes are automatically children of object
class BaseHelloWorld(object):
  """ A Greeter base class
  
  :param person: A person's name
  """
  
  def __init__(self, person):
    self.pre=self.__class__.__name__+" : " # auxiliary string for debugging output
    self.person=person
    # print(self.pre,"__init__","leaving constructor") # auxiliary debug string
    
    
  def __str__(self):
    st="Hello from "+self.person
    return st
    
    
    
def test1():
  """Empty test
  """
  pre=pre_mod+"test1 :"
  print(pre,"test1")
  print(pre,"description of test 1")


def test2():
  """Empty test
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


