#!/usr/bin/env python3

paranoid_android = "Marvin"
letters = list(paranoid_android)

for char in letters[:6]:
    print('\t' * 2, char)
print()
for char in letters[-7:]:
    print('\t' * 3, char)
print()
for char in letters[12:20]:
    print('\t' * 4, char)