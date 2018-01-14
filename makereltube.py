# Learning Python...
# 
# Script to compare a dictionary list to a second list of words, to find words the letters of which appear in all but one of the words in the second list.
# e.g. There is only one station on the London Tube network whose name does not contain any of the letters from the word Mackeral.
#
#

f = open('words.txt', 'r')
dictionary = f.read().splitlines()
f.close()

f = open('trainStations.txt', 'r')
wordSet = f.read().splitlines()
f.close()

f = open('results.txt', 'wa+')
f.close()

results = []

# For each word in the dictionary, check to see if any words in the word set contain no letters from that dictionary word

def checkLetterInWord(letter,word):
    print ("Checking letter: "+letter)
    print ("in Word: "+word)
    countOfLetter = word.count(letter)
    print (countOfLetter)
    return countOfLetter
    
def checkDictWordInWordset(dictWord,wordSet):
    print ("Checking letters from: "+dictWord)
    letters = set(dictWord.lower())
    print (letters)
    wordSetHits = []
    for word in wordSet:
        print ("in Word: "+word)
        totalCount = 0
        for letter in letters:
            totalCount += checkLetterInWord(letter,word.lower())
        print (str(totalCount)+" letters matched from "+dictWord+" in "+word)
    
        if totalCount == 0:
            wordSetHits.append(dictWord+","+word)

    return wordSetHits
        
    

for dictWord in dictionary:
    print("Testing:")
    print(dictWord)
    
    resultsForDictWord = checkDictWordInWordset(dictWord,wordSet)
    
    if len(resultsForDictWord) > 0:
        print ("Returned a hit "+str(resultsForDictWord))
        for thisResult in resultsForDictWord:
            results.append(thisResult)
            f = open('results.txt', 'a')
            f.write(thisResult)
            f.close()

        
            
print (results)

    
    
    
    