s = input("Enter string: ")
new_s =''
for ch in s:
    if ('a' <= ch <= 'z') or ('A' <= ch <= 'Z'):
        ch = chr(ord(ch) + 1)
    new_s += ch
print(new_s)