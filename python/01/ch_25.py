"""
spinWords( "Hey fellow warriors" ) => returns "Hey wollef sroirraw" 
spinWords( "This is a test") => returns "This is a test" 
spinWords( "This is another test" )=> returns "This is rehtona test"
"""

def spin_words(sentence):
    # Your code goes here
    result = []
    sl = sentence.split()
    for word in sl:
      if len(word) >= 5:
        word = word[::-1]
      result.append(word)
      
    return " ".join(result)
    

print (spin_words( "Hey fellow warriors" ))
print (spin_words( "This is a test" ))
print (spin_words( "This is another test" ))