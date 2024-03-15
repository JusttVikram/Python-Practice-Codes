def Count(list, target):
    count = 0
    for i in list:
        if i == target:
            count = count + 1

    return count


list1 = [1, 1, 1, 2, 2, 4, 5, 6, 8, 65, 0]
target = 34

print(f"{target} has {Count(list1, target)} occurrences.")
