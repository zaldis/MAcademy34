class Ball:
    pass


def learn_dynamic_creation():
    ball = Ball()
    ball.color = 'red'
    ball.radius = 10
    print(ball.color, ball.radius, ball.__dict__)


def learn_inheritance():
    class MyInt(int):
        tag = 'my tag'

    pure_number = int(5)
    my_number = MyInt(5)

    print(
        'Pure number:', getattr(pure_number, 'tag', 'Has no tag')
    )

    print(
        'My number:', getattr(my_number, 'tag', 'Has no tag')
    )

    my_number.tag = ...

# __...__ -> dunder -> double under scores  <<-- magic methods

#  learn_inheritance()

def learn_classes():
    people = [
        {
            'first_name': 'Ivan',
            'last_name': 'Borisov',
            'weight': 90,
            'year_of_birth': 1990,
        }, {
            'first_name': 'Nero',
            'last_name': 'Siro',
            'weight': 40,
            'year_of_birth': 1950,
        }, {
            'first_name': 'Abra',
            'last_name': 'Bumba',
            'weight': 50,
            'year_of_birth': 1800,
        }, ..., {}
    ]

    people[0]['weight'] = 2000


    class Person:
        # Конструктор
        def __init__(self, first_name, last_name, weight, year_of_birth):
            self.first_name = first_name
            self.last_name = last_name
            self.weight = weight
            self.year_of_birth = year_of_birth

    class Patient(Person):
        def __init__(
            self,
            first_name,
            last_name,
            weight,
            year_of_birth,
            temperature=36.6,
            eye_color='brown'
        ):
            super().__init__(first_name, last_name, weight, year_of_birth)
            self.temperature = temperature
            self.eye_color = eye_color

        def get_status(self) -> str:
            if self.temperature <= 36.6:
                return 'Looks good'
            elif self.temperature <= 38:
                return 'Beware high temperature'
            else:
                return 'Karaul!'


    people1 = [
        Patient('Ivan', 'Borisov', 90, 1990),
        Patient('Nero', 'Siro', 40, 1950, 40),
        Patient('Abra', 'Bumba', 50, 1800)
    ]

    statuses = [patient.get_status() for patient in people1]
    
    # statuses = ['a', 'b', 'c']  -> print(statuses) == print(['a', 'b', 'c'])
    # print(*statuses) == print('a', 'b', 'c')
    print(*statuses, sep='\t')

    # print(people1[0].temperature)
    # person = Person()
    # person.first_name = 'Abra'
    # person.last_name = 'Bumba'
    # person.weight = 50
    # person.year_of_birth = 1800


# print(issubclass(Ball, object))
learn_classes()