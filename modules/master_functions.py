'''
master_functions.py
Library of commonly used functions for the clinical abbreviation expander
'''

import string

# Function to normalize short form abbreviations
def normalized_short_form(sf):
    # Converts text to uppercase
    sf = sf.upper()
    # Removes leading and trailing whitespace
    sf = sf.strip()
    # Removes punctuation
    sf = sf.translate(maketrans('', '', string.punctuation))
    return sf