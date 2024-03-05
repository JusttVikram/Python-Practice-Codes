# WAP to remove all vowels from a string

def remove_vowels_from_string(string):
    vowels = 'aeiou'
    string_lower = string.lower()
    i = 0
    for char in string_lower:
        if char in vowels:
            continue
        print(char)
        i += 1

result = remove_vowels_from_string('Hello')
print(result)