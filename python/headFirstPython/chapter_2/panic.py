#!/usr/bin/env python3

phrase = "Don't panic!"
plist = list(phrase)
print(phrase)
print(plist)

# My version
# phrase = "on tap"
# plist = []
# for letter in phrase:
#     plist.append(letter)

# Book's version
for i in range(4):
    plist.pop()
plist.pop(0)
plist.remove("'")
plist.extend([plist.pop(), plist.pop()])
plist.insert(2, plist.pop(3))

new_phrase = ''.join(plist) # Convert varible from list to string.
print(plist)
print(new_phrase)