# -*- coding : utf-8 -*-


class UniqueAttrValueContainer:

    def __init__(self, iterable):
        self.__container = list()

    def add(self, value):
        pass

    def update(self, value, predicate):
        pass

    def get(self, predicate):
        pass

    def remove(self, value, predicate):
        pass

    def __iter__(self):
        return iter(self.__container)

    def __len__(self):
        return len(self.__container)


if __name__ == '__main__':
    a = Un