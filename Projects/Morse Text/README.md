# Morse Coder and Decoder

This Python script provides functionality to encode and decode text to/from Morse code.

## Features

- Encode text to Morse code.
- Decode Morse code to text.

## Usage

You can directly copy and past the python code in your local mechanic and run to generate morse code  
You can modify and expand this template to suit your specific project needs.  
  
## How this works
Here's an explanation of how the Morse Coder and Decoder script works:

1. **Morse Code Dictionary**: The script starts by defining a dictionary called `morse_code_dict`, which maps characters to their Morse code equivalents. Each letter, digit, and some punctuation marks are assigned their respective Morse code sequences.

2. **Morse Encoder**: The `morse_coder` function takes a string of text as input. It iterates over each character in the input text, converting each character to its uppercase form. If the character is found in the `morse_code_dict`, its Morse code equivalent is retrieved and added to a list. Non-alphanumeric characters are kept unchanged. Finally, the list of Morse code equivalents is joined together with spaces and returned as the encoded Morse code.

3. **Morse Decoder**: The `morse_decoder` function takes a string of Morse code as input. It splits the Morse code string into words using the separator "/". Then, it splits each word into Morse code characters using spaces as the separator. Each Morse code character is looked up in the `morse_code_dict` dictionary to find its corresponding letter. Non-Morse code characters are kept unchanged. The decoded letters are then joined together to form words, and the words are joined to form the final decoded text, which is returned.

4. **Example Usage**: The script demonstrates how to use the Morse Coder and Decoder by providing an example with the `MorseCoderDecoder` class. It shows how to encode the text "Hello, World!" and then decode the encoded Morse code back to the original text.

Overall, the script provides a simple and straightforward way to encode text to Morse code and decode Morse code back to text using a predefined dictionary mapping.



