def sequence(n):
    arr = []
    i = 0
    while i < n:
        arr.append(i)
        i += 1
    i -= 2
    while i > 0:
        arr.append(i)
        i -= 1
    return arr

def railfence(cipher_text, n):
    cipher_text = cipher_text.lower()
    L = sequence(n)
    print("The raw sequence of indices: ", L)
    temp = L.copy()
    while len(cipher_text) > len(L):
        L += temp
    for i in range(len(L) - len(cipher_text)):
        L.pop()

    temp1 = sorted(L)
    print("The row indices of the characters in the cipher string: ", L)
    print("The row indices of the characters in the plain string: ", temp1)
    print("Transformed message for decryption: ", cipher_text)

    plain_text = ""
    for i in L:
        k = temp1.index(i)
        temp1[k] = n
        plain_text += cipher_text[k]

    print("The plain text is: ", plain_text)

cipher_text = "horelollwd"
n = 3
railfence(cipher_text, n)
