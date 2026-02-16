# Problem 7: count character frequency

# test text
text = "hello world"

# Empty dictionary to store character counts
char_frequency = {}

# loop through each character in the text string
for char in text:
    if char in char_frequency:
        char_frequency[char] += 1
    else:
        char_frequency[char] = 1

# print the final character frequency dictionary
print("Character frequency:", char_frequency)