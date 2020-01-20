
def track_mutations(methods='append'):
    def mutable(class_type):

        print("In mutable")
        class_init = class_type.__init__
        class_methods = {k: v for k, v in class_type.__dict__.items() if callable(v)}
        print("Class mehtods ", class_methods)

        def inner(self, *args, **kwargs):
            self._changed = False
            class_init(self, *args, **kwargs)

        class_type.__init__ = inner

        return class_type

    return mutable


@track_mutations(methods='append')
class Test:
    def __init__(self, a):
        self.a = a
        self.cont = []
        print("In test init")

    def append(self, b):
        print("In append")
        self.cont.append(b)

    def remove(self, b):
        pass

    def call(self):
        pass


if __name__ == "__main__":
    tt = Test(10)
    # print(tt.a, tt._changed)
