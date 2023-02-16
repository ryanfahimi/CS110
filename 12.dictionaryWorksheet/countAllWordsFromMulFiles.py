import sys

f_list = []
for i in range(1, len(sys.argv)):
    fname = sys.argv[i]
    f = open(fname)
    s = f.read()
    f_list.append(s)
    f.close()

wordCount = {}


def countAllWords(f_list, wordCount):
    for s in f_list:
        words = s.split()
        for w in words:
            if w not in wordCount:
                wordCount[w] = 0
            wordCount[w] += 1


countAllWords(f_list, wordCount)
print(wordCount)
