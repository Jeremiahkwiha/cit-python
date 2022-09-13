#checking whether the string is a pangram

import string
  
letters_of_alphabet = set(string.ascii_lowercase)
  
def pangram(str):
     return not set(letters_of_alphabet) - set(str)     
string = 'The quick brown fox jumps over the lazy dog'
if(pangram(string) == True):
    print("Yes, it is a pangram")
else:
    print("No, it is not")


