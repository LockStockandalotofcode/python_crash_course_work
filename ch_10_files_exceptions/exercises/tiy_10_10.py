# downloaded pride_and_prejudice.txt 
from pathlib import Path

#########
text_files = ['pride_and_prejudice.txt', 'frankenstein.txt', 'twas_the_night_before_christmas.txt']
word = 'the '
# check_word = input("Enter the word you want to check for: ")

for text_file in text_files:
    path = Path(text_file)
    try:
        content = path.read_text()
        # content = content.lower()
    except FileNotFoundError:
        print(f"The file {path} does not exist.")
    else:
        ## writing code for one file, will later enclose it in loop for all the 3 text files downloaded

        # make words from content string
        # words = content.split()
        # count = 0
        # run for loop until the length of the string to go over each word to match with 'the' or equivalently loop over words string split() returns a list of words
        # for word in words: 
        #     if word == check_word:
        #         count += 1
        word_count = content.lower().count(word)
        print(f"The file {path} has {word_count} many words resembling '{word}'.")

# ############
# from pathlib import Path

# def count_common_words(filename, word):
#     """Count how many times word appears in the text."""
#     # Note: This is a really simple approximation, and the number returned
#     #   will be higher than the actual count.
#     path = Path(filename)
#     try:
#         contents = path.read_text()
#     except FileNotFoundError:
#         pass
#     else:
#         word_count = contents.lower().count(word)
#         msg = f"'{word}' appears in {filename} about {word_count} times."
#         print(msg)

# # filename = 'alice.txt'
# # count_common_words(filename, 'the')

# count_common_words('pride_and_prejudice.txt', 'the ')
# count_common_words('frankenstein.txt', 'the ')
# count_common_words('twas_the_night_before_christmas.txt', 'the ')