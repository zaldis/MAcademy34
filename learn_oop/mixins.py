class AttrsCountMixin:
    @property
    def attrs_count(self):
        return len(self.__dict__.keys())


class HelloMixin:
    def hello(self):
        print(f'hello from {type(self).__name__}')


class Demo(AttrsCountMixin, HelloMixin):
    def __init__(self):
        self.field = 'abc'
        self.field2 = 'bcd'


class Demo2(AttrsCountMixin, HelloMixin):
    def __init__(self) -> None:
        self.class_field = 'class field value'


d = Demo()
d2 = Demo2()
print(d.attrs_count, d2.attrs_count)

d.hello()
d2.hello()
