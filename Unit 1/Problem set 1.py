"""
Assume s is a string of lower case characters.

Write a program that counts up the number of vowels contained in the string s. Valid vowels are: 'a', 'e', 'i', 'o', and
 'u'. For example, if s = 'azcbobobegghakl', your program should print:

Number of vowels: 5
"""

s = 'azcbobobegghakl'  # Given test case

n_vowels = 0  # Initialize loop variable
vowels_list = ['a', 'e', 'i', 'o', 'u']  # List of vowels
for char in s:
    if char in vowels_list:
        n_vowels += 1
    else:
        continue
print('Number of vowels:', n_vowels)