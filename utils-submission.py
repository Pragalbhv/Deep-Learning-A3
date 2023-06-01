import numpy as np


####################

def encode(do_onehot=True):
    'returns encoder function'
    def one_hot_encode_alphabet(alphabet,alphabet_to_index):
    
        # Initialize a zero vector of length equal to the number of alphabets plus one for unseen alphabets
        one_hot_vector = [0] * (len(alphabet_to_index) + 1)
        # Set the indices of the alphabets present in the sentence to 1

        if alphabet.lower() in alphabet_to_index:
            one_hot_vector[alphabet_to_index[alphabet.lower()]] = 1
        else:
            # Set the last index to 1 to represent any unseen alphabets
            one_hot_vector[-1] = 1
        return one_hot_vector
    def simple(alphabet,alphabet_to_index):
        try:
            return alphabet_to_index[alphabet.lower()]
        except:
            return len(alphabet_to_index)
    
    
    if do_onehot:
        return one_hot_encode_alphabet
    else:
        return simple
    
        
def encode_word(word, alphabet_to_index, encoder=encode()):
    max_len = 30  # Maximum length of the encoded word
    word = '<' + word + '>'  # Add start and end symbols to the word

    while len(word) < max_len:
        word += '.'  # Pad the word with '.' to reach the maximum length of 30 characters

    word_encode = []  # List to store the encoded characters of the word
    for letter in word:
        word_encode.append(encoder(letter, alphabet_to_index))  # Encode each character using the provided encoder

    return word_encode  # Return the encoded word as a list of encoded characters


#gets alpahet from encoding
def get_alphabet_from_encode(one_hot_vector_or_index, index_to_alphabet, do_onehot=True):
    if do_onehot:
        one_hot_vector_or_index = list(one_hot_vector_or_index)  # Convert the input to a list

        index = one_hot_vector_or_index.index(1)  # Find the index of the one-hot encoded character
        
    else:
        index = one_hot_vector_or_index  # Use the input directly as the index

    try:
        alphabet = index_to_alphabet[index]  # Retrieve the corresponding alphabet using the index
        return alphabet
    except:
        alphabet = ' '  # Return a space character if the index is not found in the index_to_alphabet dictionary
        return alphabet


def word_from_vecs(vecs, index_to_alphabet, do_onehot=True):
    word = []  # List to store the characters of the word
    starter = get_alphabet_from_encode(vecs[0], index_to_alphabet, do_onehot)  # Get the first character of the word

    if starter != '<':
        print("Invalid Word")  # Print an error message if the word doesn't start with '<'
        word.append('$')  # Add a special character ('$') to the word list
        word.append(starter)  # Add the starter character to the word list
    else:
        for ij in range(1, len(vecs)):
            aphab = get_alphabet_from_encode(vecs[ij], index_to_alphabet, do_onehot)  # Get each character of the word
            if aphab == '>':
                return ''.join(word)  # If the character is '>', return the word as a string
            word.append(aphab)  # Add the character to the word list

        return ''.join(word)  # Return the word as a string by joining the characters



            
    