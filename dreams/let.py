from contextlib import contextmanager


class Let:
    def __init__(self, *variables):
        self.vars = tuple(variables)

    def __enter__(self):
        return self.vars

    def __exit__(self, *exc):
        pass


@contextmanager
def let(*args):
    yield tuple(args)


if __name__ == '__main__':
    with Let(1, 2, 3) as (x, y, z):
        with let(x, y, z) as (a, b, c):
            print(a, b, c)
