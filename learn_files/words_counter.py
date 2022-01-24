from pprint import pprint

file = open('input.txt', 'r')

lines = file.readlines()

counter = {}
total_cnt = 0

for line in lines:
    words = line.split()

    total_cnt += len(words)
    for word in words:
        counter[word] = counter.setdefault(word, 0) + 1
        # if word not in counter:
        #     counter[word] = 1
        # else:
        #     counter[word] += 1

print(f'File contains {total_cnt} words')
print(f'Words statistic:')
pprint(counter)