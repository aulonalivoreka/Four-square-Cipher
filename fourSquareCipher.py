alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y']

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