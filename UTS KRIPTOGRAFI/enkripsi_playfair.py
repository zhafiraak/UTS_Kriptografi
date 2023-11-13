def initializeMatrix(key):
    key = key.replace("j", "i")
    key += "abcdefghijklmnopqrstuvwxyz"
    key = "".join(dict.fromkeys(key))
    
    matrix = [[0] * 5 for _ in range(5)]
    k = 0
    for i in range(5):
        for j in range(5):
            matrix[i][j] = key[k]
            k += 1
    return matrix

def prepareText(text):
    text = text.replace("j", "i")
    if len(text) % 2 != 0:
        text += "x"
    return text

def findPosition(matrix, char):
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == char:
                return (i, j)

def playfairEncrypt(password, matrix):
    encrypted_password = ""
    for i in range(0, len(password), 2):
        char1, char2 = password[i], password[i + 1]
        row1, col1 = findPosition(matrix, char1)
        row2, col2 = findPosition(matrix, char2)

        if row1 == row2:
            col1 = (col1 + 1) % 5
            col2 = (col2 + 1) % 5
        elif col1 == col2:
            row1 = (row1 + 1) % 5
            row2 = (row2 + 1) % 5
        else:
            col1, col2 = col2, col1

        encrypted_password += matrix[row1][col1] + matrix[row2][col2]

    return encrypted_password
