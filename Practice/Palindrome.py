def is_palindrome(text):
    return text == text[::-1]

print(is_palindrome("racecar"))  # True
print(is_palindrome("hello"))    # False