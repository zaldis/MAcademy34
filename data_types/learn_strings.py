"""This is the doc string"""

'abca sdfklj aksdf; jkasdfk; jasd;f j'
"jald fjasdf; j asdfj ;as djf asdjkf ;asdjf"

# Ctrl + /
# text = 'I've the car'
text1 = "I've the car"
text2 = 'I\'ve the car'

"""
print("This is tab \t <==")
print("This is new line \n")
"""

age = 15
print('I am %d years old' % age)
print('I am %f years old' % age)
print('I am {:f} years old'.format(age))
print(
    'My name is {1}.\n'
    'I am {0:f} years old.\n'
    'I am {1}'.format(age, 'Denys')
)
print(
    'My name is {name}.\n'
    'I am {age:f} years old.\n'
    'I am {name}'.format(age=age, name='Denys')
)
print(f'I am {age} years old')
print(f'I am {age:f} years old')