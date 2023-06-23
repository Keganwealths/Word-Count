import os
# asking for user input
search_word_count = input('Enter the word(s), separated by a comma: ')

# split the input string into a list of words
search_words = search_word_count.split(',')

# opening text file in read only mode
file = open(r"C:\Users\User\Downloads\datascience.txt")

# reading data of the file
read_data = file.read()

# converting data in lower case and the counting the occurrence
for word in search_words: 
    word_count = read_data.lower().count(word.strip())

    # printing word and it's count
    print(f"The word '{word.strip()}' appeared {word_count} times.")
