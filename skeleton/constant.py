"""
constant.py : Some constants for your module

* Copyright: 2020 Sampsa Riikonen
* Authors  : Sampsa Riikonen
* Date     : 2020
* Version  : 0.1

This file is part of the skeleton library

Skeleton example library is free software: you can redistribute it and/or modify it under the terms of the MIT License.  
This code is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  
See the MIT License for more details.
"""

LOGGING_CONF_YAML_DEFAULT = """\
%YAML 1.2
---
logging:

    version: 1
    disable_existing_loggers: true
    root:
            level: !!python/name:logging.NOTSET
            handlers: [console]
    
    loggers:
        # *** Configure here your loggers ***
        
        this.is.namespace: # namespace you have defined for you logger
            level: !!python/name:logging.DEBUG
            handlers: [console]
            qualname: this.is.namespace
            propagate: false
        
    handlers:
      
        console:
            class: logging.StreamHandler
            stream: ext://sys.stdout
            formatter: simpleFormatter
            level: !!python/name:logging.NOTSET
      
    formatters:
        simpleFormatter:
            format: '%(name)s - %(levelname)s - %(message)s'
            datefmt: '%d/%m/%Y %H:%M:%S'
"""

SOME = """\
%YAML 1.2
---
data:

    version:1
    some: random yaml data
"""

default_ini = """\
[DEFAULT]
ServerAliveInterval = 45
Compression = yes
CompressionLevel = 9
ForwardX11 = yes

[bitbucket.org]
User = hg

[topsecret.server.com]
Port = 50022
ForwardX11 = no

[logger_skeleton]
level = DEBUG
handlers =
qualname = skeleton
"""

from .parset import ParameterSet

# this is a nice way to define a large set of default values
some_parameter_set = ParameterSet(
    inp_str = """\
%YAML 1.2
---
config:
    version: 1
    some_par_1: kikkelis
    some_par_2: kokkelis
    main_par:
        sub_par: 123
""")

PARS = some_parameter_set.config
"""you can now access values with:

PARS.some_par_1
PARS.main_par.sub_par

In your code:

def someFunc(pars: ParameterSet):
    # pars: some_parameter_set.config from constant.py
    self.p = pars
    self.p.some_par_1
    # etc.
"""
