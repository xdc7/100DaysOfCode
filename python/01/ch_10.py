"""
An alternade is a word in which its letters, taken alternatively in a strict sequence, and used in the same order as the original word, make up at least two other words. All letters must be used, but the smaller words are not necessarily of the same length. For example, a word with seven letters where every second letter is used will produce a four-letter word and a three-letter word. Here are two examples:
"board": makes "bad" and "or".
"waists": makes "wit" and "ass".

Using the word list at http://www.puzzlers.org/pub/wordlists/unixdict.txt, write a program that goes through each word in the list and tries to make two smaller words using every second letter. The smaller words must also be members of the list. Print the words to the screen in the above fashion.
"""


import requests
# Using the requets.get method to download the text file
response = requests.get('http://www.puzzlers.org/pub/wordlists/unixdict.txt')

# Calling .text on the response object and then calling the split() method on the string to create a list of words
word_list = response.text.split()

# Opening a file to write the results
results_file = open('2_plus_letter_alternades', 'w')

# Iterating over all the words in the list
for word in word_list:
    alternade_list = []
    odd_word = ""
    even_word = ""
    # Iterating over the length of each word and concatenating the odd and even lettered letters to form 2 words from odd and even numbered letters
    for i in range(0, (len(word))):
        if i % 2 == 0:
            even_word += word[i]
        else:
            odd_word += word[i]
    # Checking if both the odd and even lettered words exist in the original words list and whether their length is greater than 2
    if odd_word in word_list and even_word in word_list and len(odd_word) >= 2 and len(even_word) >= 2:
        # Creating a formatted string to hold matched odd and even words from the list
        results = "Alternades for {0}: {1} {2}\n".format(word, even_word, odd_word)
        # Writing the formatted string to the results file
        results_file.write(results)
# Closing the results file
results_file.close()
