balanceStr = input("please enter the initial balance: ")

balance = int(balanceStr)

interestRateStr = input("enter the interest rate as a pct: ")

interestRate = float(interestRateStr) / 100

interest = interestRate * balance

balanceYear1 = balance + interest

interest = interestRate * balanceYear1

balanceYear2 = balanceYear1 + interest

print(
    f"Balance after one year is: {balanceYear1}\nBalance after two years is: {balanceYear2}"
)
