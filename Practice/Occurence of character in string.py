def char_count(String):
    char_dict = {}
    for char in string:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict


string = "abracadabra"
print(char_count(string))