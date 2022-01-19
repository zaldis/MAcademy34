"""
You have the list

Sort the list and return each 2d item
"""
from pprint import pprint


def select_2d_items():
    numbers = [4, 2, 1, 4, 2, -3, 2, 0, 3]
    sorted_numbers = sorted(numbers)

    print(numbers, sorted_numbers, sorted_numbers[::2])


def learn_for_loop():
    numbers = [1, 2, 3, 4, 5, 6]
    for number in numbers:
        is_even = (number % 2 == 0)
        if is_even:
            print(f'The number {number} is even')
        else:
            print(f'The number {number} is not even')


def select_even_numbers():
    numbers = [1, 2, 3, 2, 1, 0, -3, 2, 4]
    even_nubmers = []

    for number in numbers:
        is_even = (number % 2 == 0)
        if is_even:
            even_nubmers.append(number)
    
    return even_nubmers


def select_even_numbers_with_list_comp():
    numbers = [1, 2, 3, 2, 1, 0, -3, 2, 4]
    even_numbers = [
        str(number)
        for number in numbers 
        if number % 2 == 0
    ]

    # even_numbers = []
    # for number in numbers:
    #     is_even = (number % 2 == 0)
    #     if is_even:
    #         even_numbers.append(1000 * number)
    
    return even_numbers


matrix = [[0] * 10] * 10

matrix = [[0] * 10 for _ in range(10)]

# matrix = []
# for _ in range(10):
#     matrix.append([0] * 10)

matrix[0][0] = 5

pprint(matrix)