# Given a string S, write a program to count the occurrence of Lowercase characters, Uppercase characters, Special characters and Numeric values in the string.
# Note: There are no white spaces in the string.

def count(self,s):
    lower,upper,special,digit = 0,0,0,0
    for i in s:
        if i.islower():
            lower += 1
        elif i.isupper():
            upper += 1
        elif i.isdigit():
            digit += 1
        else:
            special += 1
    return [upper,lower,digit,special]