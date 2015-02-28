# -*- coding: utf-8 -*-

class ClassProperty(property):
    """propertyデコレータのクラス変数版
    class Foo(metaclass=PropertyMeta):
        __bar = None

        @ClassProperty
        def bar(self):
            return self.__bar

        @bar.setter
        def bar(self, value)
            self.__bar = value
    """
    pass

class PropertyMeta(type):
    """クラスプロパティデコレータ実装のためのメタクラス
    """
    def __new__(cls, name, bases, namespace):
        props = [(k,v) for k,v in namespace.items() if type(v) == ClassProperty]
        for k, v in props:
            setattr(cls, k, v)
            del namespace[k]
        return type.__new__(cls, name, bases, namespace)
