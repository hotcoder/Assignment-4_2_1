'''
Created on Nov 20, 2017

@author: z002krv
'''
'''
Python program using function concept that maps list of words into a list of integers
representing the lengths of the corresponding words.
'''

wordsList  = ["ab","cde","erty"]

wordsLengths = list(map(lambda word : len(word), wordsList))
    
print(wordsLengths)