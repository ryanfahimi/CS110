import random
addend_list = []
total = 0
equation_str = ''
counter = 0

# loop and add 2-4 numbers
equation_len = random.randint(2,4)
for _ in range(equation_len):
    addend = random.randrange(0,100)
    total += addend
    addend_list.append(str(addend))

for i, addend in enumerate(addend_list):
    if i != 0:
        equation_str += ' + '
    equation_str += addend

print(f'Total: {total}')
print(equation_str)

guess = int(input("Please enter your guess for the sum: "))
if guess == total:
    print("Congratulations, you got it!")
else:
    print("Better luck next time champ.")
