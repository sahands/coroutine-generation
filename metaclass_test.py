class M(type):
    def __new__(cls, *args):
        return super().__new__(cls, *args)


class C(metaclass=M):
    pass


c = C()

print(type(c) is C)        # True
print(type(C) is M)     # True
print(type(M) is type)  # True
print(type(type) is type)  # True
