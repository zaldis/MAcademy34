


# def calc(num):
#     num2 = num
#     return num2

# other_calc = calc

# print(other_calc(10))


# for i in range(1, 10):
#     if i == 1:
#         sm = 1
#     else:
#         sm += 1

# print(sm)



# def fun1():
#     def fun2():
#         def fun3():
#             ...

#         fun3()
#         fun2()
#         fun1()
    
#     fun2()
#     fun1()

# fun1()



number = 100  # global


def func_outer():
    number = 15 # nonlocal

    def func():
        number = 10 # local
        number += 5

# func()
# print(number)


def counter(start: int):
    # value = start
    
    def next():
        nonlocal start
        start += 1
        return start
        # nonlocal value
        # value += 1
        # return value

    return next


cntr = counter(0)
for _ in range(1, 30):
    print(cntr())