#!/usr/bin/env python3

def return_palindromo(word):
    first_list = []
    second_list = []

    for i in word[:2]:
        first_list.append(i)

    for i in word[-2:]:
        second_list.append(i)

    if first_list[0] in second_list[1] and second_list[0] in first_list[1]:
        return True
    else:
        return False


words = input("Type a word: ".lower())

if return_palindromo(words) == True:
    print(f"It's a palindromo the word: {words}")
else:
    print(f'The word {words} is not a palindromo')