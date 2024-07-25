# Implement a function to find the first non-repeating character in a string.

def first_non_repeating_char(s):
    char_count = {}
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    for char in s:
        if char_count[char] == 1:
            return char
    return

# Test cases
print(first_non_repeating_char('aabbcc')) # None
print(first_non_repeating_char('abbcd')) # c