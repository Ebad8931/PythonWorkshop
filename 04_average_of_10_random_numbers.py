from statistics import mean as avg
import random as r

numbers = []
for _ in range(10):
    numbers.append(r.randint(1, 50))

print(numbers)
print(avg(numbers))
