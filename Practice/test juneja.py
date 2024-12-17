# Find all the prime numbers greater than (and including) a given number(m) and less than (and including) a second number(n).
# Input
# The input begins with the number t of test cases in a single line (t<=10). In each of the next t lines there are two numbers m and n (1 <= m <= n <= 1000000000, n-m<=100000) separated by a space.
# Output
# Output
# For every test case print all prime numbers (ascending order) p such that m <= p <= n, one number per line, test cases outputs are separated by an empty line. (see sample input/output)
# If there are no prime numbers, print 'none' without quotes.
# Code evaluation is based on output, please do NOT print anything else.
# Sample Input
# 2
# 1 10
# 3 5
# I
# Sample Output
# 2
# 3
# 5
# 7


import fileinput

inputData = ''

for line in fileinput.input():
    inputData += line

def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def find_primes(m, n):
    primes = []
    for num in range(m, n + 1):
        if is_prime(num):
            primes.append(num)
    return primes

def code_here():
    input_lines = inputData.strip().split('\n')
    t = int(input_lines[0])
    results = []
    for i in range(1, t + 1):
        m, n = map(int, input_lines[i].split())
        primes = find_primes(m, n)
        if primes:
            results.extend(primes)
        else:
            results.append('none')
        if i < t:
            results.append('')
    return '\n'.join(map(str, results))

print(code_here())

