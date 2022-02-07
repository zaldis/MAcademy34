from datetime import datetime
from functools import lru_cache


class Person:
    def __init__(self, first_name, last_name, year_of_birth):
        self.first_name = first_name
        self.last_name = last_name
        self.years_of_birth = year_of_birth

    def get_age(self):
        return datetime.now().year - self.years_of_birth

    @property
    def years_of_birth(self):
        return self._years_of_birth

    @years_of_birth.setter
    def years_of_birth(self, value: int):
        if not isinstance(value, int):
            raise ValueError(f'Years of birsth must be integer value not {type(value)}')
        
        curr_year = datetime.now().year
        if not (1800 <= value <= curr_year):
            raise ValueError(f'Years of birth must be in range 1800 .. {curr_year}. Current year is {value}')

        self._years_of_birth = value

    @property
    @lru_cache(None)
    def age(self) -> int:
        print('Calculating...')
        return datetime.now().year - self.years_of_birth

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name} {self.age}y.o.'





person = Person('Antony', 'Hopkins', 1990)
# print(person)

print(person.age)
print(person.age)
print(person.age)
print(person.age)
print(person.age)
print(person.age)
print(person.age)


print(person.years_of_birth)
person.years_of_birth = '100'
