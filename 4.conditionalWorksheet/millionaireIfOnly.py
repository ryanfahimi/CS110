balanceStr=input('please enter the balance:')
balance=int(balanceStr)
rateStr=input('enter the rate as a pct:')
rate=float(rateStr)/100
interest=balance*rate
balance=balance+interest
interest=balance*rate
balance=balance+interest
print("balance after year 2: $"+str(balance))
if balance >= 2000000:
    print("You're a multimillionaire")
if 1000000 <= balance < 2000000:
    print("You're a millionaire")
if balance < 1000000:
    print("You're broke")