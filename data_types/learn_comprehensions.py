numbers = [1, 2, 3, 1, 1, 2, 3, 1]

# list comprehension
even_pos_numbers = [
    number for number in numbers[1::2]
]

# set comprehension
even_pos_set_numbers = {
    number for number in numbers[1::2]
}

# dict comprehension
even_pos_dict_numbers = {
    number: str(number) for number in numbers[1::2]
}


print(even_pos_numbers)
print(even_pos_set_numbers)
print(even_pos_dict_numbers)