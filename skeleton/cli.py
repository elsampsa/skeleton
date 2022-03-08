"""
NAME.py : Description of the file

* Copyright: 2017 [copyright holder]
* Authors  : Sampsa Riikonen
* Date     : 2017
* Version  : 0.1

This file is part of the skeleton library

[copy-paste your license here]
"""
import logging
import argparse
import configparser # https://docs.python.org/3/library/configparser.html
from skeleton.main import app
from skeleton import constant
from skeleton.tools import confLogger, configureLogging
from skeleton.local import AppLocalDir
from skeleton.parset import MyParameterSet
from skeleton.main import app

def process_cl_args():
  
    def str2bool(v):
        return v.lower() in ("yes", "true", "t", "1")

    parser = argparse.ArgumentParser(usage="""     
skeleton-command [options] command

    commands:

        run     run me

    options:

        --nice      Be nice or not.  Needs boolean value.  Default true.
        --ini       Ini configuration file (optional)
        --reset     Reset config files (don't specify a value)
        
    """)
    # parser.register('type','bool',str2bool)  # this works only in theory..

    parser.add_argument("command", action="store", type=str,                 
                        help="mandatory command")

    parser.add_argument("--nice", action="store", type=str2bool, required=False, default=False,
                        help="Be nice")

    parser.add_argument("--ini", action="store", type=str, required=False, default=None,
                        help=".ini configuration file")

    parser.add_argument('--reset', action='store_true')

    parsed_args, unparsed_args = parser.parse_known_args()
    return parsed_args, unparsed_args


def main():
    parsed, unparsed = process_cl_args()

    if parsed.ini is None:
        pass
    else:
        # an example how to set the loggers from an ini file
        cfg = configparser.ConfigParser()
        cfg.read(parsed.ini)
        try:
            logging.config.fileConfig(cfg, disable_existing_loggers=True)
        except Exception as e:
            print("there was error reading your .ini file.  Please check your logger definitions")
            print("failed with:", e)
            raise(e)
        # using ini files
        # files = cfg.read(parsed.ini)
        # print("read files", files)
        # accessing variables from ini files:
        # cfg["DEFAULT"]["somepar"]

    
    # setting loglevels manually
    # should only be done in tests:
    """
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

    app(my_parameter_set = my_parameter_set)


if (__name__ == "__main__"):
    main()
