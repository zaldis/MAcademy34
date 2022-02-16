class Demo:
    def __init__(self):
        self._name = 'demo'
        self.__hidden_name = 'hidden_demo'

    @property
    def tag(self):
        return self._name


class DemoPlus(Demo):
    def __init__(self):
        super().__init__()
        self._name = 'demo_plus'
        print(self._Demo__hidden_name)


demo = Demo()
print(demo._name)
# print(demo.__hidden_name)
demo_plus = DemoPlus()
print(demo_plus._name)
