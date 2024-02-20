def calculate_sum(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

# Example usages
numbers = [1, 2, 3, 4, 5]
print(calculate_sum(numbers))  # Output: 15

numbers = [10, 20, 30, 40, 50]
print(calculate_sum(numbers))  # Output: 150

numbers = [-1, -2, -3, -4, -5]
print(calculate_sum(numbers))  # Output: -15