print("For list")
for number in [1, 2, 3]:
    print(number)


print("\n\nFor tuple")
for number in (1, 2, 3, ):
    print(number)


print("\n\nFor set")
for number in {1, 2, 3, }:
    print(number)


profiles = {
    'Adam': 20,
    'Petro': 19,
    'Angel': 27,
}
print("\n\nFor dict - keys")
for number in profiles.keys():
    print(number)

print("For dict - values")
for number in profiles.values():
    print(number)

print("For dict - key/value")
for name, years in profiles.items():
    print(f'{name} is {years} years old')


print("\n\nSimple range")
for number in range(-15, 16, 2):
    print(number)


print("\n\nSimple range with enumerate")
for order, number in enumerate(range(-15, 16, 2), start=1):
    print(f'{order}:\t{number}')


"""
1 .. 10 and 15 .. 20
"""
print('\n\nNumbers without middle')
for order, number in enumerate(range(1, 21), start=1):
    if 1 <= number <= 10 or 15 <= number <= 20:
        print(f'{order}:\t{number}')

print('\n\nNumbers without middle (continue)')
for order, number in enumerate(range(1, 21), start=1):
    if 11 <= number <= 14:
        continue
    print(f'{order}:\t{number}')


names = ['dog'] * 1_000_000
names[4] = 'cat'

has_cat = False
counter = 0
for name in names:
    if has_cat:
        break
    if name == 'cat':
        has_cat = True
    counter += 1
print('has cat:', has_cat)
print('iterations', counter)


ind = 0
name = names[ind]
while name != 'cat' and ind < len(names):
    ind += 1
    name = names[ind]
has_cat = name == 'cat'
print('has cat:', has_cat)
print('iterations', ind)