import time


def measure(ndigits):
    def _(f):
        def __(*args):
            print('executing {}...'.format(f.__name__))
            start = time.time()
            f(*args)
            end = time.time()
            print('elapsed time: {}ms'.format(round(1000 * (end - start), ndigits)))

        return __
    return _


def memoized(f):
    solutions = {}

    def has_precomputed_result(*args):
        if len(args) is 0:
            args = [None]
        s = solutions
        for arg in args:
            if arg not in s:
                return False
            s = s[arg]
        return True

    def set_precomputed_result(result, *args):
        if len(args) is 0:
            args = [None]
        curr, prev = solutions, None
        for arg in args:
            if arg not in curr:
                curr[arg] = {}
            curr, prev = curr[arg], curr
        prev[args[-1]] = result

    def get_precomputed_result(*args):
        if len(args) is 0:
            args = [None]
        s = solutions
        for arg in args:
            s = s[arg]
        return s

    def inner(*args):
        if not has_precomputed_result(*args):
            set_precomputed_result(f(*args), *args)
        return get_precomputed_result(*args)

    return inner