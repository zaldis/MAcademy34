def start_sets():
    fruits = {'cherry', 'apple', 'strowberry', 'cherry'}

    fruits.add('peanapple')
    # fruits.remove('peanapple')

    for fruit in fruits:
        print(f'Check is {fruit} in fruits', fruit in fruits)

    print(len(fruits))


def count_unique_names():
    names = ['Denys', 'Anton', 'Emma', 'Anton', 'Emma', 'Denys', 'Bro', 'Avraam']
    unique_names = set(names)
    unique_count = len(unique_names)
    print(f"There are {unique_count} unique names")



start_sets()