s = input("Please enter a string: ")
i = int(input("Enter the index of the character you want to substitute: "))
s = s[:i] + 'x' + s[i+1:]
print(s)