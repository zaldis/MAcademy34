class Demo:
    def __getattr__(self, attr_name: str):
        attr_map = {
            'name': 'Demo name',
            'person': 'Demo person'
        }
        return attr_map.get(attr_name, '-- Empy value --')
        # if attr_name == 'name':
        #     return 'Demo name'
        # if attr_name == 'person':
        #     return 'Demo person'
        # return None


d = Demo()
print(d.name)
print(d.person)
print(d.strange_field)


