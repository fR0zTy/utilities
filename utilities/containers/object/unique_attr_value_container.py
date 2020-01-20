# -*- coding : utf-8 -*-

from collections import Hashable


def default_state_eval_func(obj):
    obj_hash = 0

    for attr, val in vars(obj).items():
        # ignore all the private and protected attributes, as an external objects
        # should only have access to public attributes
        if attr.startswith("_"):
            continue

        if isinstance(val, Hashable):
            obj_hash ^= hash(val)
        else:
            obj_hash ^= hash(frozenset(val.items())) if instance(val, dict) else hash(frozenset(val))

    return obj_hash


class UniqueObjectStateContainer:

    def __init__(self, state_eval_func=None):
        self.__container = {}
        self.__id_key_lut = {}

        self._state_eval_func = state_eval_func if state_eval_func is not None else default_state_eval_func

    def add(self, obj):
        key = self._state_eval_func(obj)
        if key in self.__container:
            raise ValueError("An object with similar state already exists!")
        self.__container[key] = obj
        self.__id_key_lut[id(obj)] = key

    def get(self, obj):
        return self.__container[self.__id_key_lut[id(obj)]]

    def update(self, obj, attr_val_dict):
        obj = self.get(obj)

    def remove(self, value, predicate):
        pass

    def __iter__(self):
        return iter(self.__container)

    def __len__(self):
        return len(self.__container)


if __name__ == '__main__':
