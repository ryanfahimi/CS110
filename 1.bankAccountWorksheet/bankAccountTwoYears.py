balance = 3000

interestRate = .1

interestYear1 = interestRate*balance

balanceYear1 = balance + interestYear1

interestYear2 = interestRate * balanceYear1

balanceYear2 =  balanceYear1 + interestYear2

print(f'Balance after one year is: {balanceYear1}\nBalance after two years is: {balanceYear2}')
