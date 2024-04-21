#Definimi i alfabetit valid per enkriptim dhe dekriptim pa shkronjen Q
alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','R','S','T','U','V','W','X','Y','Z']

def getData(prompt, allow_spaces=False):
    #Prompt userin per input, duke siguruar qe vetem karakteret valide alfabetike dhe opsionalisht spaces (te plaintext) perfshihen 
    while True:
         #Merr user input dhe konverto ne uppercase
        dataInput = input(prompt).upper()
    
    # Check nese lejohen spaces
    if allow_spaces:
            # Perfshi spaces ne te dhenat e filtruara nese lejohet
            filtered_data = ''.join([char for char in dataInput if char in alphabet or char == ' '])
     else:
            filtered_data = ''.join([char for char in dataInput if char in alphabet])
         
                 
    # Valido inputin bazuar nese lejohen spaces apo jo 
        if not allow_spaces and len(filtered_data) != len(dataInput):
            print("Invalid input. Please use only alphabetic characters from A-Z.")
        elif allow_spaces and not all(char in alphabet or char == ' ' for char in dataInput):
            print("Invalid input. Please use only alphabetic characters from A-Z.")
        else:
            return filtered_data

def makeKeyMatrix(key):
    #Krijo nje matrice 5x5 nga celesi i dhene, duke larguar duplikatet dhe duke bere i permbushur me shkronjat e mbetura
    seen = set()
    #Filtro karakteret duplikat dhe krijo matricen 
    matrix = [char for char in key if char in alphabet and not (char in seen or seen.add(char))]
    matrix += [char for char in alphabet if char not in seen]
    return ''.join(matrix)

def makeReferenceMatrix():
    return ''.join(alphabet)

def printMatrix(matrix):
    for i in range(0, len(matrix), 5):
        print(" ".join(matrix[i:i+5]))



def removeDuplicates(key):
    # Largohen karakteret duplikat nga nje string
    seen = set()
    return ''.join([char for char in key if not (char in seen or seen.add(char))])

def evaluate(ref1, ref2):
    # Evaluohet pozita e re bazuar ne transformimin e rreshtave dhe kolonave 
    # Aplikohet formula per te percaktuar poziten e re
    return (ref1 // 5) * 5 + ref2 % 5

def search(matrix, letter):
    # Return indeksin e shkronjes ne matrice
    return matrix.index(letter) if letter in matrix else -1



def encrypt(message, key1, key2):
    # Enkripto mesazhin duke perdorur dy celesat e matrices
    # Krijo matricat bazuar ne celesat dhe matricen referente 
    matrix1 = makeKeyMatrix(removeDuplicates(key1))
    matrix2 = makeKeyMatrix(removeDuplicates(key2))
    refMatrix = makeReferenceMatrix()

    # Paraqit matricat e celesave dhe matricen referente 
    print("\nKey 1 Matrix:")
    printMatrix(matrix1)
    print("\nKey 2 Matrix:")
    printMatrix(matrix2)
    print("\nReference Matrix:")
    printMatrix(refMatrix)

    encrypted = []
    # Itero ne mesazh permes cifteve te karaktereve 
    for i in range(0, len(message), 2):
        if i + 1 < len(message):
            # Gjej pozitat e karaktereve ne matricen referente
            a, b = search(refMatrix, message[i]), search(refMatrix, message[i+1])
            # Enkrito karakteret duke perdorur matricat e celesave 
            encrypted.append(matrix1[evaluate(a, b)])
            encrypted.append(matrix2[evaluate(b, a)])
        else:
            # Menaxhimi i rastit kur kemi numer tek te karaktereve
            a = search(refMatrix, message[i])
            encrypted.append(matrix1[a]) 

    return ''.join(encrypted)
    

def decrypt(ciphertext, key1, key2):
    # Dekripto mesazhin duke perdorur matricat e celesave 
    matrix1 = makeKeyMatrix(removeDuplicates(key1))
    matrix2 = makeKeyMatrix(removeDuplicates(key2))
    refMatrix = makeReferenceMatrix()

    decrypted = []
    for i in range(0, len(ciphertext), 2):
        if i + 1 < len(ciphertext):
            a, b = search(matrix1, ciphertext[i]), search(matrix2, ciphertext[i+1])
            decrypted.append(refMatrix[evaluate(a, b)])
            decrypted.append(refMatrix[evaluate(b, a)])
        else:
            a = search(matrix1, ciphertext[i])
            decrypted.append(refMatrix[a])

    return ''.join(decrypted)
    

def main():
    print("****** Four Square Cipher *******\n")
    key1 = getData("Enter Key 1 (only A-Z, excluding Q): ", allow_spaces=False)
    key2 = getData("Enter Key 2 (only A-Z, excluding Q): ", allow_spaces=False)
    message = getData("Enter the message to encrypt (only A-Z, excluding Q): ", allow_spaces=True)

    encrypted_message = encrypt(message, key1, key2)
    print("\nEncrypted Message: ", encrypted_message)

    decrypted_message = decrypt(encrypted_message, key1, key2)
    print("\nDecrypted Message: ", decrypted_message)

if __name__ == "__main__":
    main()

