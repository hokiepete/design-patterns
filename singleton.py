def singleton(cls):
    instances = {}
    def wrapper(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return wrapper

@singleton
class SingletonList(list):
    def __init__(self):
        super().__init__()


a = SingletonList()
b = SingletonList()
assert a is b