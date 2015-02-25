
from functools import wraps
def wrapper(func):
    @wraps(func)
    def wrap(*args,**kw):
        print 'add a wrapper'
        return func(*args, **kw)

    return wrap

@wrapper
def test():
    '''test func name'''
    print 'this is a test'

@wrapper
def add(a,b):
    print "a:%d b:%d"%(a,b)
    print a+b

if __name__ == '__main__':
    test()
    print test.__doc__
    add(10,10)
