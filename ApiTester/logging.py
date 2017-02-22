import os
from robot.api import logger
from robot.libraries.BuiltIn import BuiltIn

def log(message):
    if _get_log_level() is None:
        level = 'INFO'
    else:
        level = _get_log_level().upper() 
    if (level == 'INFO'):
        _info(message)
    elif (level == 'DEBUG'):
        _debug(message)
    elif (level == 'WARN'):
        _warn(message)

def _get_log_level():
    try:
        variables = BuiltIn().get_variables()
        return variables.get('${LOG LEVEL}', 'INFO')
    except:
        return None

def _debug(message):
    logger.debug(message)

def _info(message):
    logger.info(message)

def _warn(message):
    logger.warn(message)
