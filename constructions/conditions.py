# if ...:
#     ...
# elif ...:
#     ...
# ...
# else:
#     ...

age = 18

if age <= 0:
    print("Не ражден!")
elif 0 < age <= 10:
    print("Малец")
elif 10 < age < 18:
    print("Подросток")
elif 18 <= age < 30:
    print("Молодой")
else:
    print("Взрослый") 