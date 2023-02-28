"""
cli.py : cli entry-point

* Copyright: 2017-2023 [copyright holder]
* Authors  : Sampsa Riikonen
* Date     : 2023
* Version  : 0.1

This file is part of the skeleton library

An example cli entry-point that reads some command line arguments
and some parameters and loglevels from ~/.skeleton/some_data/

[copy-paste your license here]
"""
import logging, sys
import argparse
import configparser # https://docs.python.org/3/library/configparser.html
from skeleton.main import app
from skeleton import constant
from skeleton.tools import confLogger, configureLogging
from skeleton.local import AppLocalDir
from skeleton.parset import MyParameterSet
from skeleton.main import app
from skeleton import singleton
from pathlib import Path

def process_cl_args():
    comname = Path(sys.argv[0]).stem
    parser = argparse.ArgumentParser(
        usage=(
            f'{comname} [options]\n'
            '\n'
            'A demo cli entry-point that caches a default config\n'
            'file into ~./skeleton.  Logger verbosity is also defined there.\n'
        ),
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
        # ..shows default values with -h arg
    )
    parser.add_argument("command", action="store", type=str, help="mandatory command")
    parser.add_argument("--flag", action="store_true", help="a boolean flag", 
        default=False)
    parser.add_argument("--str", action="store", help="a string", default="nada",
        required=False)
    parser.add_argument("--reset", action="store_true", help="reset cached config files", 
        default=False)
    parsed, unparsed = parser.parse_known_args()
    for arg in unparsed:
        print("Unknow option", arg)
        sys.exit(2)
    return parsed


def main():
    parsed = process_cl_args()
    """# setting loglevels manually
    # should only be done in tests:
    logger = logging.getLogger("name.space")
    confLogger(logger, logging.INFO)
    """
    # some command filtering here
    if parsed.command in ["run"]:
        print("command is", parsed.command)
    else:
        print("unknown command", parsed.command)
        raise SystemExit(2)

    # some ideas on how to handle config files & default values
    #
    # this directory is ~/.skeleton/some_data/ :
    # init default data with yaml constant string

    some_data_dir = AppLocalDir("some_data")
    if (not some_data_dir.has("some.yml")) or parsed.reset:
        with open(some_data_dir.getFile("some.yml"), "w") as f:
            f.write(constant.SOME)

    # init default constant.MyParameterSet into ~/.skeleton/some_other_pars/default.yml
    other_dir = AppLocalDir("some_other_pars")
    if (not other_dir.has("default.yml")) or parsed.reset:
        with open(other_dir.getFile("default.yml"),"w") as f:
            f.write(constant.my_parameter_set())

    # tries to read & set loglevels from a yaml file:
    configureLogging(parsed.reset)

    # read MyParameterSet
    with open(other_dir.getFile("default.yml"),"r") as f:
        config_str = f.read()
    try:
        my_parameter_set = MyParameterSet(config_str)
    except Exception as e:
        print("FATAL : your MyParameterSet config file is broken")
        print("FATAL : failed with '%s'" % (str(e)))
        print("FATAL : remove/fix it and start the program again")
        raise SystemExit(2)

    my_parameter_set.validate()
    # print(my_parameter_set.getStr())
    singleton.setSomeGlobalParameter(my_parameter_set.some_par_1)

    # start the program:
    app(my_parameter_set = my_parameter_set)


if (__name__ == "__main__"):
    main()
