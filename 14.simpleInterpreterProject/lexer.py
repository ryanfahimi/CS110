# import external modules
import sys

# initialize global variables
index = 0
token = {"lineCounter": 0}

# getInput should open a file and read its contents into a string,
# which is returned.
def getInput():
    s = ""
    if len(sys.argv) > 1:
        with open(sys.argv[1]) as f:
            s = f.read()
    else:
        print("ERROR: Please enter a file name in the command line.")
    return s


# getNextToken gets the next token in the string of code s.
# s is the code, index is the current position
# token is a dictionary, sent in as an empty dictionary
# token's value and type keys should be set in this function (it is passed by reference)
# return value is the updated index, it should end up one past the last character
# of the token identified.
def getNextToken(s, index, token):
    if index >= len(s):
        token["type"] = "EOF"
        token["value"] = "-"
    elif s[index].isspace():
        # recursive function just to flex
        index = getNextToken(s, index + 1, token)
    elif s[index].isdigit():
        token["type"] = "INT"
        token["value"] = ""
        index = getInt(s, index, token)
    elif s[index].isalpha():
        token["type"] = "ID"
        token["value"] = ""
        index = getId(s, index, token)
    elif s[index] == "=":
        token["type"] = "ASSIGNOP"
        token["value"] = "="
        index += 1
    elif s[index] == "+":
        token["type"] = "PLUSOP"
        token["value"] = "+"
        index += 1
    else:
        token["type"] = "UNKNOWN"
        token["value"] = s[index]
        index += 1
    return index


# getInt is called by getNextToken when it finds a digit as the first
# character. getInt loops through until it finds a non-digit, and places
# all of the digits into token["value"]. It returns the updated index
def getInt(s, index, token):
    while index < len(s) and s[index].isdigit():
        token["value"] += s[index]
        index += 1
    return index


# getId is called by getNextToken when it finds a letter as the first
# character. getId loops through until it finds something that is not a letter or
# digit and thus doesn't fit into an identifier. It places
# all of the letters/digits into token["value"]. It returns the updated index
def getId(s, index, token):
    while index < len(s) and (s[index].isdigit() or s[index].isalpha()):
        token["value"] += s[index]
        index += 1
    return index


# main program
# the main should get the input, then loop through the input by repeatedly calling
# Each token type/value should be printed
if __name__ == "__main__":
    s = getInput()
    while index < len(s):
        index = getNextToken(s, index, token)
        print(token)
