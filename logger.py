#!/usr/bin/.venv python3

from loguru import logger
from functools import wraps

# create a decorator function to more easily log errors and debug


def logger(**config):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            logger_config = {kwargs.get(kwarg) for kwarg in kwargs}
            logger.info(func(*args, **logger_config))
