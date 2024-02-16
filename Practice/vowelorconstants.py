def check_vowel_or_consonant(char):
    vowels = ['a', 'e', 'i', 'o', 'u']
    if char.lower() in vowels:
        return "Vowel"
    else:
        return "Consonant"

character = input("Enter a character : ")
result = check_vowel_or_consonant(character)
print(f"The character '{character}' is a {result}.")