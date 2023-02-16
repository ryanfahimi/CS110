s1 = input("Enter string: ")
s2 = input("Enter second string: ")
loop_counter = 0
match_counter = 0
for ch in s1:
    if ch == s2[loop_counter]:
        match_counter += 1
    loop_counter += 1
print(match_counter)