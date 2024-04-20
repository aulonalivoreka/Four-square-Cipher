# Second Project in Data Security 
This project was completed by sophomore students from the Faculty of Electrical and Computer Engineering at the University of Hasan Prishtina, under the expert guidance of Prof. Dr. Blerim Rexha and Ass. Mërgim Hoti, as part of our coursework in Data Security.

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
Python 3.9. Ensure Python 3 is installed on your system.
Download the script fourSquareCipher.py to your local machine.
Open a terminal or command prompt.
Navigate to the directory where the script is located.
To run the script, execute the following command in your terminal:

```bash
python fourSquareCipher.py
``` 

### How It Works
- **Input Keys**: The user is prompted to enter two keys for the matrices. These keys should contain letters from A-Z (excluding Q) and should not have spaces.
- **Input Message**: The user is prompted to input the message to be encrypted. Spaces are allowed but will be filtered out.
- **Encryption**: The script divides the input message into digraphs (pairs of letters), finds their positions in the reference matrix, and transforms them according to the key matrices to produce the ciphertext.
- **Decryption**: The script uses the encrypted message and the key matrices to retrieve the original message by reversing the encryption process.

#### Functions
- `getData`: Prompts for and validates user input.
- `makeKeyMatrix`: Creates a 5x5 matrix for a given key.
- `makeReferenceMatrix`: Generates the default reference matrix.
- `printMatrix`: Displays a matrix in a readable 5x5 format.
- `encrypt`: Encrypts the message using two key matrices.
- `decrypt`: Decrypts the message using the same matrices.

### Example Usage

**Input:**

- Enter Key 1 (only A-Z, excluding Q): `EXAMPLE`
- Enter Key 2 (only A-Z, excluding Q): `CIPHER`
- Enter the message to encrypt (only A-Z, excluding Q): `HELLO WORLD`

**Output:**  
`****** Four Square Cipher ******`

**Key 1 Matrix:**
```
E X A M P
L B C D F
G H I J K
N O R S T
U V W Y Z
```

**Key 2 Matrix:**
```
C I P H E
R A B D F
G J K L M
N O Q S T
U V W X Y
```

**Reference Matrix:**
```
A B C D E
F G H I J
K L M N O
P R S T U
V W X Y Z
```

**Encrypted Message:** `FPHJKZZJOJM`  
**Decrypted Message:** `HELLOZWORLD`

## Notes
- Key 1 and Key 2 matrixes are case-sensitive (excluding Q character and spaces) and the encryption and decryption handle only alphabetic characters.
- Error handling is in place for invalid inputs.


### Authors 

- [Aulona Livoreka](https://github.com/aulonalivoreka)
- [Artina Qorrolli](https://github.com/ArtinaQorrolli)
- [Aulona Ramosaj](https://github.com/aulonaramosaj)
- [Artin Dulahi](https://github.com/ArtinDulahi)

