""" Make a list with 150 random numbers, find all prime numbers from that list and print the list without duplicate prime numbers """

import random

lst, primes, dupe_removed = [], [], []

for i in range(10):
    lst.append(random.randint(1, 10))

for i in lst:
    if i == 0 or i == 1:
        continue
    for j in range(2, i // 2 + 1):
        if i % j == 0:
            break
    else:
        if i not in dupe_removed:
            dupe_removed.append(i)

print(f"Original List: {lst}\n\nPrime numbers in list: {sorted(dupe_removed)}\n") 
# the last line (f-string, f"original list...\n') may not work in older python versions, please check version in cmd using py --version or python --version