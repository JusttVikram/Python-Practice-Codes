def find_median(numbers):
    sorted_numbers = sorted(numbers)
    length = len(sorted_numbers)
    middle_index = length // 2

    if length % 2 == 0:
        median = (sorted_numbers[middle_index - 1] + sorted_numbers[middle_index]) / 2
    else:
        median = sorted_numbers[middle_index]

    return median

# Example usage
numbers = [5, 2, 9, 1, 7]
median = find_median(numbers)
print("Median:", median)