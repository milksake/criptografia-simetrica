def cifrarPorColFil(message, nCol):
    newMessage = ""
    for i in range (nCol):
        for j in range(0, len(message), nCol):
            newMessage += message[j + i]
    return newMessage

if __name__ == "__main__":
    x = cifrarPorColFil("ALGEBRAABSTRACTA", 4)
    print(x, cifrarPorColFil(x, 4))
