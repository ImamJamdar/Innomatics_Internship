# Problem 1: Unique words in a sentence

# Given sentence
sentence = "python is easy and python is powerful"

# split the sentence into words1
words = sentence.split()

# convert the list of words to a set to get unique words
unique_words = set(words)

# print the count of unique words
print("Number of unique words:", len(unique_words))

# print the unique words in the sentence
print("Unique words in the sentence:", unique_words)