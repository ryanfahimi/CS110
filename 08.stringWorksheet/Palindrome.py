s = input("Please enter a string: ")
s_reversed = s[::-1]
print(f"the string backward: {s_reversed}")
if s == s_reversed:
    print("The string is a palindrome")