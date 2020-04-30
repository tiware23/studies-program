#!/usr/bin/env python3
vowels = set('aeiou')
word = input("Provide a word to search for vowels: ")

found = vowels.intersection(set(word))
for vowel in found:
    print(vowel)


# for letter in word:
#     if letter in vowels:
#        if letter not in found:
#            found.append(letter)
# for vowel in found:
#     print(vowel)