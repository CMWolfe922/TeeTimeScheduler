#!/usr/bin/.venv python3
from loguru import logger
from functools import wraps
import time
from pathlib import Path
import os
import sys

# Loggers Path to save log files:
logger_path = Path.cwd() + "\\data"

# create a decorator function to more easi                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            ly log errors and debug


def start_log(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        base_format = "|{name}||{time}||{level}||{message}|"
        file = os.path.join(logger_path, "main.log")

        # add log before function or methods
        logger.add(sys.stderr, format=base_format)


# Build a normal timer just to take a log on execution time and
# Timer decorator. Time the execution of the code.
def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        duration = end - start
        arg = str(*args)
        print(f'{func.__name__}({arg}) = {result} --> {duration:.8f}s')
        return result
    return wrapper
