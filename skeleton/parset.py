import yaml
from pprint import pformat

class ParameterSet:
    """

    Suppose this yaml string:

    ::
    
        %YAML 1.2
        ---
        config:
            version: 1
            some_server: kokkelis
            some_par: kikkelis
            resource:
                name : my_resource
                
    You would do this:
    
    ::
    
        p = ParameterSet(yaml_str)
        c = p.config # another ParameterSet instance with version, some_server, etc.
        c.some_server # "kokkelis"
        print(c.getStr()) # shows whole structure as a pprinted dict
    
    Setting:
    
    ::
    
        p.config.resource.name = "new_name"
    
    """
    def __init__(self, inp_str: str = None, inp_dic: dict = None):
        self.set_("saved_str", inp_str)
        if (inp_dic is None) and (inp_str is None):
            raise(AssertionError("provide a yaml string or a dict"))        
        if inp_dic is None:
            tmp_dic = yaml.safe_load(inp_str)
        else:
            tmp_dic = inp_dic
        self.set_("dic_", {})
        for key in tmp_dic.keys():
            if isinstance(tmp_dic[key], dict):
                p = ParameterSet(inp_dic = tmp_dic[key])
            else:
                p = tmp_dic[key]
            self.set_(key, p) # so that getattr for nicely for these
            self.dic_[key] = p # ..mirror
        
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

    def getStr(self, cc=0):
        st=""
        for key, value in self.dic_.items():
            st += cc*" " + key +": "
            if isinstance(value, ParameterSet):
                st += "\n" + value.getStr(cc+2)
            else:
                st += str(value) + "\n"
        return st
    
    def toDict(self):
        out_dic = {}
        for key, value in self.dic_.items():
            if isinstance(value, ParameterSet):
                out_dic[key] = value.toDict()
            else:
                out_dic[key] = value
        return out_dic
            
    def dumpYaml(self):
        # messes up the ordering..
        return yaml.dump(self.toDict())

