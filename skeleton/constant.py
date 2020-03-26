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
