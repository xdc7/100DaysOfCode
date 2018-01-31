"""
An alternade is a word in which its letters, taken alternatively in a strict sequence, and used in the same order as the original word, make up at least two other words. All letters must be used, but the smaller words are not necessarily of the same length. For example, a word with seven letters where every second letter is used will produce a four-letter word and a three-letter word. Here are two examples:
"board": makes "bad" and "or".
"waists": makes "wit" and "ass".

Using the word list at http://www.puzzlers.org/pub/wordlists/unixdict.txt, write a program that goes through each word in the list and tries to make two smaller words using every second letter. The smaller words must also be members of the list. Print the words to the screen in the above fashion.
"""


import requests
response = requests.get('http://www.puzzlers.org/pub/wordlists/unixdict.txt')

word_list = response.text.split()
results_file = open('2_plus_letter_alternades', 'w')
for word in word_list:
    alternade_list = []
    odd_word = ""
    even_word = ""
    # for i in range(0,(len(word) - 1), 2):
    for i in range(0,(len(word))):
        if i % 2 == 0:
            even_word += word[i]
        else:
            odd_word += word[i]
    
    if odd_word in word_list and even_word in word_list and len(odd_word) >= 2 and len(even_word) >= 2:
        results = "Alternades for {0}: {1} {2}\n".format(word, even_word, odd_word)
        results_file.write(results)
        # print ("Alternades for %s: %s %s" % (word, even_word, odd_word))
        #print(results)
        
 #print ("\nLOWER CASE: %s \nUPPER CASE: %s" % (count_upper_lower_characters(entry)))   



results_file.close()
