#!/usr/bin/.venv python3
import results as results
from loguru import logger
from functools import wraps
import time
from pathlib import Path
import os
import sys

# Loggers Path to save log files:
current_dir = Path.cwd()
logger_path = str(current_dir) + "\\data"


# create a decorator function to more easily
# log errors and debug

def base_logger(*, entry=True, exit=True, level="INFO"):
    def wrapper(func):
        name = func.__name__

        @wraps(func)
        def wrapped(*args, **kwargs):
            _logger = logger.opt(depth=1)
            if entry:
                _logger.log(level, "Entering '{}' (args={}, kwargs={})", name, args, kwargs)
            result = func(*args, **kwargs)
            if exit:
                _logger.log(level, "Exiting '{}' (result={})", name, result)
            return result

        return wrapped

    return wrapper


# Create the LogFormat
LogFormat = "<green>[+]</green> [<blue>{time:MM-DD-YYYY HH:mm:ss}</blue>] - [{level}:{name}] |<level>{message}</level>"

# create a decorator function to more easily
# log errors and debug

def Log(*, entry=True, exit=True, level="INFO"):
    def wrapper(func):
        name = func.__name__

        @wraps(func)
        def wrapped(*args, **kwargs):
            log_file = logger_path + "\\tee_time_scheduler.log"
            _logger = logger.opt(depth=1)
            _logger = logger.add(log_file, backtrace=True, diagnose=True, colorize=True, format=LogFormat)
            if entry:
                _logger.log(level, "Entering '{}' (args={}, kwargs={})", name, args, kwargs)
            result = func(*args, **kwargs)
            if exit:
                _logger.log(level, "Exiting '{}' (result={})", name, result)
            return result

        return wrapped

    return wrapper


# Build a normal timer just to take a log on execution time and
# Timer decorator. Time the execution of the code.
def Timer(func) -> object:

    @wraps(func)
    def wrapped(*args,**kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        stop = time.time()
        timer_result = stop - start
        logger.debug("Function '{}' executed in {:f} s", func.__name__, timer_result)
        return result
    return wrapped

