# script to clean dictionary of words containing non-alphabet symbols

f = open('words.txt', 'r')
dictionary = f.read().splitlines()
f.close()

cleanDictionary = []

for word in dictionary:
    if word.isalpha():
        #print(word)
        #print('contains only alphabet chars')
        cleanDictionary.append(word+"\n")

f = open('testCleanDict.txt', 'w')
f.writelines(cleanDictionary)
f.close()

print(cleanDictionary)

