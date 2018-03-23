sentence = 'The quick brown fox jumped'

# change all letters to uppercase
.upper()

sentence.upper() # => does not alter the string stored inside the variable
print(sentence) # => The quick brown fox jumped

print(sentence.upper()) # => THE QUICK BROWN FOX JUMPED

sentence_two = sentence.upper()

print(sentence_two) # => THE QUICK BROWN FOX JUMPED

sentence = 'the quick brown fox jumped'.capitalize()
print(sentence) # => 'The quick brown fox jumped'

sentence = 'the quick brown fox jumped'.title()
print(sentence) # => The Quick Brown Fox Jumped

sentence = 'THE QUICK BROWN FOX JUMPED'.lower()
print(sentence) # => the quick brown fox jumped

