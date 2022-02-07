
def say_hello(name: str = 'Anonym') -> None:
    print('Hey,', name)


def my_func(*pos_params, a, b, c, d, ):
    print('a = ', a)
    print('b = ', b)
    print('c = ', c)
    print('d = ', d)
    print('pos = ', pos_params)

my_func(1, 2, 3, 4, 5, 56, 6, b=1, a=2, d=3, c=4, )


def my_func2(*args, **kwargs):
    print('*args ', args)
    print('**kwargs', kwargs)


my_func2(1, 2, 3, 4, 5, {1, 2, 3}, [12,3, 4], name='Denys', age=22, city='Kharkiv', languages=['English', 'UK'])


def my_func3(a, b, *, name1, name2):
    pass

my_func3(1, 2, name2=3, name1=4)

say_hello(name='Antony')

# print('Hello, Misha')
# print('Hello, Slavik')
# print('Hello, Illa')

# say_hello('Misha')
# say_hello('Slavik')
# say_hello('Illa')

def multiply(a: int, b: int) -> int:
    res = a * b
    print(res)
    return res, 4, 5
    # return None

print(multiply(5, 6))
print(multiply(-5, 60))


# def my_print(*values, sep=' ', end='\n'):
#     value_ls = list(str(val) for val in values)
#     out = sep.join(value_ls)
#     return f'{out}{end}'
    
# out = my_print(1, 2, 3, 4, sep='<>', end='\n\n\n')
# out = my_print([1,2,2,3,34])
# out = my_print('abc')


def is_even(number):
    return number % 2 == 0


numbers = list(range(100))
# evens = list(filter(is_even, numbers))
evens = list(filter(
    lambda number: number % 2 == 0,
    numbers
))
print(evens)
    

"""
1. Декоратор считает время выполнения функции и выводит результат в указанный файл
2. Декоратор переводит результат функции в строку
3. Декоратор выводит в файл название функции, ее параметры и результат выполнения
4. Написать функцию приветствия, которая считает сколько раз ее вызвали
"""

