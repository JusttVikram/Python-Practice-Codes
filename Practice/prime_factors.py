# Write a program to find the prime factors of a given number.

def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

# Test cases

print(prime_factors(315)) # [3, 3, 5, 7]