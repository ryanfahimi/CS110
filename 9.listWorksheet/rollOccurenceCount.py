import random

total = []
for i in range(1000):
    x, y = random.randint(1, 6), random.randint(1, 6)
    total.append(x + y)

for i in range(2, 13):
    print(f"Roll of {i} occurences: {total.count(i)}")
