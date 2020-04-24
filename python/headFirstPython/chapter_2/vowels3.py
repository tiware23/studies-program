#!/usr/bin/env python3
vowels = ['a', 'e', 'i', 'o', 'u']
word = input("Provide a word to search for vowels: ")
found = []

# My version
# for letter in word:
#    if letter in vowels and letter not in found:
#       found.append(letter)
# for f in found:
#    print(f"Letter found: {f}")

# Book's Version
for letter in word:
    if letter in vowels:
       if letter not in found:
           found.append(letter)
for vowel in found:
    print(vowel)