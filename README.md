# Second Project in Data Security 

## Encryption and Decryption Using the Four-Square Cipher

The Four-square cipher is a type of polygraphic substitution cipher that encodes pairs of letters (digraphs), enhancing its security compared to simpler substitution ciphers. This method was developed by Félix Delastelle, a French amateur cryptographer, and first described in 1902. While similar to the Playfair cipher, the Four-square cipher employs four 5x5 matrices, adding complexity to the encryption process.

## Structure of the Cipher
The Four-square cipher uses four 5x5 grids:
Grids 1 and 4 (Plaintext grids) are typically filled with a standard alphabet sequence, omitting 'Q' to fit the 25 spaces.
Grids 2 and 3 (Ciphertext grids) are filled using a keyword or phrase, ensuring no repeated letters and also omitting 'Q'. After the keyword is placed, the remaining alphabetic characters are filled in sequentially.

## Encryption Process
Divide the plaintext message into digraphs. If there's an odd number of letters, append filler letters.
For each digraph locate the first letter in the top left grid (Grid 1) and the second letter in the bottom left grid (Grid 4). Determine the new letters by finding the letter in the same row as the first letter in Grid 1 from the top right grid (Grid 2), and the letter in the same column as the second letter in Grid 4 from the bottom right grid (Grid 3).
These selected letters from the ciphertext grids form the encrypted digraph.

## Decryption Process
The decryption process mirrors encryption but uses the positions of letters in the ciphertext to retrieve the original plaintext:
For each digraph in the ciphertext, identify the positions of the letters in the top right (Grid 2) and bottom right (Grid 3).
Using the row of the first letter and the column of the second letter, find the corresponding plaintext letters in the top left (Grid 1) and bottom left (Grid 4) grids.

## Four-Square Cipher Implementation
This Python script implements the Four-square cipher. This implementation excludes the letter 'Q' from the alphabet to fit the matrix and allows for encryption and decryption of messages using two separate keys.

### Requirements
Python 3.9
Ensure Python 3 is installed on your system.
Download the script fourSquareCipher.py to your local machine.
Open a terminal or command prompt.
Navigate to the directory where the script is located.
Running the Script
To run the script, execute the following command in your terminal: 

```bash
python fourSquareCipher.py
``` 
### Authors 

- [Aulona Livoreka](https://github.com/aulonalivoreka)
- [Artina Qorrolli](https://github.com/ArtinaQorrolli)
- [Aulona Ramosaj](https://github.com/aulonaramosaj)
- [Artin Dulahi](https://github.com/ArtinDulahi)

