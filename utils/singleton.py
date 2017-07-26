class Singleton(object):
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = object.__new__(cls)
            cls.__instance.__initialized = False

        return cls.__instance

    def __init__(self, *args, **kwargs):
        if (self.__initialized): return
        self.__initialized = True

    @classmethod
    def get_instance(cls, *args, **kwargs):
        if not cls.__instance:
            return cls(*args, **kwargs)
        else:
            return cls.__instance

    @classmethod
    def reset_instance(cls):
        if cls.__instance:
            cls.__instance = None
