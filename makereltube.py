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

results = []

# For each word in the dictionary, check to see if any words in the word set contain no letters from that dictionary word

def checkLetter(letter,word):
    print ("Checking letter: "+letter)
    print ("in Word: "+word)
    countOfLetter = word.count(letter)
    print (countOfLetter)
    return countOfLetter
    

for dictWord in dictionary:
    print("Testing:")
    print(dictWord)
    letters = set(dictWord)
    
    print (letters)
    
    for word in wordSet:
        totalCount = 0
        for letter in letters:
            totalCount += checkLetter(letter,word.lower())
        print (str(totalCount)+" letters matched from "+dictWord+" in "+word)
    
        if totalCount == 0:
            results.append(dictWord+","+word)
            
print (results)

    
    
    
    