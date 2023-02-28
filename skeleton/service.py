"""
service.py : a service cli entry-point

* Copyright: 2017-2023 [copyright holder]
* Authors  : Sampsa Riikonen
* Date     : 2023
* Version  : 0.1

This file is part of the skeleton library

An example cli entry-point that reads some parameters and loglevel
info from an .ini file that you would mount as a "secret" in a cloud
environment

[copy-paste your license here]
"""
import logging, os
import argparse
import configparser # https://docs.python.org/3/library/configparser.html
from skeleton.main import app2
from skeleton import constant
from skeleton.tools import confLogger, configureLogging, IniCLI, getModulePath
from skeleton.local import AppLocalDir
from skeleton.parset import MyParameterSet
from skeleton.main import app
from skeleton import singleton


def main():
    cli = IniCLI(
        default_ini=os.path.join(getModulePath(),"ini","default.ini"),
        descr=(         
            '\n'
            'An example microservice-like cli entry-point\n'
            'Reads config stuff from an .ini file\n'
        )
    )
    cli.add_argument("command", action="store", type=str, help="mandatory command")
    cli.add_argument("--flag", action="store_true", help="a boolean flag", 
        default=False)
    cli.add_argument("--str", action="store", help="a string", default="nada",
        required=False)
    parsed, cfg = cli()
    # parsed are the cli arguments
    # cfg comes from the .ini file
    # loglevels have been set at this stage
    # some command filtering here
    if parsed.command in ["run"]:
        print("command is", parsed.command)
    else:
        print("unknown command", parsed.command)
        raise SystemExit(2)
    app2(cfg)


if (__name__ == "__main__"):
    main()
