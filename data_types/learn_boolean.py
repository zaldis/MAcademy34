True 
False

bob_age = 17
ann_age = 22
bill_age = 3
anton_age = 18

# count => cnt
adult_cnt = 0
ADULT_AGE = 18

# if bob_age == 18:
#     adult_cnt = adult_cnt + 1

# adult_cnt = adult_cnt + (bob_age >= 18)
# adult_cnt = adult_cnt + (ann_age >= 18)
# adult_cnt = adult_cnt + (bill_age >= 18)
# adult_cnt = adult_cnt + (anton_age >= 18)

# adult_cnt += (bob_age >= ADULT_AGE)
# adult_cnt += (ann_age >= ADULT_AGE)
# adult_cnt += (bill_age >= ADULT_AGE)
# adult_cnt += (anton_age >= ADULT_AGE)


def is_adult(age: int) -> bool:
    """Check if age is adult"""
    return age >= ADULT_AGE


adult_cnt += is_adult(bob_age)
adult_cnt += is_adult(ann_age)
adult_cnt += is_adult(bill_age)
adult_cnt += is_adult(anton_age)



print("Adult count:", adult_cnt)
print(is_adult.__doc__)
print(help(is_adult))