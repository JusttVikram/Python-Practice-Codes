def permute(string):
    if len(string) == 0:
        return []

    if len(string) == 1:
        return [string]

    permutations = []

    for i in range(len(string)):
        
        current_char = string[i]

        remaining_chars = string[:i] + string[i+1:]
        for perm in permute(remaining_chars):
            
            permutations.append(current_char + perm)

    return permutations


input_string = input("Enter a string: ")
result = permute(input_string)
print("All permutations of the string:", result)

