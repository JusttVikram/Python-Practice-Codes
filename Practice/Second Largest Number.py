def find_second_largest(numbers):
    largest = float('-inf')
    second_largest = float('-inf')
    
    for num in List:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num
    
    return second_largest


List = [10, 5, 8, 20, 15]
second_largest = find_second_largest(List)
print("The second largest number is:", second_largest)