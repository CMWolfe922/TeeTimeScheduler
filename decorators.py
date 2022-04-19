#!/usr/bin/.venv python3

from loguru import logger
from functools import wraps
from timeit import perf_counter
# create a decorator function to more easily log errors and debug


def logger(**config):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            logger_config = {kwargs.get(kwarg) for kwarg in kwargs}
            logger.info(func(*args, **logger_config))
            return func(*args, **kwargs)
        return wrapper
    return decorator


# Timer decorator. Time the execution of the code.
def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = perf_counter()
        result = func(*args, **kwargs)
        end = perf_counter()
        duration = end - start
        arg = str(*args)
        print(f'{func.__name__}({arg}) = {result} --> {duration:.8f}s')
        return result
    return wrapper
