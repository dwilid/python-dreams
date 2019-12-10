def please(f):
    def _please(x):
        try:
            return f(x)
        except:
            return x
    return _please
