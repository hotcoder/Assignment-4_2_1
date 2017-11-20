'''
Created on Nov 20, 2017

@author: z002krv
'''
'''
Python program using function concept that maps list of words into a list of integers
representing the lengths of the corresponding words.
'''


def mapWordToLegths(wordsList):
    wordsLengths = list(map(lambda word : len(word), wordsList))
    return wordsLengths
    
print(mapWordToLegths(["a","ramesh","babu","SeniorEngineer"]))