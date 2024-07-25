# Implement a function to reverse the order of words in a given sentence.

def reverse_the_order_of_words(sentence):
    return ' '.join(sentence.split()[::-1])


print(reverse_the_order_of_words("Hello World"))