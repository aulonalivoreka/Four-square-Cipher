#alfabeti pa shkronjen Q 

alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','R','S','T','U','V','W','X','Y','Z']


def getData():
    dataInput = input()
    return ''.join([char for char in dataInput.upper() if char in alphabet])

def makeKeyMatrix(key):
    seen = set()
    matrix = [char for char in key if char in alphabet and not (char in seen or seen.add(char))]
    matrix += [char for char in alphabet if char not in seen]
    return ''.join(matrix)

def makeReferenceMatrix():
    return ''.join(alphabet)

def printMatrix(matrix):
    for i in range(0, len(matrix), 5):
        print(" ".join(matrix[i:i+5]))

if allow_spaces:
# Perfshi spaces ne te dhenat e filtruara nese lejohet
            filtered_data = ''.join([char for char in dataInput if char in alphabet or char == ' '])
     else:
            filtered_data = ''.join([char for char in dataInput if char in alphabet])

def removeDuplicates(key):
    seen = set()
    return ''.join([char for char in key if not (char in seen or seen.add(char))])


def evaluate(ref1, ref2):
    return (ref1 // 5) * 5 + ref2 % 5

def search(matrix, letter):
    return matrix.index(letter) if letter in matrix else -1


def encrypt(message, key1, key2):
    matrix1 = makeKeyMatrix(removeDuplicates(key1))
    matrix2 = makeKeyMatrix(removeDuplicates(key2))
    refMatrix = makeReferenceMatrix()

    print("\nKey 1 Matrix:")
    printMatrix(matrix1)
    print("\nKey 2 Matrix:")
    printMatrix(matrix2)
    print("\nReference Matrix:")
    printMatrix(refMatrix)

    encrypted = []
    for i in range(0, len(message), 2):
        if i + 1 < len(message):
            a, b = search(refMatrix, message[i]), search(refMatrix, message[i+1])
            encrypted.append(matrix1[evaluate(a, b)])
            encrypted.append(matrix2[evaluate(b, a)])
        else:
            a = search(refMatrix, message[i])
            encrypted.append(matrix1[a]) 

    return ''.join(encrypted)
    

def decrypt(ciphertext, key1, key2):
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
    print("** Four Square Cipher ***\n")
    print("Enter Key 1: ", end=' ')
    key1 = getData()
    print("\nEnter Key 2: ", end=' ')
    key2 = getData()
    print("\nEnter the message to encrypt (only A-Z): ", end=' ')
    message = getData()

    encrypted_message = encrypt(message, key1, key2)
    print("\nEncrypted Message: ", encrypted_message)

    decrypted_message = decrypt(encrypted_message, key1, key2)
    print("\nDecrypted Message: ", decrypted_message)

if __name__ == "__main__":
    main()

