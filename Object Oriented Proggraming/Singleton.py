<<<<<<< HEAD
# https://webdevblog.ru/realizaciya-shablona-singleton-v-python/


class Singleton(object):
    _instance = None
    def __new__(class_, *args, **kwargs):
        if not isinstance(class_._instance, class_):
            class_._instance = object.__new__(class_, *args, **kwargs)
        return class_._instance

class MyClass(Singleton, BaseClass):
    pass

=======
# https://webdevblog.ru/realizaciya-shablona-singleton-v-python/


class Singleton(object):
    _instance = None
    def __new__(class_, *args, **kwargs):
        if not isinstance(class_._instance, class_):
            class_._instance = object.__new__(class_, *args, **kwargs)
        return class_._instance

class MyClass(Singleton, BaseClass):
    pass

>>>>>>> refs/remotes/origin/readme
