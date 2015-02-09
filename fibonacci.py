

def memoize(func):
    cache = {}

    def memoizedFunction(*args, **kw):
        if args not in cache:
            cache[args] = func(*args, **kw)
        return cache[args]

    memoizedFunction.cache = cache
    return memoizedFunction

@memoize
def fib(n):
    if n < 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

if __name__ == '__main__':
    m = fib(100)
    print m
