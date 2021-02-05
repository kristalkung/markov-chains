"""Generate Markov text from text files."""

import random


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    contents = open(file_path).read()
    cleaned_contents = contents.rstrip().replace('\n',' ')
    return cleaned_contents

text_string = open_and_read_file('green-eggs.txt')

def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains('hi there mary hi there juanita')

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}

    list_text = text_string.split(" ")

    for i in range(0, len(list_text) - 2):
        if (list_text[i], list_text[i + 1]) not in chains:
            chains[(list_text[i], list_text[i + 1])] = [list_text[i + 2]]
        else:
            chains[(list_text[i], list_text[i + 1])].append(list_text[i + 2])

    return chains


chains = make_chains(text_string)

def make_text(chains):
    """Return text from chains."""

    words = []

    current_key = random.choice(list(chains.keys()))
    # need to put current_key into words

    random_word = random.choice(list(chains[current_key]))    
    
    for word in chains[current_key]: # chains[current_key] is value of the key, but that is a list that can multiple items.  
        words.append(word)
    
    # put random_word into words
    # change current key to the last two words of words
    # loop again, but only add the new random_word
    # loop ends when the key doesn't exist
    # return joined words


    print(current_key)
    print(chains[current_key])
    
    # your code goes here

    return ' '.join(words)

print(make_text(chains))

# input_path = 'green-eggs.txt'

# # Open the file and turn it into one long string
# input_text = open_and_read_file(input_path)

# # Get a Markov chain
# chains = make_chains(input_text)

# # Produce random text
# random_text = make_text(chains)

# print(random_text)
