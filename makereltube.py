# Learning Python...
# 
# Script to compare a dictionary list to a second list of words, to find words the letters of which appear in all but one of the words in the second list.
# e.g. There is only one station on the London Tube network whose name does not contain any of the letters from the word Mackeral.
#
#

f = open('dictionary.txt', 'r')
dictionary = f.read().splitlines()

f = open('wordSet.txt', 'r')
wordSet = f.read().splitlines()

for dictWord in dictionary:
    print("Testing:")
    print(dictWord)
    letters = list(dictWord)
    
    remainingWords = wordSet
    
    for letter in letters:
        print(letter)

        # Take second list array. For each letter in the dictionary word, remove words from the second list that contain that letter.
        
        # If array contains only one entry, we have a winner.
        
        remainingWords = filter(lambda listWord: letter not in listWord, remainingWords)
        
        print(remainingWords)
        print(len(remainingWords))

print("")
