"""Generate Markov text from text files."""

import random


def open_and_read_file(file_path_1, file_path_2):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    contents_1 = open(file_path_1).read()
    contents_1 = contents_1.rstrip().replace('\n',' ')
    
    contents_2 = open(file_path_2).read()
    contents_2 = contents_2.rstrip().replace('\n',' ').replace('  ', ' ')

    cleaned_contents = contents_1 + " " + contents_2
    return cleaned_contents

# text_string = open_and_read_file('green-eggs.txt')

def make_chains(text_string, n):
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

    # for i in range(0, len(list_text) - n):
    #     if (list_text[i], list_text[i + 1]) not in chains:
    #         chains[(list_text[i], list_text[i + 1])] = [list_text[i + 2]]
    #     else:
    #         chains[(list_text[i], list_text[i + 1])].append(list_text[i + 2])
    
    for i in range(0, len(list_text) - n):
        elements_to_add_to_tuple = list_text[i:n+i]
        key = tuple(elements_to_add_to_tuple)

        if key not in chains:
            chains[key] = [list_text[i + n]]
        else:
            chains[key].append(list_text[i + n])

    
    return chains


# chains = make_chains(text_string,3)
# print(chains)

def make_text(chains, n):
    """Return text from chains."""

    words = []

    # current_key = random.choice(list(chains.keys()))
    while True:
        first_key = random.choice(list(chains.keys()))

        if first_key[0][0] in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            current_key = first_key
            break


    for word in current_key:
        words.append(word)
    
    while True:
        current_key = tuple(words[-n:])

        if current_key not in chains.keys():
            break
        else:
            random_word = random.choice(list(chains[current_key])) 
            words.append(random_word)
            
    reversed_words = words[::-1]

    i = 0
    for word in reversed_words:
        if word[-1] in ".?!":
            break
        else:
            i += 1

    return ' '.join(words[:len(words) - i])

# print(make_text(chains, 3))

input_path_1 = 'green-eggs.txt'
input_path_2 = 'gettysburg.txt'

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path_1, input_path_2)

# Get a Markov chain
chains = make_chains(input_text, 2)

# Produce random text
random_text = make_text(chains, 2)

print(random_text)
