# Implement a function to check if a given number is a power of two.

def power_of_two(n):
    if n == 0:
        return False
    while n % 2 == 0:
        n = n / 2
    return n == 1

# Test cases

print(power_of_two(21)) # False
print(power_of_two(1)) # True