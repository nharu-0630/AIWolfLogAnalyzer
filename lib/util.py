import os
import errno
import configparser

def check_config(config_path:str) -> configparser.ConfigParser:

    if not os.path.exists(config_path):
        raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), config_path)
    
    return configparser.ConfigParser()

def read_inifile(config_path:str) -> configparser.ConfigParser:
    inifile = check_config(config_path=config_path)

    return inifile.read(config_path,"UTF-8")