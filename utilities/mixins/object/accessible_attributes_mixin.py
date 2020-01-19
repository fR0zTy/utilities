# -*- coding : utf-8 -*-

class AccessibleAttributesMixin:
    """
    Mixin class for accessing, iterating over object attributes more easily.
    """

    def __init__(self, obj, allow_protected_access=False):
        self.__obj = obj
        self.__allow_protected_access = allow_protected_access
        self.__invalid_name_prefs = set([f'_{self.__obj.__class__.__name__}__',
                                         f'_{AccessibleAttributesMixin.__name__}__'])

    def _validate_attr(self, attr):
        return (all(not attr.startswith(name) for name in self.__invalid_name_prefs) and
                (self.allow_protected_access or not attr.startswith('_')))

    @property
    def allow_protected_access(self):
        return self.__allow_protected_access

    @allow_protected_access.setter
    def allow_protected_access(self, value):
        self.__allow_protected_access = value

    @property
    def obj(self):
        return self.__obj

    def iter_attr_vals(self):
        for attr, val in vars(self.__obj).items():
            if self._validate_attr(attr):
                yield attr, val

    def iter_attrs(self):
        for attr, _ in self.iter_attr_vals():
            yield attr

    def iter_values(self):
        for _, val in self.iter_attr_vals():
            yield val