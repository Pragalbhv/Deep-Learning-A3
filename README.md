# Deep-Learning-A3
### By Pragalbh Vashishtha
### Dependencies

python 3.7+ Keras

In addition, install the following packages:

    numpy
    tqdm
    wandb
    matplotlib
    copy



Please find below the following files.
## utils-submission.py:
contains
- `encode` is a function that returns an encoder function based on the specified encoding mode (one-hot or simple).
- The `encode_word` function takes a word, a mapping of alphabets to indices, and an encoder function (defaulting to `encode()`) and returns the encoded representation of the word. The word is padded with dots (`.`) to a maximum length of 30, and each letter in the word is encoded using the provided encoder function and alphabet-to-index mapping. The encoded representation of the word is returned as a list.
- The `get_alphabet_from_encode` function takes a one-hot encoded vector or index, a mapping of indices to alphabets, and a flag indicating whether the encoding is one-hot or simple. If the encoding is one-hot, the function finds the index of the element with value 1 in the vector and returns the corresponding alphabet. If the encoding is simple, the function directly returns the alphabet corresponding to the index. If the alphabet is not found in the mapping, a space character is returned.
- The `word_from_vecs` function takes a sequence of encoded vectors, a mapping of indices to alphabets, and a flag indicating whether the encoding is one-hot or simple. It iterates over the encoded vectors, retrieving the corresponding alphabets using the `get_alphabet_from_encode` function. It constructs a word by appending each alphabet to a list until it encounters the end marker (`>`). The constructed word is returned as a string. If the word is invalid (i.e., does not start with `<`), error is thrown.
## Submission_Vanilla.ipynb 
Click run all to run
Does not use Attention
Contains:
- The `Encoder` class is a module for the sequence-to-sequence model. It takes an input size, embedding size, hidden size, number of layers, cell type, dropout rate, and bidirectional flag as input. The forward pass of the encoder takes an input batch of tokenized sentences and returns the hidden and cell states of the LSTM layer.

- The `Decoder` class is a module for the sequence-to-sequence model. It takes an output size, embedding size, hidden size, number of layers, cell type, dropout rate, and bidirectional flag as input. The forward pass of the decoder takes a target tensor, hidden state from the encoder's LSTM layer, and cell state from the encoder's LSTM layer. It returns the prediction tensor, hidden state of the decoder's LSTM layer, and cell state of the decoder's LSTM layer.

- The `Seq2Seq` class is the main sequence-to-sequence model that combines an encoder and decoder. It takes an encoder module, decoder module, and device as input. The forward pass of the Seq2Seq model takes source and target batches of tokenized sentences and performs the encoding and decoding steps. It returns the outputs of the decoder.
- model is saved with the name 'noattn_model.model'
- predictions saved in predictions_vanilla.txt can be loaded with: ```np.loadtxt('predictions_vanilla.txt',delimiter=',',encoding='utf-8',dtype=str)```

## Submission_Attn.ipynb 
Click run all to run
Uses Attention
Contains:
 - The `Encoder` class  It takes input parameters such as `input_size` (source vocabulary size), `embed_size` (embedding layer dimension), `enc_hid_size` (encoder hidden state size), `dec_hid_size` (decoder hidden state size), `num_layers` (number of encoder layers), `cell_mode` (type of cell: LSTM, GRU, or RNN), `dropout` (dropout rate for the encoder layer), and `is_bi` (flag indicating if the encoder is bidirectional).
 - The `forward` method of the `Encoder` class performs the forward pass of the encoder. It takes an input batch of tokenized source sentences and returns the outputs of the LSTM layer, the last hidden state of the LSTM layer, and the last cell state of the LSTM layer (only for LSTM cell mode).
 - The `Attention` class represents the attention module of the Seq2Seq model. It takes input parameters `enc_hid_dim` (encoder hidden state size), `dec_hid_dim` (decoder hidden state size), and `is_bi` (flag indicating if the encoder is bidirectional).
 - The `forward` method of the `Attention` class performs the forward pass of the attention module. It takes encoder outputs and the hidden state of the decoder as inputs and returns attention weights.
 - The `Decoder` class represents the decoder module of the Seq2Seq model. It takes input parameters such as `output_size` (target vocabulary size), `embed_size` (embedding layer dimension), `enc_hid_dim` (encoder hidden state size), `dec_hid_dim` (decoder hidden state size), `num_layers` (number of decoder layers), `cell_mode` (cell type for the decoder: LSTM, GRU, or RNN), `dropout` (dropout probability for the decoder), `attention` (attention module used by the decoder), and `is_bi` (flag indicating if the encoder is bidirectional)
 - The `forward` method of the `Decoder` class performs the forward pass of the decoder. It takes a target tensor for a single time step, encoder outputs, and the hidden and cell states of the decoder (optional for LSTM) as inputs and returns the output prediction for the time step, the new hidden state of the decoder, and the new cell state of the decoder (optional for LSTM).
- model is saved with the name 'noattn_model.model'
- predictions saved in 
predictions_attention.txt  can be loaded with: ```np.loadtxt('predictions_attention.txt ',delimiter=',',encoding='utf-8',dtype=str)```

# Arguements taken by model:
Make Model function

The `make_model` function is responsible for creating an instance of a Seq2Seq model. It takes several arguments:

1. `train_iterator` and `valid_iterator`: These are the iterators for the training and validation data, respectively. They provide batches of data for training and evaluation.

2. `cell_mode`: This argument specifies the type of cell to be used in the encoder and decoder. It can be 'lstm', 'gru', or 'rnn'.

3. `dec_embed_size` and `dec_hid_size`: These arguments define the dimensions of the embedding layer and the hidden state size of the decoder.

4. `dropout`: This argument specifies the dropout probability for the encoder and decoder layers. It helps in regularization by randomly setting a fraction of the input units to 0 during training.

5. `enc_embed_size` and `enc_hid_size`: These arguments define the dimensions of the embedding layer and the hidden state size of the encoder.

6. `epochs`: This argument determines the number of epochs for training the model. An epoch refers to a complete pass through the entire training dataset.

7. `is_bi`: This argument is a boolean flag indicating whether the encoder should be bidirectional or not.

8. `num_layers`: This argument specifies the number of layers in the encoder and decoder.

The `make_model` function creates an instance of the Seq2Seq model by initializing the encoder, attention, and decoder modules. It then sets up the training and evaluation processes using the provided iterators and hyperparameters. The function returns the created Seq2Seq model.

In Vanilla, we fix the hidden layers of encoder and decoder to be the same, but it is not essential


# Report Link:
PFA wandb report link:
https://wandb.ai/pragalbh/DL_Assign3/reports/Transliteration-CS6910-Assignment-3--Vmlldzo0NDk2Mzg3


