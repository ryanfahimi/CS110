def countDown(num):
    if num >= 10:
        print("blastoff")
    else:
        print(num)
        countDown(num + 1)


countDown(0)
