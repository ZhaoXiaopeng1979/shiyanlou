#!/usr/bin/env python3
from functools import wraps
from datetime import datetime

def log(func):
    @wraps(func)
    def decorator(*args, **kwargs):
        print('Function ' + func.__name__ + ' has been called at ' + datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

        return func(*args, **kwargs)
    return decorator

@log
def add(x, y):
    return x + y

print(add.__name__)
print(add(1,2))

