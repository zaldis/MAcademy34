class TextInt:
    def __init__(self, name: str):
        self._name = name

    def __int__(self):
        names_map = {
            'one': 1,
            'two': 2,
            'three': 3,
            'four': 4
        }
        return names_map.get(self._name, 0)

    def __eq__(self, obj: object) -> bool:
        if not isinstance(obj, TextInt):
            return False
        return self._name == obj._name

    def __hash__(self) -> int:
        return hash(self._name)

    def __add__(self, num: 'TextInt') -> int:
        return int(self) + int(num)

    def __str__(self):
        return f'<TextInt: {self._name}>'

    def __repr__(self) -> str:
        return str(self)


one = TextInt('one')
two = TextInt('two')
# print(int(one) + int(two))
print(one + two)


counter = {}
counter[TextInt('one')] = 1
counter[TextInt('one')] += 1
counter[TextInt('one')] += 1

counter[TextInt('two')] = 0

print(counter)