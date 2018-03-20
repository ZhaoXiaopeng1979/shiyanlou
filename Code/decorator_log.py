#! /usr/bin/env python3

from datetime import datetime
def log(func):
    def decorator(*args,**kwargs):
        print('Function '+func.__name__+' has been called at ' +datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        return func(*args,**kwargs)
    return decorator

@log
def add(x, y):
    return x + y
def add_no(x,y):
    return x+y
print('-'*30+'Use @'+'-'*30)
print('add(1,2)='+str(add(1, 2)))
print('add.__name__:'+add.__name__)

print('-'*30+'No @'+'-'*30)
print('add_no.__name__:'+add_no.__name__)
add_no = log(add_no)
print('add_no(1,2)',add_no(1, 2))
print('After log(add_no),add.__name__:'+add.__name__)
