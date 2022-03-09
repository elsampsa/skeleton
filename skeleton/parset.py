import yaml
from pprint import pformat

class ParameterSet:
    yaml_model=None # must subclass
    """Please subclass like this:
    
    ::
    
        class MyParameterSet(ParameterSet):
            yaml_model = [three quotes]\
                %YAML 1.2
                ---
                some: 1
                typical: kokkelis
                parameters: kikkelis
                for_your_parameter_set:
                    name : my_resource
        [three quotes]

    Use like this:

    ::

        p = MyParameterSet()
        p.typical # "kokkelis"
        print(p.getStr()) # shows whole structure as a pprinted dict
    
    Setting values:
    
    ::
    
        p.for_your_parameter_set.name = "something"
    

    Functions using these parameters, nicely declared with the custom class:

    ::

        def func(my_parameter_set: MyParameterSet):
            pass


    """
    def __init__(self, inp_str: str = None, inp_dic = None):
        if inp_dic is None:
            if inp_str is None:
                inp_str = self.yaml_model
            self.set_("saved_str", inp_str)
            tmp_dic = yaml.safe_load(inp_str)
        else:
            tmp_dic = inp_dic
        self.set_("dic_", {})
        for key, value in tmp_dic.items():
            if isinstance(value, dict):
                p = ParameterSet(inp_dic = value)
            elif isinstance(value, list):
                p = self.listToParset(value)
            else:
                p = value
            self.set_(key, p) # so that getattr for nicely for these
            self.dic_[key] = p # ..mirror
        
    def listToParset(self, lis):
        lis_ = []
        for el in lis:
            if isinstance(el, dict):
                p = ParameterSet(inp_dic = el)
            elif isinstance(el, list):
                p = self.handleList(el)
            else:
                p = el
            lis_.append(p)
        return lis_

    def listToDic(self, lis):
        lis_ = []
        for el in lis:
            if isinstance(el, ParameterSet):
                p = el.toDict()
            elif isinstance(el, list):
                p = self.listToDic(el)
            else:
                p = el
            lis_.append(p)
        return lis_

    def getSavedStr(self):
        return self.saved_str
        
    def __call__(self):
        return self.getSavedStr()

    def set_(self, key, value):
        super().__setattr__(key, value)
                
    def __setattr__(self, key, value):
        # print("setattr")
        par = getattr(self, key)
        assert(par.__class__ == value.__class__), "wrong class, should be " + par.__class__.__name__
        self.dic_[key] = value
        super().__setattr__(key, value)

    def listToStr(self, lis, cc = 0):
        st=""
        for el in lis:
            st += cc*" " + "- "
            if isinstance(el, ParameterSet):
                st += el.getStr(cc+2)
            elif isinstance(el, list):
                st += self.listToStr(el, cc+2)
            else:
                st += str(el) + "\n"
        return st

    def getStr(self, cc=0):
        st=""
        for key, value in self.dic_.items():
            st += cc*" " + key +": "
            if isinstance(value, ParameterSet):
                st += "\n" + value.getStr(cc+2)
            elif isinstance(value, list):
                st += "\n" + self.listToStr(value, cc+2)
            else:
                st += str(value) + "\n"
        return st
    
    def toDict(self):
        out_dic = {}
        for key, value in self.dic_.items():
            if isinstance(value, ParameterSet):
                out_dic[key] = value.toDict()
            elif isinstance(value, list):
                out_dic[key] = self.listToDic(value)
            else:
                out_dic[key] = value
        return out_dic
            
    def dumpYaml(self):
        # messes up the ordering..
        return yaml.dump(self.toDict())


    def checkList(self, lis, model):
        lis_ = []
        for i, el in enumerate(lis):
            m = model[i]
            assert(el.__class__ == m.__class__), "list element type should be " + m.__class__.__name__
            if isinstance(el, ParameterSet):
                el.check(m)
            elif isinstance(el, list):
                self.checkList(el, m)


    def check(self, model):
        for key, value in self.dic_.items():
            assert(key in model.dic_), "key '"+key+"' missing"
            class_ = model.dic_[key].__class__
            assert(value.__class__ == class_),\
                "type for key '"+key+"' should be " + class_.__name__
            if isinstance(value, ParameterSet):
                value.check(model.dic_[key])
            elif isinstance(value, list):
                self.checkList(value, model.dic_[key])


    def validate(self):
        self.check(self.__class__())



class MyParameterSet(ParameterSet):
    yaml_model="""\
%YAML 1.2
---
version: 1
some_par_1: kikkelis
some_par_2: kokkelis
main_par:
    sub_par: 123
    float_par: 1.2
    a_list:
        - 1
        - subkey1: 2.1
          subkey2: 2.2
        - 3
"""
