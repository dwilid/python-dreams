class LazyDict(MutableMapping):

    def __init__(self, *args, **kwargs):
        self.store = dict()
        self.backup = dict()
        self.update(dict(*args, **kwargs))

    def __getitem__(self, key):
        if callable(self.store[key]):
            self.store[key] = self.store[key]()
        return self.store[key]

    def __setitem__(self, key, value):
        if not callable(value):
            raise ValueError('Value must be a callable')
        self.backup[key] = value
        self.store[key] = value

    def __delitem__(self, key):
        del self.store[key]

    def __iter__(self):
        return iter(self.store)

    def __len__(self):
        return len(self.store)
    
    def __str__(self):
        return str(self.store)
    
    def reset(self, key):
        self.store[key] = self.backup[key]
