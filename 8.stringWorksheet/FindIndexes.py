s = input("Please enter a string: ")
lost_chr = input("Please enter the symbol to count: ")
counter = 0
for ch in s:
    if ch == lost_chr:
        print(f"{lost_chr} found at index {counter}")
    counter += 1