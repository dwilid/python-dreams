def please(f):
    def _please(x):
        try:
            return f(x)
        except:
            return x
    return _please


def inspect(obj):
    """Shamelessly stolen from Elixir"""
    print(obj)
    return obj
