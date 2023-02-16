balance=int(input('Please enter the balance: '))
years = int(input("Please enter number of years simulated: "))

for i in range(years):
    if balance >= 20000:
        rate = 0.17
    elif balance >= 10000:
        rate = 0.15
    else:
        rate = 0.1
    interest = rate*balance
    balance = balance + interest


print (f'Balance after {years} years is: {balance}')