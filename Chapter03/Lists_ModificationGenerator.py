#!/usr/bin/env python

import string

def caesar(letter, shift):
    letter = letter.upper()
    
    plain_idx = string.ascii_uppercase.index(letter)
    cipher_idx = (plain_idx + shift) % len(string.ascii_uppercase)
    
    cipher_letter = string.ascii_uppercase[cipher_idx]
    
    return cipher_letter


# Text to be en/decrypted
plain_text = "Hello, world!"

# To decrypt simple negate the shift
cipher_shift = 4

# Replace each char with cipher char, exclude non ASCII letters
cipher = [caesar(char, cipher_shift) for char in plain_text if char in string.ascii_letters]

# Create a string from the list of chars
print "".join(cipher)
