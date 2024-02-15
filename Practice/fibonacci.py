def fibonacci_series(n):

    if n < 0:
        print("Please enter a non-negative integer.")
        return

    a, b = 0, 1
    print(a, b, end=" ")  # Print the first two terms separately

    for i in range(2, n):
        c = a + b
        print(c, end=" ")
        a, b = b, c  # Update values for the next iteration

n = int(input("Enter the number of terms: "))

fibonacci_series(n)
