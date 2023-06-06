"""
Assume s is a string of lower case characters.

Write a program that prints the number of times the string 'bob' occurs in s. For example, if s = 'azcbobobegghakl', then your program should print

Number of times bob occurs is: 2
"""

s = 'obobbobobbboobobboboboboboblbooboboobobb'  # Given test case
word = 'bob'
n_word = 0  # Initialize loop variable
for i, character in enumerate(s[:-(len(word)-1)]):
    if word == s[i:i+len(word)]:
        n_word += 1
print(f'Number of times {word} occurs is: {n_word}')