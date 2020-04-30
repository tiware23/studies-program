#!/usr/bin/env python3
vowels = ['a', 'e', 'i', 'o', 'u']
word = input("Provide a word to search for vowels: ")
found = {}

# Book's Version
for letter in word:
    if letter in vowels:
       found.setdefault(letter, 0) 
       found[letter] += 1
for k, v in found.items():
    print(k, 'was found', v, 'times(s).')