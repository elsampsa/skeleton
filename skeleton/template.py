"""
NAME.py : Description of the file

* Copyright: 2017 [copyright holder]
* Authors  : Sampsa Riikonen
* Date     : 2017
* Version  : 0.1

This file is part of the skeleton library

[copy-paste your license here]
"""

import sys
from skeleton.tools import typeCheck, dictionaryCheck, objectCheck, parameterInitCheck, noCheck
pre_mod = "module.submodule : " # a string for aux debuggin purposes


class EmptyClass(object):
  """An example of how to make an API.  Initialization done using kwargs.  Inherited from :class:`~vainu_ner.greeters.base.BaseHelloWorld`
  
  API checks for input types: here we have a complex object type as an input parameter
  
  :param person: person's name : string, mandatory
  :param address: person's name : string, optional, default value = "nothing"
  :param age: person's age : integer, optional, default value = 0
  :param subgreeter: an object of the type :class:`~vainu_ner.greeters.fancy.FancyHelloWorld`
  
  """
  parameter_defs={
    "person"     : str,             # :param person: person's name : string, mandatory
    "address"    : (str,"nothing"), # :param address: person's name : string, optional, default value = "nothing"
    "age"        : (int,0),         # :param age: person's age : integer, optional, default value = 0
    "subgreeter" : FancyHelloWorld  # :param subgreeter: an object of the type :class:`~vainu_ner.greeters.fancy.FancyHelloWorld`
    }

    
  def __init__(self,**kwargs):
    self.pre=self.__class__.__name__+" : " # auxiliary string for debugging output
    parameterInitCheck(self.parameter_defs,kwargs,self) # check kwargs agains parameter_defs, attach ok'd parameters to this object as attributes

    
def test1():
  st="""Empty test
  """
  pre=pre_mod+"test1 :"
  print(pre,st)
  

def test2():
  st="""Empty test
  """
  pre=pre_mod+"test2 :"
  print(pre,st)
  

def main():
  pre=pre_mod+"main :"
  print(pre,"main: arguments: ",sys.argv)
  if (len(sys.argv)<2):
    print(pre,"main: needs test number")
  else:
    st="test"+str(sys.argv[1])+"()"
    exec(st)
  
  
if (__name__=="__main__"):
  main()

