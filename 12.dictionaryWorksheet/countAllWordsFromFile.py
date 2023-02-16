import sys

fname = sys.argv[1]
f = open(fname)
s = f.read()
f.close()
wordCount = {}


def countAllWords(s, wordCount):
    words = s.split()
    for w in words:
        if w not in wordCount:
            wordCount[w] = 0
        wordCount[w] += 1


countAllWords(s, wordCount)
print(wordCount)
