"""
Assume s is a string of lower case characters.

Write a program that prints the longest substring of s in which the letters occur in alphabetical order. For example, if s = 'azcbobobegghakl', then your program should print

Longest substring in alphabetical order is: beggh
In the case of ties, print the first substring. For example, if s = 'abcbcd', then your program should print

Longest substring in alphabetical order is: abc
Note: This problem may be challenging. We encourage you to work smart. If you've spent more than a few hours on this problem, we suggest that you move on to a different part of the course. If you have time, come back to this problem after you've had a break and cleared your head.
"""

s = 'azcbobobegghakl'
max_sub_str = ''
for i, char in enumerate(s[:-1]):
    j = i+1  # Initiate counter
    sub_str = char  # Initiate loop variable
    while s[j] >= s[j-1]:
        sub_str += s[j]
        j += 1
        if j == len(s):
            break
    if len(sub_str) > len(max_sub_str):
        max_sub_str = sub_str
print(f'Longest substring in alphabetical order is: {max_sub_str}')


