def Count(list, target):
    count = 0
    for i in list:
        if i == target:
            count = count + 1

    return count


def char_count_for_loop(String):
    char_dict = {}
    for char in string:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict


string = "abracadabra"
char_frequency = char_count_for_loop(string)
print(char_frequency)

list1 = [1, 1, 1, 2, 2, 4, 5, 6, 8, 65, 0]
target = 34

print(f"{target} has {Count(list, target)} occurrences.")
