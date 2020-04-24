#!/usr/bin/env python3

phrase = "Don't panic!"
plist = list(phrase)
print(phrase)
print(plist)

# My version
# new_list = []

# new_list.extend(plist[1:3])
# new_list.extend(plist[5])
# new_list.extend(plist[4])
# new_list.extend(plist[7])
# new_list.extend(plist[6])

# plist = new_list

# new_phrase = ''.join(plist) # Convert varible from list to string.

# Book's Version

new_phrase = ''.join(plist[1:3])
new_phrase = new_phrase + ''.join([plist[5], plist[4], plist[7], plist[6]])
print(plist)
print(new_phrase)