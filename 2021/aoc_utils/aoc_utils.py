import time


def measure(ndigits):
    def _(f):
        def __(*args):
            print('executing {}..'.format(f.__name__))
            start = time.time()
            f(*args)
            end = time.time()
            print('elapsed time: {}ms'.format(round(1000 * (end - start), ndigits)))

        return __
    return _
