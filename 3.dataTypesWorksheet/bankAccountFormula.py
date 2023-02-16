P = int(input('Please enter the balance of your bank account: '))
r = float(input("Please enter the interest rate of your bank account as a percentage: "))/100
t = float(input("Please enter the number of years over which you would like to simulate your bank account balance: "))
n = int(input("Please enter the number of compounding periods per year:"))

A = P * (1 + r/n) ** (n*t)

print (f'Balance after {t} years is: {A:.2f}')