def apply(*funcs):
    def _apply(*args, **kwargs):
        return tuple(f(*args, **kwargs) for f in funcs)

    return _apply


def cat(*xs):
    ys = []
    for x in xs:
        ys += x
    return ys


def concatenate(xxs):
    return ft.reduce(cat, xxs)


def thread(obj, *funcs):
    for f in funcs:
        obj = f(obj)
    return obj
