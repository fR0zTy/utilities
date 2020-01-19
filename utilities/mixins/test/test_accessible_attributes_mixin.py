# -*- coding : utf-8 -*-

from utilities.mixins import AccessibleAttributesMixin


class MockObject(AccessibleAttributesMixin):

    def __init__(self):
        super().__init__(self)
        self.attr_1 = 10
        self._attr_2 = 20
        self.__attr_3 = 40


def test_iter_public_attributes():
    obj = MockObject()
    public_attrs = ['attr_1']
    itered_attrs = list(obj.iter_attrs())


    assert len(public_attrs) == len(itered_attrs)
    assert all(attr in public_attrs for attr in itered_attrs)


def test_iter_public_and_protected_attributes():
    obj = MockObject()
    obj.allow_protected_access = True

    attrs = ["attr_1", "_attr_2"]
    itered_attrs = list(obj.iter_attrs())

    assert len(attrs) == len(itered_attrs)
    assert all(attr in attrs for attr in itered_attrs)


if __name__ == "__main__":
    test_iter_public_attributes()
    test_iter_public_and_protected_attributes()
