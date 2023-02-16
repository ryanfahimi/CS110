from lexer import getNextToken, getInput

# initialize global vars
idTable = {}
status = {}
memory = []
index = 0


def parseId(s, index, idTable, status):
    # initialize local vars
    token = {}

    # derive next token
    index = getNextToken(s, index, token)

    # if the token is not an ID, the interpreter produces an error
    if token["type"] != "ID":
        status["error"] = "expecting identifier"

    # if the ID is not in the ID Table, it is added and the stored address is set to the current ID address
    elif token["value"] not in idTable:
        idTable[token["value"]] = len(idTable)
        status["storeAddr"] = idTable[token["value"]]

    # if the ID is in the ID Table, the stored address is set to the current ID address
    else:
        status["storeAddr"] = idTable[token["value"]]
    return index


def parseAssignOp(s, index, status):
    # initialize local vars
    token = {}

    # derive next token
    index = getNextToken(s, index, token)

    # if the token is not an assign operator, the interpreter produces an error
    if token["type"] != "ASSIGNOP":
        status["error"] = "expecting assignOp"
    return index


def parseExpr(s, index, idTable, memory, status):
    # initialize local vars
    token = {}
    evaluated = False
    solution = 0
    nextIndex = 0

    # derive next token
    index = getNextToken(s, index, token)

    # if the stored address is not yet an index in memory, a value of None is appended to the end of memory
    if len(memory) == status["storeAddr"]:
        memory.append(None)

    # the loop continues parsing the expression until it is evaluated
    while not evaluated:

        # IDs are evaluated
        if token["type"] == "ID":

            # IDs in the ID Table are evaluated
            if token["value"] in idTable:

                # if an ID is newly appended to memory, the interpreter produces an error
                if memory[idTable[token["value"]]] == None:
                    status["error"] = f"identifier '{token['value']}' not defined"
                    break

                # if an ID is already assigned, it is added to the solution
                else:
                    solution += memory[idTable[token["value"]]]

            # if an ID is not in the ID Table, the interpreter produces an error
            else:
                status["error"] = f"identifier '{token['value']}' not defined"
                break

            # check next index
            nextIndex = getNextToken(s, index, token)

        # if a token is an integer, it is added to the solution
        elif token["type"] == "INT":
            solution += int(token["value"])

            # check next index
            nextIndex = getNextToken(s, index, token)

        # if the tokens in the expression are neither IDs nor integers, the interpreter produces an error
        else:
            status["error"] = "expecting integer or identifier"
            break

        # if the token is a plus operator, the next token is derived
        if token["type"] == "PLUSOP":
            index = getNextToken(s, nextIndex, token)

        # if the token is an ID or an integer, the expression is considered evaluated
        elif token["type"] == "ID" or token["type"] == "INT":
            evaluated = True

        # if the token is an end of file, the expression is considered evaluated
        elif token["type"] == "EOF":
            index = nextIndex
            evaluated = True

        # if the token is neither a plus operator nor an ID, the interpreter produces an error
        else:
            index = nextIndex
            status["error"] = "expecting plusOp"
            break

    # solution is assigned to the stored index in memory
    memory[status["storeAddr"]] = solution
    return index


def error(s, index, status):
    # if error is in status, the function prints an error message and returns True
    if "error" in status:
        print("ERROR on line {}: {}".format(s[:index].count("\n") + 1, status["error"]))
        return True
    else:
        return False


# main
if __name__ == "__main__":
    s = getInput()
    while index < len(s):
        index = parseId(s, index, idTable, status)
        if error(s, index, status):
            break
        index = parseAssignOp(s, index, status)
        if error(s, index, status):
            break
        index = parseExpr(s, index, idTable, memory, status)
        if error(s, index, status):
            break
    if s and "error" not in status:
        print(f"ID Table: {idTable}")
        print(f"Memory: {memory}")
