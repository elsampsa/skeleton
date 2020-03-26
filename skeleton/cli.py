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
from skeleton.constant import default_ini


def set_logging(command, options, config):
    """
    print("got commands", args)
    config = kwargs["config"]
    print("with config", config)

    l = config["DEFAULT"]
    print(l)
    print(l["ServerAliveInterval"])

    l = config["logger_skeleton"]
    print(l)

    l = config["bitbucket.org"]
    print(l["User"])
    """
    for key in config.keys():
        if "logger_" in key:
            pars = config[key]
            qualname = pars["qualname"]
            levelstr = pars["level"]
            level = getattr(logging, levelstr)
            
            logger = logging.getLogger(qualname)
            logger.setLevel(level)

            if not logger.hasHandlers():
                formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
                ch = logging.StreamHandler()
                ch.setFormatter(formatter)    
                logger.addHandler(ch)

    """
    ## now, anywhere in your code, do this:
    logger = logging.getLogger("skeleton")
    logger.debug("debug")
    logger.info("info")
    """

    ## could chain more config / option handling here
    ## next, proceed to the actual entry point of your app
    app(command, options, config)


def process_cl_args():
  
    def str2bool(v):
        return v.lower() in ("yes", "true", "t", "1")

    parser = argparse.ArgumentParser(usage="""     
your_command [options] command

    commands:

        foo     Is not bar
        bar     Is not foo

    options:

        --nice  Be nice or not.  Default true.
        --ini   ini configuration file.

    """)
    parser.register('type','bool',str2bool)

    parser.add_argument("command", action="store", type=str,                 
                        help="mandatory command")

    parser.add_argument("--nice", action="store", type=bool, required=False, default=False,
                        help="Be nice")

    parser.add_argument("--ini", action="store", type=str, required=False, default=None,
                        help=".ini configuration file")

    parsed_args, unparsed_args = parser.parse_known_args()
    return parsed_args, unparsed_args


def main():
    parsed, unparsed = process_cl_args()

    cf = configparser.ConfigParser()
    cf.read_string(default_ini)

    if parsed.ini is None:
        pass
    else:
        files = cf.read(parsed.ini)
        # print("read files", files)

    ## some command filtering here
    if parsed.command in ["foo", "bar"]:
        set_logging(parsed.command, parsed, cf)
    else:
        print("unknown command", parsed.command)


if (__name__ == "__main__"):
    main()
