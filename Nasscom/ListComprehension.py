numbers = [1, 2, 3, 4, 5]

# List comprehension to create a new list with squared values
squared_numbers = [num ** 2 for num in numbers]
print(squared_numbers)


#List Comprehension for filteration

Even_numbers = [i for i in range(10) if i%2==0]
print(Even_numbers)
