# Learning Python...
# 
# Script to compare a dictionary list to a second list of words, to find words the letters of which appear in all but one of the words in the second list.
# e.g. There is only one station on the London Tube network whose name does not contain any of the letters from the word Mackeral.
#
#

f = open('words.txt', 'r')
dictionary = f.read().splitlines()

f = open('wordSet.txt', 'r')
wordSet = f.read().splitlines()

results = []

for dictWord in dictionary:
    print("Testing:")
    print(dictWord)
    letters = list(dictWord)
    
    def checkLetters(dictWord,wordSet):
        """
        How many words in the array wordSet contain none of the letters in the dictWord parameter?
        """
        print('Checking '+dictWord)
        
        wordSetNotMatches = []
        
        for word in wordSet:
            matches = 0
            print(word)
            for letter in dictWord:
                if word.lower().count(letter.lower()) > 0:
                    print (letter+' is in '+word)
                    matches += 1
                else:
                    print (letter+' is not in '+word)
            print('Number of matches of '+dictWord+' in '+word+': '+str(matches))
            if matches == 0:
                wordSetNotMatches.append(word)
            
        print('Checked '+dictWord+'. Words in word set that contain no letters from '+dictWord+': ')
        print(len(wordSetNotMatches))
        return wordSetNotMatches
            
    
    notMatches = checkLetters(dictWord,wordSet)
    print('')
    if len(notMatches) == 1:
        print('Found exactly one word in word set that contains no letters from the word '+dictWord)
        results.append(dictWord)
    else:
        print('Found '+str(len(notMatches))+' words in word set that contain no letters from: '+dictWord)
    print('')

print("")
print("Words whose letters only appear in one memeber of the word set:")
print(results)
