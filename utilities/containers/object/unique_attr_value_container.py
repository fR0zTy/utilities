# -*- coding : utf-8 -*-

import hashlib

from utilities.misc.object_utils import iter_attributes


def default_state_eval_func(obj):
    obj_hash = hashlib.sha1()
    for attr in iter_attributes

class UniqueObjectStateContainer:

    def __init__(self, iterable, state_eval_func=None):
        self.__container = {}

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
