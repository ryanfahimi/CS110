import sys

fname = sys.argv[1]
f = open(fname)
s = f.read()
f.close()
wordCount = {}


def countAndThe(s, wordCount):
    words = s.split()
    wordCount["the"] = 0
    wordCount["and"] = 0
    for w in words:
        if w == "the":
            wordCount["the"] += 1
        elif w == "and":
            wordCount["and"] += 1


countAndThe(s, wordCount)
print(wordCount)
