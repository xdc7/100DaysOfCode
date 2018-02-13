"""implement a print_words(filename) function that counts
how often each word appears in the text and prints:
word1 count1
word2 count2
...

Print the above list in order sorted by word (python will sort punctuation to
come before letters -- that's fine). Store all the words as lowercase,
so 'The' and 'the' count as the same word."""

import re

def print_words(text):
    word_regex = re.compile(r'([\(\!]*)([a-zA-Z\']+)([\)\!]*)')
    counts = {}
    text = text.lower().split()
    result_tup_list = []
    result = ["----------\nWord Count\n----------"]
    for word in text:
        #print (word)
        match = word_regex.search(word)
        
        if match:
            #print (match.group(2))
            counts[match.group(2)] = counts.get(match.group(2) , 0) + 1
    for k, v in counts.items():
        result_tup_list.append((k,v))

    for tup in sorted(result_tup_list):
        result.append("{0} {1}".format(tup[0], tup[1]))
    return result



text1 = "Print the above list in order sorted by word (python will sort punctuation to come before letters! -- that's fine). Store all the words as lowercase and love the letters toto"
wc = print_words(text1)
for item in wc:
    print(item)