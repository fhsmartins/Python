"""
Author: fhsmartins
"""

def reverse_words_order_and_swap_cases(sentence):
     words = sentence.split()

     words = list(reversed(words))
    
     j = " ".join(words)

     return j.swapcase()
