my_dict = {
    "apple": 20,
    "carrot": 40,
    "potato": 25
}

my_dict['butter'] = 15
# del my_dict['butter']

print("Check if dictionary contains key `butter`:", 'butter' in my_dict)

for name, count in my_dict.items():
    print(name, count)

total = sum(my_dict.values())
print("Total count:", total)

print(my_dict.get('house1', 'default value'))