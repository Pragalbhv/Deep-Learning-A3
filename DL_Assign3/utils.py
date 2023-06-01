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
        
def encode_word(word,alphabet_to_index,encoder=encode()):
    max_len=30
    word='<'+word+'>'
    
    while len(word)<30:
        word+='.'
    
    
    
    word_encode=[]
    for letter in word:
        word_encode.append(encoder(letter,alphabet_to_index))
    
    return word_encode

def get_alphabet_from_encode(one_hot_vector_or_index, index_to_alphabet, do_onehot=True):
    
    
    if do_onehot:
        one_hot_vector_or_index=list(one_hot_vector_or_index)
        
        index = one_hot_vector_or_index.index(1)
        
    else:
        index = one_hot_vector_or_index
    
    try:
        alphabet = index_to_alphabet[index]
        return alphabet
    except:
        alphabet=' '
        return alphabet

def word_from_vecs(vecs,index_to_alphabet, do_onehot=True):
    
    
    word=[]
    starter=get_alphabet_from_encode(vecs[0],index_to_alphabet, do_onehot)
    if starter!='<':
        print("Invalid Word")
        word.append('$')
        word.append(starter)
    else:
        for ij in range(1,len(vecs)):
            aphab=get_alphabet_from_encode(vecs[ij],index_to_alphabet, do_onehot)
            if aphab=='>':
                return ''.join(word)
            word.append(aphab)
        return ''.join(word)

            
    