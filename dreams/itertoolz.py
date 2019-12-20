def head(xs):
    if type(xs) is list or type(xs) is tuple:
        return xs[0]
    return next(xs)


def tail(xs):
    if type(xs) is list or type(xs) is tuple:
        return xs[1:]


def head_tail(xs):
    return xs[0], xs[1:]


def take(n):
    def _take(xs):
        if type(xs) is tuple:
            return xs[:n]
        if type(xs) is list:
            try:
                for _ in range(n):
                    yield xs.pop(0)
            except IndexError:
                return
        try:
            for _ in range(n):
                yield next(xs)
        except StopIteration:
            return

    return _take


def peek(n):
    def _peek(xs):
        if type(xs) is list or type(xs) is tuple:
            return xs[:n]
        xs = iter(xs)
        return [next(xs) for _ in range(n)]

    return _peek


def fetch(itr, *keys):
    """Generator which yields values from an iterator of dictlike
    objects
    """
    for i in itr:
        if len(keys) > 1:
            yield tuple(i[k] for k in keys)
        else:
            yield i[keys[0]]
